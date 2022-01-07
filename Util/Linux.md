



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

