# 介绍

[Spring常见面试题总结（超详细回答）](https://blog.csdn.net/a745233700/article/details/80959716)

        Spring是一个轻量级的IoC和AOP的容器框架，是为Java应用程序提供基础性服务的一套框架，目的是用于简化企业应用程序的开发，它使得开发者只需要关心业务需求。主要包含以下七个模块：

- Spring Context：提供框架式的Bean访问方式，以及企业及功能（JNDI，定时任务等）

- Core：核心类库，所有功能都依赖于该库，提供IOC和DI服务

- AOP

- Web：提供了基本的面向Web的综合特性，提供对常见框架如Struts2的支持，Spring能够管理这些框架，将Spring的资源注入给框架，也能在这些框架的前后插入拦截器

- MVC：提供面向Web的MVC实现

- DAO：对JDBC的抽象封装，简化了数据访问异常的处理，并能统一管理JDBC事务

- ORM：对现有的ORM框架支持

## 优点

1. 低侵入式设计，代码的污染低

2. DI机制将对象之间的依赖关系交由框架处理，减低组件的耦合性

3. 提供了AOP技术，支持将一些通用的任务（如安全、事务、日志、权限等）进行集中式的管理，从而提供更好的复用。

4. 对主流的应用框架提供了集成支持

## IoC

        Inversion of Control，控制反转，指将对象的控制权转移给Spring框架，由框架来负责控制对象的生命周期（如创建、销毁）和对象间的依赖关系。就像一个比较高级的工厂模式。

        最直观的表达就是，以前创建对象的时机和主动权都是由程序自己把控的，如果在一个对象中使用另外的对象，就必须通过new来创建依赖对象，使用完后还需要销毁（比如Connection），对象事中回合其他接口或类耦合。而IoC则是由专门的容器来帮忙创建对象，将所有的类在框架中等级，当需要某个对象时，不再需要主动去new了，只需要告诉容器，将会在系统运行到适当的时机，把需要的对象主动给过来。

        对于某个具体的对象而言，以前是由自己控制它所引用对象的生命周期，而在IoC中，所有的对象都被框架控制，控制对象生命周期的不再是引用它的对象，而是Spring容器，由Spring容器帮我们创建、查找以及注入依赖对象，而引用对象只是被动的接受依赖对象，所以这叫控制反转。

### DI

        IoC的一个重点就是程序运行时，动态的向某个对象提供它所需要的其他对象，这一点就是通过DI（Dependency Injection，依赖注入）来实现的，即应用程序在运行时依赖IoC容器来动态注入对象所需要的外部依赖。而 Spring 的 DI 具体就是通过反射实现注入的，反射允许程序在运行的时候动态的生成对象、执行对象的方法、改变对象的属性

### 原理

Spring 的 IoC 的实现原理就是工厂模式加反射机制

[Spring的Bean加载流程_spring bean加载过程_张维鹏的博客-CSDN博客](https://blog.csdn.net/a745233700/article/details/113840727)

## AOP

        一般称为面向切面，作为面向对象的一种补充。用于将那些与业务无关，但却对多个对象产生影响的公共行为和逻辑，抽取并封装为一个可重用的模块，这个模块称为“切面”（Aspect）。

> 类比Python的装饰器，或Spring的注解。不过AOP是在切面上用注解的方式插入到哪，而装饰器与注解是主动将目标方法添加上额外功能

- 减少重复代码

- 降低模块间的耦合度

- 提高系统的可维护性

- 可用于权限认证、日志、事务处理等

### 相关概念

- **连接点 Join point**：指程序运行过程中所执行的方法

- **切面 Aspect**：被抽取出来的公共模块，可以用来横切多个对象

- **切点 Pointcut**：用于定义要对那些Join point进行拦截

- **通知 Advice**：要再连接点上执行的动作，即增强逻辑。包括Around、Before、After、After returning、After throwing

- **目标对象 Target**：包含连接点的对象，也被称作通知对象。

- **织入 Weaving**：通过动态代理，在目标对象的方法中执行增强逻辑的过程

- **引入 Introduction**：添加额外的方法或字段到被通知的类。Spring允许引入新的接口到任何被代理的对象

![](https://img-blog.csdnimg.cn/2020120700443256.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2E3NDUyMzM3MDA=,size_16,color_FFFFFF,t_70)

# 启动流程

[Spring容器的启动流程_spring启动过程_张维鹏的博客-CSDN博客](https://blog.csdn.net/a745233700/article/details/113761271)

1. 初始化Spring容器，注册内置的BeanPostProcessor的BeanDefinition到容器中：
   
   1. 实例化BeanFactory【DefaultListableBeanFactory】工程，用于生成Bean对象
   
   2. 实例化BeanDefinitionReader注解配置读取器，用于对特定注解的类进行读取转化成BeanDefinition对象。（BeanDefinition 是 Spring 中极其重要的一个概念，它存储了 bean 对象的所有特征信息，如是否单例，是否懒加载，factoryBeanName 等）
   
   3. 实例化ClassPathBeanDefinitionScanner路径扫描器，用于对指定的包目录进行扫描并查找bean对象

2. 将SpringConfig配置类注册到容器中

3. 调用`refresh()`方法刷新容器
   
   1. prepareRefresh()刷新前的预处理
   
   2. obtainFreshBeanFactory()：获取在容器初始化时创建的BeanFactory
   
   3. prepareBeanFactory(beanFactory)：BeanFactory的预处理工作，向容器中添加一些组件
   
   4. postProcessBeanFactory(beanFactory)：子类重写该方法，可以实现在BeanFactory创建并预处理完成以后做进一步的设置
   
   5. invokeBeanFactoryPostProcessors(beanFactory)：在BeanFactory标准初始化之后执行BeanFactoryPostProcessor的方法，即BeanFactory的后置处理器
   
   6. registerBeanPostProcessors(beanFactory)：向容器中注册Bean的后置处理器BeanPostProcessor，它的主要作用是干预Spring初始化bean的流程，从而完成代理、自动注入、循环依赖等功能
   
   7. initMessageSource()：初始化MessageSource组件，主要用于做国际化功能，消息绑定与消息解析：
   
   8. initApplicationEventMulticaster()：初始化事件派发器，在注册监听器时会用到：
   
   9. onRefresh()：留给子容器、子类重写这个方法，在容器刷新的时候可以自定义逻辑
   
   10. registerListeners()：注册监听器：将容器中所有的ApplicationListener注册到事件派发器中，并派发之前步骤产生的事件：
   
   11. finishBeanFactoryInitialization(beanFactory)：初始化所有剩下的单实例bean，核心方法是preInstantiateSingletons()，会调用getBean()方法创建对像
   
   12. finishRefresh()：发布BeanFactory容器刷新完成事件：

# 生命周期

只有四个阶段

- 实例化 Instantiation

- 属性赋值 Populate

- 初始化 Initialization

- 销毁 Destruction

# 设计模式

Spring框架用到的设计模式主要有以下：

1. 工厂模式，通过BeanFactory和ApplicationContext来创建对象

2. 单例模式，Bean默认为单例模式

3. 策略模式，如Resource的实现类，针对不同的资源文件，实现不同方式的资源获取策略

4. 代理模式，AOP功能用到了JDK的动态代理和CGLIB字节码生成技术

5. 模板方法，可以将相同代码放在父类中，而将不同的代码放入不同的子类中，用来解决代码重复的问题

6. 适配器模式，AOP的增强或通知使用了适配器模式，MVC有

7. 观察者模式：Spring事件驱动模型就是观察者模式的一个经典应用

8. 桥接模式，可以根据客户的需求能够动态切换不同的数据源。
