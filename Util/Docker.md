

# 概述



### 镜像（image）

docker镜像就好比是一个模板，可以通过这个模板来创建容器服务。

> 如：tomcat镜像=》run=》tomcat01 容器（提供服务器）

通过这个镜像可以创建多个容器（最终服务运行或者项目运行就是在容器中的）。



### 容器（container）

docker利用容器技术，独立运行一个或者一组应用，通过镜像来创建的。



### 仓库（repository）

存放镜像的地方。

分为私有和公有仓库。







# 底层原理

**Docker是如何工作的？**

Docker是一个CS结构的系统，以守护进程运行在主机上，通过Socket从客户端访问。

DockerServer接收到client的指令就会执行



**Docker为什么比VM快？**

1、Docker有着比虚拟机更少的抽象层。

2、docker利用的是宿主机的内核，vm需要GuestOS





# 常用命令



## 帮助命令



## 镜像命令



## 容器命令