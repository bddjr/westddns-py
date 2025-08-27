# westddns-py

[西部数码](https://www.west.cn)专用的 DDNS 脚本，暂时仅支持 IPv4 地址。

## 在 Linux 安装

1. 安装脚本依赖

```bash
pip3 install requests
```

2. 创建目录

```bash
sudo mkdir -m 700 -p /opt/westddns-py
```

3. 获取脚本

```bash
sudo curl https://raw.githubusercontent.com/bddjr/westddns-py/refs/heads/main/westddns.py -o /opt/westddns-py/westddns.py
```

4. 创建并填写配置文件。  
   `apidomainkey`请参考 <https://www.west.cn/docs/505763.html> 填写。

```bash
sudo nano /opt/westddns-py/conf.json
```

```json
{
	"apidomainkey": "",
	"domain": "example.com",
	"hostname": "ddns.example.com"
}
```

5. 创建服务

```bash
sudo bash -c "curl https://raw.githubusercontent.com/bddjr/westddns-py/refs/heads/main/westddns.service -o /etc/systemd/system/westddns.service && systemctl daemon-reload"
```

6. 运行服务（开机自启）

```bash
sudo systemctl enable --now westddns
```
