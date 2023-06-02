# Django

# 简介

Django采用的是**MVT模型**，即模型（Model），视图（View）和模板（Template）

- M（Model）：编写程序应有的功能，负责业务对象与数据库的映射（ORM），同MVC的M

- V（View）：负责业务逻辑，并在适当时候调用Model和Template。同MVC的C

- T（Template）：负责如何把页面展示给用户。同MVC的V

# 视图Views

​        views函数的第一个参数都是请求对象，由django传递

- 作用：
  - 相应模板
  - 重定向
  - 直接相应字符串
  - 响应错误模板
  - json数据

## 1.HttpRequest

​        HttpRequest是从web服务器传递过来的请求对象，经过Django框架封装产生的

- 服务器接受到http请求后，django框架会自动根据服务器传递的环境变量创建HttpRequest对象
- view的第一个参数必然是HttpRequest
- 在django.http模块中定义了HttpRequest对象的API
- 使用HttpRequest对象的不同属性值可以获取请求中的多种信息

| 属性           | 说明                                |
| ------------ | --------------------------------- |
| content-type | 请求的mime类型                         |
| GET          | 一个类似于字典的QueryDict对象，包含get请求所带的参数  |
| POST         | 一个类似于字典的QueryDict对象，包含post请求所带的参数 |
| COOKIES      |                                   |
| SESSION      | 只有启用会话的支持时可用                      |
| PATH         | 请求的页面的完整路径，不包含域名                  |
| body         | 二进制数据，原生请求体中的参数内容                 |
| method       | 表示请求所使用的方法，如GET，POST              |
| FILES        | 一个类似于字典的QueryDict对象，包含所有上传的文件     |
| META         | 请求头详细信息                           |
| encoding     |                                   |
| scheme       | 协议                                |

## 2.HttpResponse

​        每一个view函数都必须返回的一个响应对象

| 属性           | 说明          |
| ------------ | ----------- |
| content      | 字节字符串       |
| charset      | 字符编码        |
| status_code  | http状态码     |
| content_type | 指定输出的MIME类型 |

### 调用模板返回

​        一一般用`render`函数返回，它是HttpResponse的包装，还是会返回一个HttpResponse对象

```PYTHON
def render(request, template_name, context=None, content_type=None, status=None, using=None):
    """
    Return a HttpResponse whose content is filled with the result of calling
    django.template.loader.render_to_string() with the passed arguments.
    template_name    模板名称
    context            添加到模板的字典，默认空
    content_type    MIME类型
    status            响应状态码
    """
    content = loader.render_to_string(template_name, context, request, using=using)
    return HttpResponse(content, content_type, status)
```

## 3.JsonResponse

​        Django的内置对象，一般是可以把字典、列表转换为Json返回给前端，里面的元素只能是内置类型。

​        传入`dict`后会自动转化为Json对象，如果传入其他类型的属性，带上`safe=False`即可

## 4.重定向

​        重定向到指定路由地址，参数就是目标路由

```PYTHON
return HttpResponseRedirect(url)
return redirect(url)
```

## 5.错误模板

​        Django内置了处理HTTP错误的view（在django.views.defaults下），主要包括：

- 403：permission_denied（权限拒绝）
- 404：page_not_found
- 500：server_error（这个基本是代码问题）

url匹配失败后，django会调用内置的`django.views.defaults.found()`，调用404.html进行显示。开发阶段时可以开启调试模式`DEBUG = True`，关闭后则会显示一个标准的错误页面

### 错误页面自定义

​        在templates目录下创建`error_code.html`即可

# 模型Model

## ORM

对象关系映射（Object Relational Mapping，ORM）用于实现面向对象编程语言里不同类型系统的数据之间的转换。

ORM在约为逻辑层和数据库之间充当桥梁的作用。它通过描述对象与数据库之间的映射的元数据，将程序中的对象自动持久化到数据库中。

## 定义模型

```python
from django.db import models
"""
common params

blank        默认是false，是否允许该字段为控
db_column    如果model里的字段名与表里的字段名不一致，db_column为表里的字段名
db_index    默认为false，是否以此字段建立常规索引
unique        默认false，字段值是否唯一
primary_key    主键
defalut        默认值
"""
class model_name(models.Model):
    """
    创建数据模型，即表
    field_name = field_type(opt,)


    """
    # 自增主键，若不声明，建表时也会自动生成自增主键id
    field_name1 = models.AutoField(primary_key=True)
    # 字符串CharField字段必须指明长度
    field_name2 = models.CharField(max_length=30)
    # auto_created == DEFAULT CURRENT_TIMESTAMP。
    # auto_now     == DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    field_name3 = models.DateTimeField(auto_created=Ture)

    class Meta:
        """
        元数据，模型本身的信息，与表里的字段没有关联
        """
        # django默认表名：app_model_name
        db_table = "table_name"    # 表名变为table_name
        abstract = False    # 设置为true时不会以这个模型去建表，主要用于继承
        managed = True        # 如果设置False，则迁移时不会创建或删除表
        ordering = ['field_name', '-field_name2']    # 搜索时的排序字段，默认是以主键升序排序，弱要降序则在字段名前加'-'
```

### models中的常用字段

```python
AutoField  # 如果没有指明逐渐，会产生一个自增主键
BigIntegerField  # 长整型
BinaryField  # 二进制
BooleanField  # 布尔型, 且该类型不允许null;数据库类型tinyint(1)
CharField  # 字符串，需要指明max_length
CommaSeparatedIntegerField  # 逗号分隔的整数, 需要指明max_length
DateField # 时间，对应python的datetime.date;数据库类型date
DateTimeField  # 时间, 对应python的datetime.datetime;数据库类型datetime(6)
DecimalField  # 固定精度的十进制数, 对应python的Decimal
EmailField  # 字符串, 会检查是否为合法的Email地址
FileField  # 文件对象
FloatField  # 浮点数, 需指明max_digits, decimal_places
ImageField  # 项目下的图片路径，并不是图片二进制流
IntegerField  # 整形
IPAddressField  # 点分十进制表示的IP
NullBooleanField  # 运行null的布尔型
PositiveIntegerField  # 正整数或0, 取值范围为[0 ,2147483647]
PositiveSmallIntegerField  # 正短整数或0, 取值范围为[0 ,32767]
SlugField  # 只能包含字母，数字，下划线和连字符的字符串, 通常表示url
TextField  # 文本类型
TimeField  # 时间，队友python的datetime.time
URLField  # URL字符串，默认长度200
```

### models中的常用参数

```python
null=True  # 是否可为空
blank=True  # django的Admin中添加数据时是否允许空值
primary_key=False  # 主键。对AutoField设置后，会代替原来默认的自增id列
auto_now  # 自动赋值当前时间，修改&创建
auto_now_add  # 自动赋值创建时间
max_length  # 最大长度
default  # 默认值
verbose_name  # 字段描述
name|db_column  # 数据库中的字段名称
unique=True  # 是否唯一
db_index=True  # 数据库索引
editable=True  # 在Admin中是否可编辑
error_messages=None  # 错误提示
auto_created=False  # 自动创建
help_text  # 在Admin中提示帮助信息
validators=[]  # 验证
upload-to  # 文件上传路径

max_digits  # 位数总数，整数+小数
decimal_places  # 小数长度
```

### Meta字段

```python
abstract=True  # 如果为True，则认为是抽象模型，不会实际生成数据库表
db_table  # 数据库表名
ordering  # 排序方式，接收元组或列表。默认升序，字段前加'-'表示降序
'''
ordering = ['pub_date']             # 表示按'pub_date'字段进行升序排列
ordering = ['-pub_date']            # 表示按'pub_date'字段进行降序排列
ordering = ['-pub_date', 'author']  # 表示先按'pub_date'字段进行降序排列，再按`author`字段进行升序排列。
'''
```

## 模型迁移与建表

```shell
python manage.py makemigrations
python manage.py migrate [app_name]
```

通过migrate model生成的表，字段后面没有注释字段，如要增加

1、通过修改makemigrations的文件，然后再migrate

2、

## 增删改

```python
"""
基本都是实例化对象后，因为model都是继承自Django.Model，所以实例化后可以直接save、delete等，很方便
"""
# 新增
new_user = Users(userName=random.sample('zyxwvutsrqponmlkjihgfedcba',5),
                 userAccount=random.sample('zyxwvutsrqponmlkjihgfedcba',5),
                 password='123')
new_user.save()
new_data = {'userName': random.sample('zyxwvutsrqponmlkjihgfedcba',5),
            'userAccount': random.sample('zyxwvutsrqponmlkjihgfedcba', 5),
            'password': '123'}
Users.objects.create(new_data)
# 批量创建
Users.objects.bulk_create([Users(), ])

# 修改
old_user = Users.objects.get(pk=3)
old_user.userName='update_after'
old_user.save()

# 删除
old_user = Users.objects.get(pk=3)
old_user.delete()
# 删除多条记录
users = Users.objects.filter()
users.delete()
```

## 查询

### ORM

### 过滤器

### SQL

```python
# 用raw执行sql
user = Users.objects.raw(f"select * from user_users where userName={'admin'}")
user = Users.objects.raw("select * from user_users where userName=%s", ['admin'])

# 其他执行sql
from django.db import connection
with connection.cursor() as cursor:
    cursor.execute("sql")
    columns = [col[0] for col in cursor.description]
    res = [dict(zip(columns, row)) for row in cursor.fetchall()]
    print(res)
```

## 管理器manager

​        类似mybatis，可以自定义管理器，以增强功能，同时可以统合一些重复性高的filter等

# 序列化器Serializer

序列化器的主要工作就是将前端传入后端的JSON数据转换为ORM模型映射。

# 路由URL

在url中，从上往下进行匹配，当匹配到对应的一个路由后不再往下进行匹配。

> path.name属性用来反向映射路由，前端页面中可以通过{% url 'name' %}来获取url。这样当后期如果要修改url时，只需要修改name属性就好，不用一一修改。它是路由的名称

## 动态url

```python
"""
带参数的路由
多个参数用/隔开
'url/<type:field>[/]'
"""
# 在根路由中包含子路由
path('user/', include('user.urls'))

# int
path('info/<int:id>/', views.info, name='info')

# str，如果没有指定参数类型，默认是str。不能匹配/和空字符串
path('info/<str:name>/', views.info)
path('info/<name>/<int:id>/', views.info)

# slug 匹配由字母、数字、-和_组成的字符串参数


# path 匹配任何非空字符串，包括/。如果包含多个参数，path必须要在最后一个


# re_path则是正则匹配模式串url
re_path(r'^tel/(\d{8})/$', views.tel)
```

# 快速开始

## 1、创建项目

在CMD中进入项目目录，输入

```shell
django-admin startproject porject_name
```

会创建项目文件夹

## 2、创建应用

在CMD进入上面创建的项目文件夹中，输入

```shell
python manager.py startapp app_name
```

## 3、注册应用

在`./porject_name/setting.py`文件中，将`app_name`加入`INSTALLED_APPS`中

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles', 
    'app_name'
]
```

## 4、开发应用

### 4.1、定义Model

在models.py中新建数据模型

### 4.2、数据迁移

```shell
python manager.py makemigrations  # 相当于在该app下建立 migrations目录，并记录下你所有的关于modes.py的改动
python manager.py migrate
```

### 4.3、编写View

### 4.4、设置Url

### 4.5、前端部分

### 4.6、迁移migrate

```python
python manager.py makemigrations  # 
```

# 用户认证与权限模块auth

​        auth是django提供的标准权限模块

主要功能包括：

1. create_user    创建用户
2. authenticate   验证登录
3. login                 记住登录
4. logout               退出登录
5. is_authenticated  判断用户是否登录
6. @login_required  判断用户是否登录的装饰器

## User对象

​        1、继承自Django的AbstractUser类

同时在settings中加上

```python
AUTH_USER_MODEL = 'APP_NAME.model_name'
```

# 前后端分离

会遇到两大问题，一个是会话信息的保存，一个是跨域问题

## 跨域问题

在Django的settings中进行跨域配置

## 会话保存

1、放到本地内存中

2、放进缓存数据库中