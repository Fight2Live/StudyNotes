



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

```shell
docker version		# 版本信息
docker info			# 详细信息
docker 命令 --help   # 查看对应命令的使用方法

```

[官方文档](https://docs.docker.com/reference/)



## 镜像命令

**查看镜像**

```shell
docker images [option]	# 查看本地所有镜像
  -a, --all             # 列出所有镜像
  -q, --quiet           # 只显示镜像ID
```



**搜索镜像**

```SHELL
docker search (name) [option]	# 搜索镜像
	-f, --filter				# 过滤条件
```



**下载镜像**

```shell
docker pull (name[:tag]) [option]	# 下载镜像，如果不写tag，默认取最新版本.
# pull时镜像是分层下载，联合文件系统。
```



**删除镜像**

```shell
docker rmi -f (image)[image2, image3]		# 删除指定镜像
docker rmi -f $(docker images -aq)			# 全部删除
```



## 容器命令

**启动容器**

```shell
docker run [option] image		# 新建容器并启动
# 参数说明
--name="Name"	容器名字
-d				以后台方式运行
-it				使用交互方式运行，可以进入容器查看内容
-p				指定容器端口	-p 8080:8080
	-p ip:主机端口:容器端口
	-p 主机端口:容器端口
	-p 容器端口
-P				随即指定端口
```



**查看容器**

```shell
docker ps [option]	# 列出正在运行的容器
	-a				# 列出正在运行的容器与历史运行过的容器
	-n=?			# 显示最近创建的n个容器
	-q				# 只显示容器的编号
```



**退出容器**

```shell
exit		# 停止容器并退出
ctrl+P+Q	# 不停止容器，只退出
```



**删除容器**

```shell
docker rm 容器id					# 删除指定容器
docker rm -f $(docker ps -aq)	 # 删除所有容器
docker ps -a -q|xargs docker rm	 # 删除所有容器
```



**启动和停止**

```shell
docker start 容器id		# 启动
docker restart 容器id		# 重启
docker stop	容器id		# 停止正在运行的
docker kill 容器id		# 强制停止当前容器
```



**后台启动容器**

```SHELL
docker run -d centos	# 想后台运行容器
# 然后发现centos停止了
# 常见的坑：docker容器使用后台运行时，必须要有一个前台进程，如果docker发现没有应用就会将其停止
```



**进入正在运行的容器**

```shell
# 方式一。进入容器后开启一个新的终端，可以在里面操作
docker exec -it 容器id bashShell
# 方式二。进入容器正在执行的终端，不会启动新的
docker attach 容器id
```



**从容器内拷贝到主机上**

```shell
docker cp 容器id:容器内路径 主机路径
```





## 其他命令

**日志**

```shell
docker logs 容器id
	-f		# 保留打印窗口，持续刷新
	-t		# 展示时间戳
```



**容器中的进程信息**

```shell
docker top 容器id
```



**查看容器的元数据**

```shell
docker inspect 容器id
```





# 安装MySQL

```SHELL
[root@localhost /]# docker pull mysql:8.0
[root@localhost /]# docker  run -d -p 3310:3306 -v /dick_cdef/container/mysql/conf:/etc/mysql/my.conf -v /dick_cdef/container/mysql/data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=123456 --name mysql80 mysql:8.0
```







# Dockerfile

Dockerfile是用来构建docker镜像的构建文件，命令脚本。它是面向开发的，官网上的镜像往往功能不全，我们就自己来构建。

镜像是一层一层的，脚本一个一个的命令，就对应镜像里的一层一层

构建步骤：

1、编写dockerfile文件

2、docker build 构建为一个镜像

3、docker run 运行镜像

4、docker push 发布镜像



## 构建过程

1、每个保留关键字（指令）都必须是大写字母

2、执行命令从上到下

3、# 表示注释

4、每一个指令都会创建一个新的镜像层

## 命令

```shell
FROM		# 基础镜像，一切从这开始，通常是操作系统内核
MAINTAINER	# 镜像作者

# 镜像构建指令
ADD			# 往镜像里添加需要的内容，比如tomcat，tar类型文件会自动解压(网络压缩资源不会被解压)，可以访问网络资源，类似wget
WORKDIR		# 指定工作目录，之后的命令都是基于这个目录
VOLUME		# 挂载卷目录
EXPOSE		# 暴露端口
ONBUILD		# 当构建一个被继承的DockerFile时就会运行ONBUILD
COPY		# 类似ADD，将文件拷贝到镜像中
ENV			# 设置环境变量
RUN			# 镜像构建时需要运行的命令
USER		# 指定运行容器时的用户名或UID

# 容器启动时自动执行的指令
CMD			# 容器启动时要运行的命令，只有最后一个会生效，会被替代
ENTRYPOINT	# 容器启动时要运行的命令，可以追加命令
```

**镜像构建**

```SHELL
docker build [OPTIONS] PATH | URL |-

参数说明：

--build-arg=[] :设置镜像创建时的变量；

--cpu-shares :设置 cpu 使用权重；

--cpu-period :限制 CPU CFS周期；

--cpu-quota :限制 CPU CFS配额；

--cpuset-cpus :指定使用的CPU id；

--cpuset-mems :指定使用的内存 id；

--disable-content-trust :忽略校验，默认开启；

-f :指定要使用的Dockerfile路径；

--force-rm :设置镜像过程中删除中间容器；

--isolation :使用容器隔离技术；

--label=[] :设置镜像使用的元数据；

-m :设置内存最大值；

--memory-swap :设置Swap的最大值为内存+swap，"-1"表示不限swap；

--no-cache :创建镜像的过程不使用缓存；

--pull :尝试去更新镜像的新版本；

--quiet, -q :安静模式，成功后只输出镜像 ID；

--rm :设置镜像成功后删除中间容器；

--shm-size :设置/dev/shm的大小，默认值是64M；

--ulimit :Ulimit配置。

--tag, -t: 镜像的名字及标签，通常 name:tag 或者 name 格式；可以在一次构建中为一个镜像设置多个标签。

--network: 默认 default。在构建期间设置RUN指令的网络模式
```







# Docker Compose

​		Docker Compose是一个用来定义和运行复杂应用的Docker工具。一个使用Docker容器的应用，通常由多个容器组成。使用Docker Compose不再需要使用shell脚本来启动容器。

​		Compose通过一个配置文件来管理多个Docker容器，在配置文件中，所有的容器通过services来定义，然后使用docker-compose脚本来启动，停止和重启应用，和应用中的服务以及所有依赖服务的容器，非常适合组合使用多个容器进行开发的场景。

