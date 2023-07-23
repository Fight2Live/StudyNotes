# 介绍

- Hadoop是一个由Apache基金会所开发的分布式系统基础架构  

- 主要解决海量数据的**存储**和海量数据的分析**计算**问题  

- 广义上来说，Hadoop通常是指一个更广泛的概念——Hadoop生态圈

## 优势

- **高可靠性**：Hadoop底层维护多个数据副本，所以即使Hadoop某个计算元素或存储出现故障，也不会导致数据的丢失。

- **高扩展性**：在集群间分配任务数据，可方便的扩展数以千计的节点

- **高效性**：在MapReduce的思想下，Hadoop是并行工作的，以加快处理速度

- **高容错性**：能够自动将失败的任务重新分配

## 组成

- Hadoop 1.x
  
  - MapReduce（负责计算与资源调度）
  
  - HDFS（负责数据存储）
  
  - Common（辅助工具）

- Hadoop 2.x/3.x
  
  - MapReduce（计算）
  
  - Yarn（资源调度）
  
  - HDFS（数据存储）
  
  - Common（辅助工具）

### HDFS

Hadoop Distributed File System，分布式文件系统

**架构**

主要由三部分组成

- **NameNode(nn)**：存储文件的元数据（如文件的名称、目录结构、属性等），以及每个文件的块列表和块躲在的DataNode等

- **DataNode(dn)**：用于存储数据块与其读写操作

- **Secondary NameNode(2nn)**：每隔一段时间对NameNode进行备份，类似备份用的从节点

**特性**

1. 文件在物理上是分块存储（block）的，块的大小可以通过配置参数（dfs.blocksize）来规定，默认大小在2.x版本中是128M，老版本是64M

2. 会给客户端提供一个**统一的抽象目录树**，客户端通过路径来访问文件，如`hdfs://namenode:port/dir-a/dir-b/dir-c/file.data`

3. **元数据（目录结构及文件分块信息等）** 的管理由`namenode`节点承担

4. 文件的各个block存储管理由`datanode`节点承担

5. HDFS是设计成适应一次写入，多次读出的场景，且不支持文件的修改

> namenode是HDFS集群主节点，负责维护整个HDFS的目录树，以及每一个路径所对应的block块信息
> 
> datanode是HDFS集群从节点，没一个block都可以在多个datanode上存储多个副本，副本数量也可以通过参数dfs.replication设置。
> 
> 同一个block不会存储多份在同一个datanode上。

### YARN

Yet Another Resource Negotiator，是一种资源管理器。

**架构**

主要由四部分组成

- **ResourceManager(RM)**: 整个集群资源（内存、CPU等）的管理者

- **NodeManager(NM)**: 单个节点服务器资源的管理者

- **ApplicationMaster(AM)**: 单个任务运行的管理者

- **Container**: 容器，封装了任务运行所需要的资源

### MapReduce

        它是一个分布式运算程序的编程框架，核心功能是将用户编写的业务逻辑代码和自带默认组件整合成一个完整的分布式运算程序。

**核心思想**

        它的工作模式主要分为Map阶段和Reduce阶段。

        一个Job通常将输入的数据集分割成独立的块，这些块被map任务以完全并行的方式处理。框架对map的输出进行排序，然后将其输入到Reduce中。通常作业的输入和输出都在文件系统中，框架负责调度任务、监视任务并重新执行失败的任务。

        主打一个”分而治之“。

**架构**

        该框架主要由单个主节点Master的ResourceManager，每个Slave节点NodeManager和每个应用程序的MRAppMaster组成。

- ResourceManager
  
  - **Client Service**: 应用提交、终止、输出信息（应用、队列、集群等的状
  
  - **Adaminstration Service**: 队列、节点、Client 权限管理
  
  - **ApplicationMasterService**: 注册、终止 ApplicationMaster, 获取ApplicationMaster 的资源申请或取消的请求，并将其异步地传给 Scheduler, 单线程处理
  
  - **ApplicationMaster Liveliness Monitor**: 接收 ApplicationMaster 的心跳消息，如果某个 ApplicationMaster 在一定时间内没有发送心跳，则被任务失效，其资源将会被回收，然后 ResourceManager 会重新分配一个 ApplicationMaster 运行该应用（默认尝试 2 次）
  
  - **Resource Tracker Service**: 注册节点, 接收各注册节点的心跳消息
  
  - **NodeManagers Liveliness Monitor**: 监控每个节点的心跳消息，如果长时间没有收到心跳消息，则认为该节点无效, 同时所有在该节点上的 Container 都标记成无效，也不会调度任务到该节点运行
  
  - **ApplicationManager**: 管理应用程序，记录和管理已完成的应用
  
  - **ApplicationMaster Launcher**: 一个应用提交后，负责与 NodeManager 交互，分配Container 并加载 ApplicationMaster，也负责终止或销毁
  
  - **YarnScheduler**: 资源调度分配， 有 FIFO(with Priority)，Fair，Capacity 方式
  
  - **ContainerAllocationExpirer**: 管理已分配但没有启用的 Container，超过一定时间则将其回收

- NodeManager

- MRAppMaster

**优点**

1. 易于编程，用户只关心业务逻辑与实现接口

2. 良好扩展性，可以动态增加服务器，解决计算资源不够的问题

3. 高容错性，任何一台机器挂掉，可以将任务转移到其他节点

4. 适合海量数据计算

**缺点**

1. 不擅长实时计算

2. 不擅长流式计算

3. 不擅长DAG计算



## 运行模式

### 本地模式

        数据存储在Linux本地，偶尔用于测试环境

### 伪分布式模式

        数据存储在HDFS，公司经济不允许时用这种方式

### 分布式模式

        堕胎服务器组成分布式环境。