# 安装

1. 下载[官方网站](http://apache.stu.edu.tw/hadoop/common)

2. 将tar.gz上传至服务器

3. 解压
   
   ```shell
   tar zxfv hadoop.tar.gz
   ```

# 配置

[Hadoop完全分布式配置全过程②之Ubuntu18.04.4环境下配置xsync实现文件的集群分发_又是安静写bug的一天呢的博客-CSDN博客](https://blog.csdn.net/PxxxxN/article/details/113611226)

系统环境变量

```shell
export JAVA_HOME=/opt/jdk-11.0.19
export JAVA_BIN=$JAVA_HOME/bin
export PATH=$PATH:$JAVA_BIN
export CLASSPATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar
export JAVA_HOME JAVA_BIN PATH CLASSPATH

export HADOOP_HOME=/opt/hadoop-3.2.4
export PATH=$PATH:$HADOOP_HOME/bin
export PATH=$PATH:$HADOOP_HOME/sbin
```

Hadoop配置

```shell
vim /hadoop/etc/hadoop-env.sh

# 添加java环境
export JAVA_HOME=/opt/java-11.0.19
```

## 伪分布式配置

> [各配置文件参数](https://blog.csdn.net/knidly/article/details/80268230)

这里配置三台服务器集群

| 服务               | 组件                   | Hadoop101 | Hadoop102 | Hadoop103 |
| ---------------- | -------------------- | --------- | --------- | --------- |
| HDFS             | NameNode             | √         |           |           |
|                  | DataNode             | √         | √         | √         |
|                  | SecondaryNameNode    |           |           | √         |
| Yarn             | NodeManager          | √         | √         | √         |
|                  | Resourcemanager      |           | √         |           |
| Zookeeper        | Zookeepker Server    | √         | √         | √         |
| Flume（采集日志）      | Flume                | √         | √         |           |
| Kafka            | Kafka                | √         | √         | √         |
| Flume（消费Kafka日志） | Flume                |           |           | √         |
| Flume（消费Kafka业务） | Flume                |           |           | √         |
| Hive             |                      | √         | √         | √         |
| MySQL            | MySQL                | √         |           |           |
| DataX            |                      | √         | √         | √         |
| Spark            |                      | √         | √         | √         |
| DolphinScheduler | ApiApplicationServer | √         |           |           |
|                  | AlertServer          | √         |           |           |
|                  | MasterServer         | √         | √         | √         |
|                  | WorkerServer         | √         | √         | √         |
|                  | LoggerServer         | √         |           |           |
| Superset         |                      | √         |           |           |
| Flink            |                      | √         |           |           |
| ClickHouse       |                      | √         |           |           |
| Redis            |                      | √         |           |           |
| Hbase            |                      | √         |           |           |
| 总计               |                      | 20        | 11        | 12        |

- Hadoop101
  
  - NameNode
  
  - DataNode

- Hadoop102
  
  - DataNode

- Hadoop103
  
  - Secondary NameNode
  - DataNode
1. 配置核心组件`core-site.xml`

```xml
<configuration>
         <property>
             <name>hadoop.tmp.dir</name>
             <value>/opt/module/hadoop/data</value>
             <description>Abase for other temporary directories.</description>
        </property>
        <property>
             <name>fs.defaultFS</name>
             <value>hdfs://hadoop101:8020</value>
             <description>HDFS's host and port.</description>
        </property>
        <property>
             <name>hadoop.http.staticuser.user</name>
             <value>admin</value>
             <description>static user.</description>
        </property>
        <property>
             <name>hadoop.proxyuser.admin.groups</name>
             <value>*</value>
        </property>
        <property>
             <name>hadoop.proxyuser.admin.hosts</name>
             <value>*</value>
        </property>
        <property>
             <name>hadoop.proxyuser.admin.users</name>
             <value>*</value>
        </property>
</configuration>
```

配置文件系统`hdfs-site.xml`

```xml
<configuration>
        <!-- NN Web端访问地址-->
        <property>
             <name>dfs.namenode.http-address</name>
             <value>hadoop101:9870</value>
        </property>
        <!-- 2NN Web端访问地址-->
        <property>
             <name>dfs.namenode.secondary.http-address</name>
             <value>hadoop103:9868</value>
        </property>
        <!-- 副本数-->
        <property>
             <name>dfs.replication</name>
             <value>1</value>
        </property>
</configuration>
```

配置`yarn-site.xml`

```xml
<configuration>
        <!-- 指定MR走shuffle-->
        <property>
             <name>yarn.nodemanager.aux-services</name>
             <value>mapreduce_shuffle</value>
        </property>
        <!-- 指定ResourceManager地址-->
        <property>
             <name>yarn.resourcemanager.hostname</name>
             <value>hadoop102</value>
        </property>
        <!-- 继承环境变量-->
        <property>
             <name>yarn.nodemanager.env-whitelist</name>
             <value>JAVA_HOME,HADOOP_COMMON_HOME,HADOOP_HDFS_HOME,HADOOP_CONF_DIR,CLASSPATH_PREPEND_DISTCACHE,HADOOP_YARN_HOME,HADOOP_MAPRED_HOME</value>
        </property>
        <!-- 单个容器允许分配的最大最小内存-->
        <property>
             <name>yarn.scheduler.minimum-allocation-mb</name>
             <value>512</value>
        </property>
        <property>
             <name>yarn.scheduler.maximum-allocation-mb</name>
             <value>2048</value>
        </property>
        <!-- 容器允许管理的物理内存大小-->
        <property>
             <name>yarn.scheduler.resource.memory-mb</name>
             <value>2048</value>
        </property>
        <!-- 关闭yarn对虚拟内存的限制检查-->
        <property>
             <name>yarn.nodemanager.veme-check-enabled</name>
             <value>false</value>
        </property>
        <!-- 开启日志聚集-->
        <property>
             <name>yarn.log-aggregation-enable</name>
             <value>true</value>
        </property>
        <!-- 设置日志聚集服务器地址-->
        <property>
             <name>yarn.log.server.url</name>
             <value>http://hadoop102:19888/jobhistory/logs</value>
        </property>
        <!-- 设置日志保留时间为7天-->
        <property>
             <name>yarn.log-aggregation.retain-seconds</name>
             <value>604800</value>
        </property>
</configuration>
```

配置MapReduce文件`mapred-site.xml`

```xml
<configuration>
        <!-- 指定MapReduce运行在Yarn上-->
        <property>
             <name>mapreduce.framework.name</name>
             <value>yarn</value>
        </property>
        <!-- 历史服务器-->
        <property>
             <name>mapreduce.jobhistory.address</name>
             <value>hadoop101:10020</value>
        </property>
        <!-- 历史服务器Web端-->
        <property>
             <name>mapreduce.jobhistory.webapp.address</name>
             <value>hadoop101:19888</value>
        </property>
</configuration>
```

配置master中的worker

```shell
vim $/hadoop/etc/hadoop/workers

## 新增Hadoop的服务器节点
hadoop101
hadoop102
hadoop103
```

# 启动

1. 如果是集群第一次启动，需要在主节点上格式化`NameNode`（格式化之前一定要先停止上次启动的所有`NameNode`和`DataNode`进程，在删除data和log数据）

```shell
hdfs namenode -format
```

2. 启动HDFS

```shell
start-dfs.sh
```

如果报以下错误：

```log
Starting namenodes on [hadoop]
ERROR: Attempting to operate on hdfs namenode as root
ERROR: but there is no HDFS_NAMENODE_USER defined. Aborting operation.
Starting datanodes
ERROR: Attempting to operate on hdfs datanode as root
ERROR: but there is no HDFS_DATANODE_USER defined. Aborting operation.
Starting secondary namenodes [hadoop]
ERROR: Attempting to operate on hdfs secondarynamenode as root
ERROR: but there is no HDFS_SECONDARYNAMENODE_USER defined. Aborting operation.
```

可以通过在环境变量中增加以下配置来解决：

```shell
export HDFS_NAMENODE_USER=root
export HDFS_DATANODE_USER=root
export HDFS_SECONDARYNAMENODE_USER=root
export YARN_RESOURCEMANAGER_USER=root
export YARN_NODEMANAGER_USER=root
```

3. 在配置了ResouceManeger的节点上启动YARN

```shell
start-yarn.sh
```

4. 历史服务器

```shell
mapred --daemon start historyserver
```

都完成后可以通过网站查看集群

```
# NameNode Web
http://hadoop101:9870/
# Yarn
http://hadoop102:8088/cluster
# 2NN Web
http://hadoop103:9868/
```
