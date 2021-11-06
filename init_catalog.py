import os

"""
初始化 REAMDE.md 目录
"""

# 完善中
wirtint = ['算法简记', '题目本', '描述性统计分析', 'KNN',
           '决策树', '概念与解释', 'pandas', '贝叶斯概率',
           'PowerBI', '分析模型', 'matplotlib', 'PyTorch'
           , '随机森林']

# 待完善
wait_wirte = ['常用指标', 'MySQL', 'Apriori',
              'numpy',  '回归树', '逻辑回归' ]

# 规划中
# 一想到这个列表会不断变长就头疼
wait_start = ['Hadoop', 'Hive', 'Spark', 'ETL',
              'noSQL', 'GBDT', 'Scikit-Learn', ]

root_path = './'
readme_head =\
f"""
# StudyNotes
在学习与工作中学习到的，用到的知识的一个总结，和在网上搜过的一些问题的解决方法。同时将规划知识罗列出来，提醒自己学习与补充  \n
做这个仓库的目的：  \n
1、想以后如果忘了哪部分的知识或点，就把笔记翻出来看，不用去翻书  \n
2、想让不懂这块知识的人，看了之后起码会有一个概念  \n
3、同时把以后需要学的知识先建一个文件，提醒自己需要学习与补充  \n  \n
**统计：**  \n
完善中:{len(wirtint)}  \n
待完善:{len(wait_wirte)}  \n
规划中:{len(wait_start)}  \n

# 目录:  \n

"""


def get_label(file_name):
    if file_name in wirtint:
        return '（…… 完善中）'
    elif file_name in wait_wirte:
        return '（！ 待完善）'
    elif file_name in wait_start:
        return '（× 规划中）'
    else:
        return ''

def recursion_init_path(path, hight, file_text):
    """
    递归添加文件路径
    :param path:        当前的文件夹
    :param hight:       深度，用于拼接路径
    :param file_text:   README文件内容
    :return:
    """
    print(f'当前根文件夹：{path}, 内容有：{os.listdir(path)}')
    # 当前文件夹下的子文件夹列表
    cur_sub_dir_list = []
    # 子文件夹对应的文本内容
    cur_sub_dir_text_map = {}
    for cur_path in os.listdir(path):
        print(f'当前目标{cur_path}')
        if '.' == cur_path[0]:
            print(f'结构文件{cur_path}，跳过')
            continue
        if '.' in cur_path:
            # 文件
            if '/' == path[-1]:
                sub_path = cur_path
            else :
                sub_path = '/' + cur_path
            file_name = cur_path.split(".")[0]
            cur_link = f'[{file_name}]({path + sub_path})'
            label = get_label(file_name)
            file_text = file_text  + '  \n' + '  ' * hight + '- ' + cur_link + ' '+ label + '  \n'
        else :
            # 子文件夹
            if '/' == path[-1]:
                sub_path = path + cur_path
            else :
                sub_path = path + '/' + cur_path

            cur_sub_dir_list.append(sub_path)
            cur_str = '\n' + '  ' * hight + '- ' + cur_path
            cur_sub_dir_text_map[sub_path] = cur_str


    # 对子文件夹进行遍历
    for sub_dir in cur_sub_dir_list:
        file_text = file_text + cur_sub_dir_text_map[sub_dir]
        file_text = recursion_init_path(sub_dir, hight + 1, file_text)

    return file_text

readme_text = recursion_init_path(root_path, 0, '')
print(readme_text)
readme = readme_head + readme_text

readme_file = open('./README.md', 'w+')
readme_file.write(readme)
readme_file.close()

