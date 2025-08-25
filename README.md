# westddns-py

[西部数码](https://www.west.cn)专用的 DDNS 脚本。

## 在 Linux 安装

依赖：

> python3  
> git

1. 创建目录

```bash
sudo mkdir -m 700 -p /opt/westddns-py
```

2. 获取脚本

```bash
sudo curl https://raw.githubusercontent.com/bddjr/westddns-py/refs/heads/main/westddns.py -o /opt/westddns-py/westddns.py
```

3. 创建并填写配置文件。  
   `apidomainkey`请参考 <https://www.west.cn/docs/505763.html> 填写。

```bash
sudo nano /opt/westddns-py/conf.json
```

```json
{
	"apidomainkey": "",
	"domain": "example.com",
	"hostname": "ddns.example.com",
	"get_ip_from": "https://4.ipw.cn"
}
```

3. 创建服务

```bash
sudo bash -c "curl https://raw.githubusercontent.com/bddjr/westddns-py/refs/heads/main/westddns.service -o /etc/systemd/system/westddns.service && systemctl daemon-reload"
```

4. 运行服务（开机自启）

```bash
sudo systemctl enable --now westddns
```
