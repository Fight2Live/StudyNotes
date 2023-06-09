# Kafka

# 一、概述

## 1.定义

​        Kafka是一个分布式的基于发布/订阅模式的消息队列，主要应用于大数据实时处理领域。

## 2、消息队列

​    具体含义参考 [消息队列是什么]:(https://www.zhihu.com/question/54152397?sort=created)

### 好处

​            消息队列最大的特点主要是三点，**异步，解耦和削峰**

#### 1、解耦

​        允许独立的扩展或修改两边的处理过程，只要确保它们遵守同样的接口约束

#### 2、可恢复性

​        系统的一部分组件失效时，不会影响到整个系统。消息队列降低了进程间的耦合度，所以即使一个处理消息的进程挂掉。

#### 3、缓冲

​        有助于控制和优化数据流经过系统的速度，解决生产消息和消费消息的处理速度不一致的情况

#### 4、灵活性

​        在访问量在剧增的情况下，应用仍然需要继续发挥作用，但是这样的突发流量并不常见。如果为以能处理这类峰值的访问标准来投入资源随时待命无疑是巨大的浪费。使用消息队列能够使关键组件顶住突发的访问压力，而不会因为突发的超负荷的请求而崩溃。

#### 5、异步通信

### 模式

#### 1、点对点模式（一对一）

消费者主动拉取数据，消息收到后清楚消息

#### 2、发布/订阅模式（一对多）

消费者消费数据之后不会清除消息。生产者将消息发布到topic中，同时有多个消费者订阅消费消息。

​        1、消费者主动拉取消息（Kafka是这种）

​        2、将消息主动推消息给消费者

## 3、名词解释

- `broker` : Kafka服务器，负责消息存储和转发

- `topic`：消息类别、主题，Kafka按照topic来分类存储消息

- `partition`：topic的分区，为了实现扩展性，一个topic可以分为多个partition，每个partition是一个分区有序的队列，但不保证全局有序

- `replica`：副本，一个topic的每个partition有若干个副本，一个leader和多个follower

- `offset`：消息在partition上的偏移量，也是表示该消息的唯一序号

- `producer`：生产者

- `consumer`：消费者

- `zookeeper`：保存着集群broker、topic、partition等元数据；负责broker故障发现，partition leader选举，负载均衡等功能

- `ISR(InSyncRepli)`：速率和leader相差低于10秒的follower集合

- `OSR(OutSyncRepli)`：与leader速率相差大于10秒的followe集合

- `AR(AllRepli)`：所有分区的follower

# 二、架构

# 选举策略

1、 OfflinePartition Leader选举：每当有分区上线时，就需要执行Leader选举。所谓的分区上线，可能是创建了新分区，也可能是之前的下线分区重新上线。这是最常见的分区Leader选举场景。

2、 ReassignPartition Leader选举：当你手动运行Kafka-reassign-partitions命令，或者是调用Admin的alterPartitionReassignments方法执行分区副本重分配时，可能触发此类选举。假设原来的AR是[1，2，3]，Leader是1，当执行副本重分配后，副本集合AR被设置成[4，5，6]，显然，Leader必须要变更，此时会发生Reassign Partition Leader选举。

3、 PreferredReplicaPartition Leader选举：当你手动运行Kafka-preferred-replica-election命令，或自动触发了Preferred Leader选举时，该类策略被激活。所谓的Preferred Leader，指的是AR中的第一个副本。比如AR是[3，2，1]，那么，Preferred Leader就是3。

4、 ControlledShutdownPartition Leader选举：当Broker正常关闭时，该Broker上的所有Leader副本都会下线，因此，需要为受影响的分区执行相应的Leader选举。

这4类选举策略的大致思想是类似的，即从AR中挑选首个在ISR中的副本，作为新Leader。