# westddns-py
# https://github.com/bddjr/westddns-py

from urllib.parse import quote
import requests, json, time, logging, re

logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s %(asctime)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logging.info("westddns-py start!")

with open("conf.json") as f:
    conf = json.load(f)

domain = quote(str(conf["domain"]))
hostname = quote(str(conf["hostname"]))
apidomainkey = quote(str(conf["apidomainkey"]))

ipa = None
success = False

reGetIPv4Address = re.compile(r"(\d{1,3}\.){3}\d{1,3}")


def do():
    global domain, hostname, apidomainkey, ipa, success
    success = False
    try:
        resp = requests.get("https://ddns.oray.com/checkip")
        if resp.ok:
            respText = reGetIPv4Address.search(resp.text).group()
            if ipa == respText:
                success = True
            else:
                ipa = respText
                logging.info(ipa)
                record_value = quote(str(ipa))
                resp = requests.get(
                    f"https://api.west.cn/API/v2/domain/dns/?act=dnsrec.update&domain={domain}&hostname={hostname}&record_value={record_value}&apidomainkey={apidomainkey}"
                )
                if resp.ok:
                    logging.info("Set DNS record success!")
                    success = True
                else:
                    logging.error(f"Set DNS record failed! Code: {resp.status_code}")
        else:
            logging.error(f"Get IP address failed! Code: {resp.status_code}")
    except Exception as e:
        logging.exception(e)


try:
    while True:
        do()
        time.sleep(60 if success else 10)
except KeyboardInterrupt:
    print("^C")
