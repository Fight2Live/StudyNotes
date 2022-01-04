



## 挂载多个硬盘到一个目录下

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

