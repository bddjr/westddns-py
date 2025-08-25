# westddns-py
# https://github.com/bddjr/westddns-py

from urllib.parse import quote
import requests, json, time, logging

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


def do():
    global domain, hostname, apidomainkey, ipa, success
    success = False
    try:
        resp = requests.get(conf["get_ip_from"])
        if resp.ok:
            respText = resp.text.strip()
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
    while not success:
        do()
        time.sleep(10)
    while True:
        do()
        time.sleep(60)
except KeyboardInterrupt:
    print("^C")
