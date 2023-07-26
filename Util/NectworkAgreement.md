# TCP/IP协议

[TCP/IP协议常见面试题_tcp/ip面试题](https://blog.csdn.net/qq_41696018/article/details/124249818)

[太厉害了，终于有人能把TCP/IP 协议讲的明明白白了](https://blog.csdn.net/wuzhiwei549/article/details/105965493)

TCP/IP 中有两个具有代表性的传输层协议，分别是 TCP 和 UDP。

- TCP 是面向连接的、可靠的流协议。流就是指不间断的数据结构，当应用程序采用 TCP 发送消息时，虽然可以保证发送的顺序，但还是犹如没有任何间隔的数据流发送给接收端。TCP 为提供可靠性传输，实行“顺序控制”或“重发控制”机制。此外还具备“流控制（流量控制）”、“拥塞控制”、提高网络利用率等众多功能。
- UDP 是面向报文的，是不具有可靠性的数据报协议。细微的处理它会交给上层的应用去完成。在 UDP 的情况下，虽然可以确保发送消息的大小，却不能保证消息一定会到达。因此，应用有时会根据自己的需要进行重发处理。
- TCP 和 UDP 的优缺点无法简单地、绝对地去做比较：TCP 用于在传输层有必要实现可靠传输的情况；而在一方面，UDP 主要用于那些对高速传输和实时性有较高要求的通信或广播通信。TCP 和 UDP 应该根据应用的目的按需使用。

#### UDP

- UDP 不提供复杂的控制机制，利用 IP 提供面向无连接的通信服务。
- 并且它是将应用程序发来的数据在收到的那一刻，立即按照原样发送到网络上的一种机制。即使是出现网络拥堵的情况，UDP 也无法进行流量控制等避免网络拥塞行为。
- 此外，传输途中出现丢包，UDP 也不负责重发。
- 甚至当包的到达顺序出现乱序时也没有纠正的功能。
- 如果需要以上的细节控制，不得不交由采用 UDP 的应用程序去处理。
- UDP 常用于一下几个方面：1.包总量较少的通信（DNS、SNMP等）；2.视频、音频等多媒体通信（即时通信）；3.限定于 LAN 等特定网络中的应用通信；4.广播通信（广播、多播）。

#### TCP

- TCP 与 UDP 的区别相当大。它充分地实现了数据传输时各种控制功能，可以进行丢包时的重发控制，还可以对次序乱掉的分包进行顺序控制。而这些在 UDP 中都没有。
- 此外，TCP 作为一种面向有连接的协议，只有在确认通信对端存在时才会发送数据，从而可以控制通信流量的浪费。
- 根据 TCP 的这些机制，在 IP 这种无连接的网络上也能够实现高可靠性的通信（ 主要通过检验和、序列号、确认应答、重发控制、连接管理以及窗口控制等机制实现）。

##### 三次握手

当TCP开始连接时，会进行“三次握手”的通信，即客户端和服务器共发送三个包来确认链接的建立。

1. 客户端将标志位SYN置为1，随机产生一个`SEQ`值，然后将数据包A发给服务器，客户端进入`SYN_SENT` 状态，等待服务器确认

2. 服务器接收到数据包A后，将标志位`SYN`和`ACK`置为1，并产生新的`SEQ`值，将新的数据包B发送给客户端

3. 客户端接收到数据包B，确认并检查标志位后，新打包一个数据包C发送给服务器，服务器确认C中的字段值正确后，即建立连接

##### 四次挥手

        当一方发起中断连接请求后，发起方即停止发送，但依然处于数据接收状态，当被动方当前的数据发送完成后，也会转入停止发送状态，最后接收到发起方发送中断确认的信号后，即断开连接

- 中断连接端可以是客户端，也可以是服务器端。也就一方主动关闭，另一方被动关闭的情况。
1. 客户端发送数据包A`FIN=M`，并关闭客户端到服务器端的数据发送，客户端进入`FIN_WAIT_1`状态。

2. 服务器接收到数据包A后，会先发送数据包B`ACK=M+1`，客户端接收B后进入`FIN_WAIT_2`状态，继续等待服务器端的信息

3. 当服务器确定数据都发送完成时，向客户端发送数据包C`FIN=N`，并进入`LAST_ACK`状态，准备关闭连接

4. 客户端接收到数据包C后，进入`TIME_WAIT`状态，并最后向服务器发送数据包D`ACK=N+1`，如果服务器端没有收到D可以进行重传。服务器接收D后，连接即断开。又或者当客户端等待一定时间没有收到回复后，也证明服务器端已关闭，即断开连接。
- 实际中还存在两把同时发起主动关闭的情况

三次握手与四次挥手

### IP

#### 分类

IP地址分为四个级别，分别为A,B,C,D四类，根据IP地址从第1位到第4位的bit列对其网络标识和主机标识进行区分

#### 子网掩码

        通过子网掩码，将原网络地址细分出比A,B,C类更小粒度的网络，实际上就是将原地址的主机地址部分用作子网地址，可以将原网络分为多个物理网络的机制。

        用32位的二进制表示，它对应IP地址网络标识部分的位全为1，对应主机标识部分的全为0

# HTTP/HTTPs协议

[面试必考HTTP协议面试题（含答案）*http面试题*](https://blog.csdn.net/weixin_45819386/article/details/123219420)

[HTTP 协议完全解析](https://zhuanlan.zhihu.com/p/158044137)

https://zhuanlan.zhihu.com/p/37436528

# DNS协议

[DNS图解（秒懂 + 史上最全）_40岁资深老架构师尼恩的博客-CSDN博客](https://blog.csdn.net/crazymakercircle/article/details/120521694)

### 原理

![img](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9RQjZHNFpvRTE4NGljd1J3OG9LaWNVaEhCUlI5UXp6c29xY2liR1F0WmZLaWFpY2dESEk5Rmlhc3p4VkFoaWF4d0ppY2JBZXFVOU9sckNsOG1yaWE5UUV5eVI2RDVUUS82NDA)

**基础结构部分：**

事务 ID：DNS 报文的 ID 标识。对于请求报文和其对应的应答报文，该字段的值是相同的。通过它可以区分 DNS 应答报文是对哪个请求进行响应的。
标志：DNS 报文中的标志字段。
问题计数：DNS 查询请求的数目。
回答资源记录数：DNS 响应的数目。
权威名称服务器计数：权威名称服务器的数目。
附加资源记录数：额外的记录数目（权威名称服务器对应 IP 地址的数目）。

**问题部分：**

查询问题区域：

- 查询名：一般为要查询的域名，有时也会是 IP 地址，用于反向查询。
- 查询类型：DNS 查询请求的资源类型。通常查询类型为 A 类型，表示由域名获取对应的 IP 地址。
- 查询类：地址类型，通常为互联网地址，值为 1。

**资源记录部分：**

- 回答问题区域字段、
- 权威名称服务器区域字段、
- 附加信息区域字段。

### 解析过程

1. 检查浏览器缓存中是否存在域名对应的IP

2. 浏览器缓存中不存在时，会从本机的hosts文件中查询是否存在
   
   - 在`Windows`系统中，`hosts`文件位置在`C:\Windows\System32\drivers\etc\hosts`。
   
   - 在`Linux`或者`Mac`系统中，`hosts`文件在`/etc/hosts` 文件中。

3. 以上两步都找不到时，会向本地域名系统`LDNS` 请求查找。它总结起来为三点：
   
   - 从“根域名服务器”查到“一级域名服务器”的NS记录和A记录
   
   - 从“一级域名服务器”查到“二级域名服务器”的NS记录和A记录
   
   - 从“二级域名服务器”查出“主机名”的IP地址

### 查询类型

        从客户端触发，完整的DNS查找过程中会有三种类型的查询。通过组合使用这些查询，优化的DNS解析过程可缩短传输距离

- 递归查询

本机向LDNS发出一次查询请求，若LDNS无法解析，LDNS会向其他域名服务器查询，知道得到最终的IP地址返回

- 迭代查询

本地域名服务器向根域名服务器查询，根域名服务器告诉它下一步去哪查，

- 非递归查询

### DNS劫持

#### 如何确认DNS劫持

查看路由器DNS配置是否被篡改。  
可以使用一些全网拨测的工具确认DNS劫持和其影响范围。在此隆重介绍一下，阿里的DNS域名检测工具于国庆后已经正式上线，地址是：[阿里云网站运维检测平台](https://zijian.aliyun.com/#/domainDetect)

#### 劫持防范

• 安装杀毒软件，防御木马病毒和恶意软件；定期修改路由器管理账号密码和更新固件。
• 选择安全技术实力过硬的域名注册商，并且给自己的域名权威数据上锁，防止域名权威数据被篡改。
• 选择支持DNSSEC的域名解析服务商，并且给自己的域名实施DNSSEC。DNSSEC能够保证递归DNS服务器和权威DNS服务器之间的通信不被篡改。阿里云DNS作为一家专业的DNS解析服务厂商，一直在不断完善打磨产品功能，DNSSEC功能已经在开发中，不日就会上线发布。
• 在客户端和递归DNS服务器通信的最后一英里使用DNS加密技术，如DNS-over-TLS，DNS-over-HTTPS等。

### DNS隧道

[一文读懂DNS隧道](https://blog.csdn.net/FreeBuf_/article/details/128149766)

        DNS隧道，是隧道技术中的一种。当我们的HTTP、HTTPS这样的上层协议、正反向端口转发都失败的时候，可以尝试使用DNS隧道。DNS隧道很难防范，因为平时的业务也好，使用也罢，难免会用到DNS协议进行解析，所以防火墙大多对DNS的流量是放行状态。这时候，如果我们在不出网机器构造一个恶意的域名（***.xxx.ga），本地的DNS服务器无法给出回答时，就会以迭代查询的方式通过互联网定位到所查询域的权威DNS服务器。最后，这条DNS请求会落到我们提前搭建好的恶意DNS服务器上，于是乎，我们的不出网主机就和恶意DNS服务器交流上了。