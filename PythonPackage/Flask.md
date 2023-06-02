# 简介

        Flask是一个非常小的，轻量化的web框架，只提供了一个稳健的核心，其他功能全部通过扩展实现的。

# 创建应用

```python
from flask import Flask

app = (__name__)

@app.route('/')
def hallo_word():
    return 'Hello Flask!'

if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')  # 设置debug=True是为了让代码修改实时生效，而不用每次重启加载
```

## 初始化简介

```python
# Flask实例的源码：
class Flask(_PackageBoundObject):
    def __init_(self, import_name,  # 指定应用的名字和工程目录，默认为__name__
                static_path=None,  #  是静态文件存放的路径，会赋值给static_url_path参数
                static_url_path=None,  # 设置静态文件路由的前缀，默认为“/static”
                static_folder='static', # 静态文件的存放目录， 默认值为"static"
                template_folder='templates', # 模板文件的存放目录，默认值为"templates"
                instance_path=None, # 设置配置文件的路径，在instance_relative_config=True情况下生效
                instance_relative_config=False # 设置为True表示配置文件相对于实例路径而不是根路径
                root_path=None) # #  应用程序的根路径
```

# 配置参数

        flask实例化后会加载默认的配置参数，我们也可以手动设置参数，常用的有：

```properties
DEBUG:是否启用debug模式，默认false。
TESTING :启用/禁止测试模式
SECRET_KEY :密钥,在启用session等很重要
SESSION_COOKIE_NAME :设置保存的session在 cookie 的名称
SESSION_COOKIE_DOMAIN：设置会话的域，默认是当前的服务器，因为Session是一个全局的变量，可能应用在多个app中；设置这个参数必须设置SERVER_NAME,否则报错
PERMANENT_SESSION_LIFETIME：session失效时间，作为一个 datetime.timedelta 对象，也可以用秒表示；
LOGGER_NAME:日志记录器的名称，默认__name__;
SERVER_NAME:服务器的名称以及端口，需要它为了支持子域名 (如: 'myapp.dev:5000')
MAX_CONTENT_LENGTH:设置一个请求所允许的最大的上传数据量，单位字节；
SEND_FILE_MAX_AGE_DEFAULT:  设置调用send_file发送文件的缓存时间；
TRAP_HTTP_EXCEPTIONS:如果这个值被设置为 True ， Flask 不会执行 HTTP 异常的错误处理， 而是像对待其它异常一样，通过异常栈让它冒泡;
PREFERRED_URL_SCHEME:设置URL 模式用于 URL 生成。如果没有设置 URL 模式，默认将为 http 。
JSON_AS_ASCII：默认情况下 Flask 序列化对象成 ascii 编码的 JSON。 如果不对该配置项就行设置的话，Flask 将不会编码成 ASCII 保持字符串原样，并且返回 unicode 字符串。jsonfiy 会自动按照 utf-8 进行编码并且传输。
JSON_SORT_KEYS：默认情况下 Flask 将会依键值顺序的方式序列化 JSON。 这样做是为了确保字典哈希种子的独立性，返回值将会一致不会造成 额外的 HTTP 缓存。通过改变这个变量可以重载默认行为。 这是不推荐也许会带来缓存消耗的性能问题。
JSONIFY_PRETTYPRINT_REGULAR：如果设置成 True (默认下)，jsonify 响应对象将会完美地打印。
```

### 设置参数

```python
# 通过文件加载
app.config.from_pyfile("./config.cfg") # 指定参数的路径，内容按行书写,配置文件放置在与app的同目录下
def from_pyfile(self, filename, silent=False):
    filename = os.path.join(self.root_path, filename)
    pass

# 通过类设置
class Config(object):
    DEBUG = True
app.config.from_object(Config)


# 通过json
# config.json
{
    'DEBUG':True
}

app.config.from_json('config.json')

# 直接操作app对象进行设置
app.config['DEBUG'] = True
# 或者
app.config.update({'DEBUG':True,})
```

### 获取参数

```python
app.config.get("DEBUG")
或者
current_app.config.get("DEBUG")
```

# 路由

        通过Flask的`app.route`装饰器来设置，类似Spring

```python
@app.route('/', methods=['POST', 'GET'])
def index():
    return 'Index Page'


@app.route('/hello')
def hello():
    return 'Hello world'
```

## 路径变量

        路径变量的语法是`/path/<converter:varname>`。在路径变量前还可以使用可选的转换器，有以下几种转换器。

| 转换器    | 作用                      |
| ------ | ----------------------- |
| string | 默认选项，接受除了斜杠之外的字符串       |
| int    | 接受整数                    |
| float  | 接受浮点数                   |
| path   | 和string类似，不过可以接受带斜杠的字符串 |
| any    | 匹配任何一种转换器               |
| uuid   | 接受UUID字符串               |

```python
# 官方例子
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):   # 函数参数中接收传递的参数
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id
```

## 查看URL

```python
@app.route('/loginto')
def login():
    print(url_for('login')) # 会打印出网址中主机名后的部分
    return 'Hello world!'
```

## 参数获取

```python
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        print(request.form['userid'])  # 获取post穿过来的参数
        dict = request.form.to_dict()  # 将请求参数解析成字典
        print(dict['userid'])
        return 'POST'
    else:
        print(request.args['userid'])   # 获取get传过来的参数
        dict = request.args.to_dict()  # 将请求参数解析成字典
        print(dict['userid'])
        return 'GET'
```

## 获取上传文件

        利用Flask也可以方便的获取表单中上传的文件，只需要利用 request 的files属性即可，这也是一个字典，包含了被上传的文件。如果想获取上传的文件名，可以使用filename属性，不过需要注意这个属性可以被客户端更改，所以并不可靠。更好的办法是利用werkzeug提供的secure_filename方法来获取安全的文件名

```python
from flask import request
from werkzeug.utils import secure_filename

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/' + secure_filename(f.filename))
```
