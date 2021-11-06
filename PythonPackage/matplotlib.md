# matplotlib



```python
import numpy as np
from matplotlib import pyplot as plt
import matplotlib

fonts = ['SimHei']  # 字体
plt_height = 4      # 画布上显示height行图片
plt_weigh = 3       # 画布上显示weigh列图片

base_list = [100, 200, 300, 400, 500]   # 通用数据列表

def createHistogram(cur_plt):
    """
    柱状图
    :return:
    """
    x = np.array([0, 1, 2, 3, 4])
    y = np.array(base_list)

    plt.sca(cur_plt)
    plt.bar(x, y, color='blue')
    # x轴标签，要与x一一对应
    plt.xticks(x, ['A', 'B', 'C', 'D', 'E'])
    plt.xlabel('姓名')
    plt.ylabel('得分')
    plt.title('直方图')



def createPie(cur_plt):
    """
    饼图pie() params:
    x       :(每一块)的比例，如果sum(x) > 1会使用sum(x)归一化；
    labels  :(每一块)饼图外侧显示的说明文字；
    explode :(每一块)离开中心距离；
    startangle :起始绘制角度,默认图是从x轴正方向逆时针画起,如设定=90则从y轴正方向画起；
    shadow  :在饼图下面画一个阴影。默认值：False，即不画阴影；
    labeldistance :label标记的绘制位置,相对于半径的比例，默认值为1.1, 如<1则绘制在饼图内侧；
    autopct :控制饼图内百分比设置,可以使用format字符串或者format function
            '%1.1f'指小数点前后位数(没有用空格补齐)；
    pctdistance :类似于labeldistance,指定autopct的位置刻度,默认值为0.6；
    radius  :控制饼图半径，默认值为1；
    counterclock ：指定指针方向；布尔值，可选参数，默认为：True，即逆时针。将值改为False即可改为顺时针。
    wedgeprops ：字典类型，可选参数，默认值：None。参数字典传递给wedge对象用来画一个饼图。例如：wedgeprops={'linewidth':3}设置wedge线宽为3。
    textprops ：设置标签（labels）和比例文字的格式；字典类型，可选参数，默认值为：None。传递给text对象的字典参数。
    center ：浮点类型的列表，可选参数，默认值：(0,0)。图标中心位置。
    frame ：布尔类型，可选参数，默认值：False。如果是true，绘制带有表的轴框架。
    rotatelabels ：布尔类型，可选参数，默认为：False。如果为True，旋转每个label到指定的角度。
    :return:
    """
    label_list = ['A', 'B', 'C', 'D', 'E']
    data = np.array(base_list)

    plt.sca(cur_plt)
    # autopct 格式化数值显示
    plt.pie(data, labels=label_list, autopct='%1.1f%%')
    plt.title('饼图')


def createHist(cur_plt):
    """
    直方图hist() params：
    x：指定要绘制直方图的数据；输入值，这需要一个数组或者一个序列，不需要长度相同的数组。
    bins：指定直方图条形的个数；
    range：指定直方图数据的上下界，默认包含绘图数据的最大值和最小值；
    density：布尔,可选。如果"True"，返回元组的第一个元素将会将计数标准化以形成一个概率密度，也就是说，直方图下的面积（或积分）总和为1。这是通过将计数除以数字的数量来实现的观察乘以箱子的宽度而不是除以总数数量的观察。如果叠加也是“真实”的，那么柱状图被规范化为1。(替代normed)
    weights：该参数可为每一个数据点设置权重；
    cumulative：是否需要计算累计频数或频率；
    bottom：可以为直方图的每个条形添加基准线，默认为0；
    histtype：指定直方图的类型，默认为bar，除此还有’barstacked’, ‘step’, ‘stepfilled’；
    align：设置条形边界值的对其方式，默认为mid，除此还有’left’和’right’；
    orientation：设置直方图的摆放方向，默认为垂直方向；
    rwidth：设置直方图条形宽度的百分比；
    log：是否需要对绘图数据进行log变换；
    color：设置直方图的填充色；
    label：设置直方图的标签，可通过legend展示其图例；
    stacked：当有多个数据时，是否需要将直方图呈堆叠摆放，默认水平摆放；
    normed：是否将直方图的频数转换成频率；(弃用，被density替代)
    alpha：透明度，浮点数。
    edgecolor: 直方图间的边界色
    :param cur_plt:
    :return:
    """
    x = np.random.normal(0, 1, 1000)  # 随机生成符合标准正态分布的数组
    plt.sca(cur_plt)
    plt.hist(x, color='steelblue', edgecolor = 'k', alpha=0.75)
    plt.title('直方图')







# 指定默认字体
matplotlib.rcParams['font.sans-serif'] = fonts
plt.figure()

createHistogram(plt.subplot(plt_weigh, plt_height, 1))

createPie(plt.subplot(plt_weigh, plt_height, 2))

createHist(plt.subplot(plt_weigh, plt_height, 3))

plt.show()
```

