# Python环境配置

这里可以根据需要，可以直接在[Python官网](https://www.python.org/)下载对应版本进行安装，也可以选择安装Anaconda来使用和统一管理python

## Anaconda

1、[官网安装]([Anaconda | Anaconda Distribution](https://www.anaconda.com/products/distribution#windows))

2、添加环境变量

```shell
# 在Path下添加
G:\ProgramData\Anaconda3
G:\ProgramData\Anaconda3\Scripts
G:\ProgramData\Anaconda3\Library\bin
G:\ProgramData\Anaconda3\Library\mingw-w64\bin
```

## 设置Pip下载源

- 在`%APPDATA%`下新建`pip`文件夹，创建文件`%APPDATA%/pip/pip.ini`：

```shell
[global]
timeout = 6000
index-url = https://mirrors.aliyun.com/pypi/simple/
trusted-host = mirrors.aliyun.com
```

- 或者在命令行输入：

```shell
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```



> 国内常用源
> 
> pypi 清华大学源：https://pypi.tuna.tsinghua.edu.cn/simple
> pypi 腾讯源：http://mirrors.cloud.tencent.com/pypi/simple
> pypi 阿里源：https://mirrors.aliyun.com/pypi/simple/
> pypi 豆瓣源 ：http://pypi.douban.com/simple/



## PyCharm破解

1、下载[2022.2.2专业版](https://download.jetbrains.com/python/pycharm-professional-2022.2.2.exe)

2、下载破解补丁`ja-netfilter`

3、进入 Pycharm 的安装目录，在 `/bin` 目录下，修改 `pycharm64.exe.vmoptions` 配置文件，在末尾处添加：

```shell
# 引用补丁，开头必须以 -javaagent: 开头，后面跟着补丁的绝对路径（可根据你实际的位置进行修改）,注意路径一定要填写正确，且不能包含中文，否则会导致 Pycharm 无法启动
-javaagent:D:/ja-netfilter/ja-netfilter.jar

# 最新 Pycharm 版本需要添加下面两行，否则会报 key valid
--add-opens=java.base/jdk.internal.org.objectweb.asm=ALL-UNNAMED
--add-opens=java.base/jdk.internal.org.objectweb.asm.tree=ALL-UNNAMED
```

4、重启PyCharm

5、填入激活码





# Java环境配置

## JDK

1、[官网下载](https://www.java.com/zh-CN/download/)安装

2、配置环境变量

- 新增变量
  
  - `JAVA_HOME`：`C:\Program Files\Java\jdk1.8.0_211`
  
  - `CLASSPATH`：`.;%JAVA_HOME%\lib\dt.jar;%JAVA_HOME%\lib\tools.jar;`

- 在`Path`中添加
  
  - `%JAVA_HOME%\bin;%JAVA_HOME%\jre\bin;`

3、测试安装是否成功：

- 在CMD中输入`java`, `javac` 都不报错即算成功



## IDEA破解

1、下载[2022.2.2专业版](https://download.jetbrains.com/idea/ideaIU-2022.2.2.exe)

2、下载破解补丁`ja-netfilter`

3、进入 Pycharm 的安装目录，在 `/bin` 目录下，修改 `pycharm64.exe.vmoptions` 配置文件，在末尾处添加：

```shell
# 引用补丁，开头必须以 -javaagent: 开头，后面跟着补丁的绝对路径（可根据你实际的位置进行修改）,注意路径一定要填写正确，且不能包含中文，否则会导致 Pycharm 无法启动
-javaagent:D:/ja-netfilter/ja-netfilter.jar

# 最新 Pycharm 版本需要添加下面两行，否则会报 key valid
--add-opens=java.base/jdk.internal.org.objectweb.asm=ALL-UNNAMED
--add-opens=java.base/jdk.internal.org.objectweb.asm.tree=ALL-UNNAMED
```

4、重启IDEA

5、填入激活码





# MySQL

1、[官网下载](https://dev.mysql.com/downloads/installer/)

2、MSI安装包一路往下





# Git

1、[官网下载](https://git-scm.com/)

2、SSH

- 配置信息

```shell
git config --global user.name "youe_name"
git config --global user.email "your_email@example.com"
```

- 生成

```shell
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```

- 三次回车

3、默认公钥地址：`C:\Users\30935\.ssh\id_rsa.pub`


