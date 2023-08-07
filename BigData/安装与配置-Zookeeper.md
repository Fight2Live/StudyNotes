# 分布式部署

1. 解压安装
   
   ```shell
   tar -zxvf hadoop.tar.gz
   ```

2. 配置服myid
   
   1. 在`./zookeeper/`下创建文件夹`zkData`
   
   2. 在`./zookeeper/zkData/`下创建一个`myid`文件
   
   3. 在`myid`文件中输入server编号

3. 配置`zoo.cfg`
   
   1. 在`./zookeeper/conf/`目录下生成`zoo.cfg`文件
      
      ```shell
      cp zoo_sample.cfg zoo.cfg
      ```
   
   2. 修改数据存储路径，并增加配置
      
      ```properties
      datadir=/opt/module/zookeeper/zkData
      
      
      # cluster
      server.1=hadoop101:2888:3888
      server.2=hadoop102:2888:3888
      server.3=hadoop103:2888:3888
      ```
