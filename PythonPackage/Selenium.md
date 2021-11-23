# Selenium笔记
Selenium是一个针对Web应用的自动化框架，它能够让使用者编写出自动化程序，可以像人一样的对浏览器进行操作，如点击按钮、输入文本等等。
它还可以像爬虫一样自动获取网站的信息。

## 一、简单的例子

​    实例化一个WebDriver对象，并指明浏览器驱动
​    wd = webdriver.Chrome('浏览器驱动路径')
​    

```python
# 使用.get（）可以打开指定网站
wd.get(url)

# 当连续操作web时，浏览器可能来不及反应，这时可以用该语句设置隐式等待，当没有立即发现目标元素时会过半秒再尝试一次
WebDriver.implicitly_wait(10)
```
## 二、选择元素 

 web界面自动化，想要操控目标元素，首先就要【选择】界面元素，或者说【定位】界面元素，就是告诉浏览器，你要操作【哪个】元素，让它找到你要操作的界面元素。所以我们必须要让浏览器先找到元素，然后才能操作元素。

### 1.开发者工具

 使用开发者窗口，鼠标定位到目标元素，获取目标元素的信息，如标签名、class、id和name等等。
    可以根据唯一的属性名去选择特定元素  
    

```python
# 根据属性选择对象，返回元素对应的WebElement对象
element = wd.find_element_by_id('id值')
element = wd.find_element_by_name('name值')
element = wd.find_element_by_class_name('class值')
element = wd.find_element_by_tag_name('tag值')
element = wd.find_element_by_link_text('链接名')
element = wd.find_elements_by_partial_link_text(link_text)
```
以上定位方法都只返回一个对象，如果找到多个则返回第一个对象，如果需要选择多个元素，则将以上方法中的element加s，如：
    
```python
element = wd.find_elements_by_class_name('class值')
```
并且element找不到元素时会抛出异常，elemenets找不到元素时则返回空列表。当调用方法的对象不同时，寻找的范围也不一样。
    
```python
WebDriver.find_element_by_xxx    # 的范围是整个网页
WebElement.find_element_by_xxx   # 的范围是对应元素的内部
```
### 2.CSS选择器

可以用css的语法来选择目标元素

```python
# 获取单个元素，如果是搜索id，则参数=#id值
find_element_by_css_selector(CSS Select参数)
# 获取一组元素
find_elements_by_css_selector(CSS Select参数)

find_element_by_css_selector('div')
# 上一条等价于下一条
find_element_by_tag_name('div')
```

### 3.XPath路径

XPath能更好的选取目标元素  

```python
#find_element_by_xpath('xpath路径')
```

## 三、各类操作     

### 1.浏览器

```python
    WebDriver.set_window_size()   # 设置浏览器的大小
    WebDriver.maximize_window()   # 最大化
    WebDriver.fullscreen_window() # 全屏显示
    WebDriver.back()              # 后退
    WebDriver.forward()           # 前进
    WebDriver.refresh()           # 刷新
    WebDriver.window_handles      # 返回当前浏览器所有窗口的句柄列表
    WebDriver.title               # 返回当前页面的标题
```

### 2.元素

```python
	WebElement.clear()	        # 清除文本
    WebElement.send_keys (value)    # 模拟按键输入
    WebElement.click()	        # 单击元素
    WebElement.submit()             # 用于提交表单
    WebElement.get_attribute(name)  # 获取元素属性值
    WebElement.is_displayed()       # 设置该元素是否用户可见
    WebElement.size                 # 返回元素的尺寸
    WebElement.text                 # 获取元素的文本
```

### 3.鼠标 

在Selenium中，模拟鼠标的方法都封装在了ActionChains类中。    
    

```python
ActionChains(driver)     # 构造ActionChains对象
click()                  # 左键单击
context_click()	         # 右击
double_click()	         # 左键双击
click_and_hold()         # 点击鼠标左键，按住不放
release(on_element=None) # 在某个元素位置松开鼠标左键
drag_and_drop(source, target)	 # 拖动某个元素至目标元素处
move_to_element(element)         # 鼠标移动到某个元素
move_by_offset(xoffset, yoffset) # 鼠标移动到距离当前位置（x,y）的地方
move_to_element_with_offset(to_element, xoffset, yoffset) #将鼠标移动到距某个元素多少距离的位置
perform()               # 执行所有 ActionChains 中存储的行为
```

### 4.键盘

键盘操作的方法基本上都是send_keys()，只是括号中的值不同而已

```python
send_keys(Keys.BACK_SPACE)    # 删除键（BackSpace）
send_keys(Keys.SPACE)         # 空格键（Space）
send_keys(Keys.TAB)           # 制表键（Tab）
send_keys(keys.ESCAPE)        # 回退键（Esc）
send_keys(Keys.ENTER)         # 回车键（Enter）
send_keys(Keys.CONTROL,'a')   # Ctrl+A
send_keys(Keys.ALT,'c')       # Alt+C
send_keys(Keys.F1)            # 键盘F1
key_down(value, element=None) # 按下某个键盘上的键
key_up(value, element=None)   # 松开某个键
```

### 5.切换

WebDriver默认指向第一个窗口页面的，而在很多时候，我们需要跳转到其他页面去完成任务。倘若新页面是覆盖原页面，那不需要跳转，只需等待页面加载完毕即可。而如果新页面在新窗口中打开，那么就需要让驱动切换窗口，然后再进行操作。  

```python
WebDriver.switch_to.window(window_handle)
```
并且WebDriver不仅默认指向第一个窗口页面，假若该页面中还存在有多个iframe，它也会指向第一个iframe，当我们搜索元素时，是无法活的其他iframe中的元素的，也需要先切换到目标iframe中再进行element_find_  

```python
WebDriver.switch_to.frame(frame_reference)
```

### 6.调用JavaScript

​    WebDriver.execute_script(js语句)