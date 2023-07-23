# 安装

1. 下载[官方网站](http://apache.stu.edu.tw/hadoop/common)

2. 将tar.gz上传至服务器

3. 解压
   
   ```shell
   tar zxfv hadoop.tar.gz
   ```

# 配置

系统环境变量

```shell
export HADOOP_HOME=/opt/hadoop-3.2.4
export PATH=$PARH:$HADOOP_HOME/bin
export PATH=$PARH:$HADOOP_HOME/sbin
```

Hadoop配置

```shell
vim /hadoop/etc/hadoop-env.sh

# 添加java环境
export JAVA_HOME=/opt/java-11.0.19
```



## 伪分布式配置

配置核心组件core-site.xml

```xml
<configuration>
         <property>
             <name>hadoop.tmp.dir</name>
             <value>file:/root/hadoop-2.10.0/tmp</value>
             <description>Abase for other temporary directories.</description>
        </property>
        <property>
             <name>fs.defaultFS</name>
             <value>hdfs://localhost:9000</value>
        </property>
</configuration>
```

配置文件系统hdfs-site.xml

```xml
<configuration>
        <property>
             <name>dfs.replication</name>
             <value>1</value>
        </property>
        <property>
             <name>dfs.namenode.name.dir</name>
             <value>file:/root/hadoop-2.10.0/tmp/dfs/name</value>
        </property>
        <property>
             <name>dfs.datanode.data.dir</name>
             <value>file:/root/hadoop-2.10.0/tmp/dfs/data</value>
        </property>
</configuration>
```

配置yarn-site.xml

配置MapReduce文件mapred-site.xml

配置master中的worker
