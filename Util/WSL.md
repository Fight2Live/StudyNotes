

# SSH连接

## Linux环境配置

```shell
#客户端
sudo apt-get install openssh-client
#服务器
sudo apt-get install openssh-server
#或
apt-get install ssh
 
#/etc/ssh/sshd_config件更改包括端口、是否允许root登录等设置
#默认是不允许root远程登录的
#开启：找到PermitRootLogin without-password 修改为PermitRootLogin yes 
# 推荐通过新建账号来连接
sudo vi /etc/ssh/sshd_config
 
#重启
sudo service ssh --full-restart

# 
```



## 宿主机配置

```shell
# netsh interface portproxy add v4tov4 listenport=[win10端口] listenaddress=0.0.0.0 connectport=[虚拟机的端口] connectaddress=[虚拟机的ip]
netsh interface portproxy add v4tov4 listenport=22 listenaddress=0.0.0.0 connectport=22 connectaddress=172.22.22.22
 
#检测是否设置成功
netsh interface portproxy show all
 
#删除端口映射
netsh interface portproxy delete v4tov4 listenaddress=监听地址 listenport=监听端口
```



**要注意网路共享配置是否打开！！两台设备是否能ping通！！**


