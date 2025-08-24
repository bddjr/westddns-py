# westddns-py

[西部数码](https://www.west.cn)专用的 DDNS 脚本。

## 在 Linux 安装

依赖：
> python3  
> git  

1. 克隆仓库并设置权限

```bash
sudo bash -c "git clone https://github.com/bddjr/westddns-py /opt/westddns-py && chmod 700 /opt/westddns-py"
```

2. 创建并填写配置文件。  
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
sudo bash -c "cp /opt/westddns-py/westddns.service /etc/systemd/system/ && systemctl daemon-reload"
```

4. 运行服务（开机自启）

```bash
sudo systemctl enable --now westddns
```
