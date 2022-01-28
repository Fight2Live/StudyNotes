



>linux系统基本上分两大类：
>1 RedHat系列：Redhat、Centos、Fedora等
>2 Debian系列：Debian、Ubuntu等

>RedHat 系列：
>1 常见的安装包格式 rpm 包，安装rpm包的命令是 “rpm -参数”
>2 包管理工具 yum
>3 支持tar包

>Debian系列：
>1 常见的安装包格式 deb 包，安装deb包的命令是 “dpkg -参数”
>2 包管理工具 apt-get
>3 支持tar包

# 常用命令

## 重命名



```SHELL
# 可以用mv a b 来进行重命名
mv a.txt b.txt
```





## 删除



```shell
rm -f file_name	# 删除指定文件
rm -f *			# 删除当前目录下的所有文件
rm -f *.txt		# 删除当前目录下所有txt文件
rm -fr dir_path	# 删除文件夹即所有子文件
```



## 端口

```SHELL
lsof -i:端口号
lsof -i:8080：查看8080端口占用
lsof abc.txt：显示开启文件abc.txt的进程
lsof -c abc：显示abc进程现在打开的文件
lsof -c -p 1234：列出进程号为1234的进程所打开的文件
lsof -g gid：显示归属gid的进程情况
lsof +d /usr/local/：显示目录下被进程开启的文件
lsof +D /usr/local/：同上，但是会搜索目录下的目录，时间较长
lsof -d 4：显示使用fd为4的进程
lsof -i -U：显示所有打开的端口和UNIX domain文件

netstat [-tunlp] | grep 端口号
# -t (tcp) 仅显示tcp相关选项
# -u (udp)仅显示udp相关选项
# -n 拒绝显示别名，能显示数字的全部转化为数字
# -l 仅列出在Listen(监听)的服务状态
# -p 显示建立相关链接的程序名
```



## chmod

控制文件的权限

```SHELL
chmod [-cfvR] [--help] [--version] mode file...

-c : 若该文件权限确实已经更改，才显示其更改动作
-f : 若该文件权限无法被更改也不要显示错误讯息
-v : 显示权限变更的详细资料
-R : 对目前目录下的所有文件与子目录进行相同的权限变更(即以递归的方式逐个变更)
```



| #    | 权限           | rwx  | 二进制 |
| :--- | :------------- | :--- | :----- |
| 7    | 读 + 写 + 执行 | rwx  | 111    |
| 6    | 读 + 写        | rw-  | 110    |
| 5    | 读 + 执行      | r-x  | 101    |
| 4    | 只读           | r--  | 100    |
| 3    | 写 + 执行      | -wx  | 011    |
| 2    | 只写           | -w-  | 010    |
| 1    | 只执行         | --x  | 001    |
| 0    | 无             | ---  | 000    |




# 查看系统信息

```shell
# 电脑及操作系统信息
uname -a

# 内核版本
cat /proc/version

# 发行版本 
cat /etc/issue
```





# Ubuntu安装IP相关的tool

```SHELL
apt-get update
apt-get install ethtool
apt-get install iproute2
apt-get install bridge-utils
apt-get install iputils-ping
```





# Ubuntu安装python

#### 1. 升级

```shell
# sudo apt update
# sudo apt upgrade -y
```

#### 2. 安装编译Python源程序所需的包

```shell
# sudo apt install build-essential -y
# sudo apt install libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev -y
# sudo apt-get install libbz2-dev
# sudo apt-get install zlib1g-dev

```

#### 3. 下载Python源程序压缩包

（或者直接在Python官网下载Linux安装包）

```shell
# wget https://www.python.org/ftp/python/3.7.1/Python-3.7.1.tgz
```

#### 4. 解压

```shell
# tar -xzvf Python-3.7.1.tgz
```

#### 5. 配置

```shell
# cd Python-3.7.1
# ./configure --enable-optimizations
```

#### 6. 编译和安装

```shell
# sudo make
# sudo make install
```

#### 7. 查看Python版本

```shell
# python3
Python 3.7.1 (default, Nov 21 2018, 16:35:49) 
[GCC 7.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

**安装成功！**

------

由于用Pip安装软件包速度很慢，因为要访问外网的。这里可以选择国内的源，这里以清华源为例。

#### 8. 升级Pip和更换Pip源

```shell
# sudo pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
# pip3 install --upgrade pip
```



# 安装npm

```SHELL
# 下载安装包
cd ~
wget https://nodejs.org/dist/v14.15.4/node-v14.15.4-linux-x64.tar.xz
# 解压并移动
tar -xf node-v14.15.4-linux-x64.tar.xz
mv node-v14.15.4-linux-x64 /usr/local/node
# 建立软链接
cd /usr/bin
ln -s /usr/local/node/bin/node node
ln -s /usr/local/node/bin/npm npm

# 设置镜像
npm config set registry https://registry.npm.taobao.org
# cnpm
npm install -g cnpm --registry=https://registry.npm.taobao.org
cd /usr/bin
ln -s /usr/local/node/bin/cnpm cnpm

```





# 挂载多个硬盘到一个目录下

- PV（Physical Volume）- 物理卷
  物理卷在逻辑卷管理中处于最底层，它可以是实际物理硬盘上的分区，也可以是整个物理硬盘，也可以是raid设备。

- VG（Volumne Group）- 卷组
  卷组建立在物理卷之上，一个卷组中至少要包括一个物理卷，在卷组建立之后可动态添加物理卷到卷组中。一个逻辑卷管理系统工程中可以只有一个卷组，也可以拥有多个卷组。

- LV（Logical Volume）- 逻辑卷
  逻辑卷建立在卷组之上，卷组中的未分配空间可以用于建立新的逻辑卷，逻辑卷建立后可以动态地扩展和缩小空间。系统中的多个逻辑卷可以属于同一个卷组，也可以属于不同的多个卷组

- PE（Physical Extent）- 物理块



```shell
# 查看当前磁盘信息
fdisk -l  
# 对硬盘进行分区
fdisk /dev/硬盘名  
# 然后依次输入 n p 1 回车 回车 t l 8e w
# n：创建分区
# p：扩展分区
# 1：分区号(1-4)
# t：修改分区类型
# l：列出所有分区类型
# 8e：指Linux LVM
# w：保存并退出

# 创建PV
pvcreate /dev/硬盘1 /dev/硬盘2 ...
# 查看PV
pvdisplay

# 创建卷组
vgcreate 卷组名 /dev/硬盘1 /dev/硬盘2 ...
# 查看卷组
vgs

# 创建逻辑卷
lvcreate -l 100%VG -n 逻辑卷名 卷组名

# 格式化。
mkfs.ext3 /dev/卷组名/逻辑卷名

# 创建挂载目录
mkdir /new_dir

# 挂载
mount /dev/卷组名/逻辑卷名 挂载目录

# 开机挂载
vim /etc/fstab
# 加上 /dev/卷组名/逻辑卷名 挂载目录 ext3 defaluts 1 2
```

