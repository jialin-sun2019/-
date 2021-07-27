import os
import numpy as np
import pandas as pd

"""     针对不同的文件夹----进行关键词预览     """
# tree_dir = 'data/2017/'
# tree_dir = 'data/2018/'
# tree_dir = 'data/2019/'
# tree_dir = {'00data/data-export/2017/','00data/data-export/2018/','00data/data-export/2019/'}
tree_dir = {'../00data/data-export/2019/'}
data_all = pd.DataFrame()
for dirs in tree_dir: 
    print('*'*80)
    print('*'*26,dirs,'*'*26)
    for file in os.listdir(dirs):
        print('->->->正在读取->->->'+ os.path.join(dirs,file))
        df = pd.read_csv(dirs+file, encoding= 'gb18030')
        data_all = data_all.append(df)
print('*'*80)
print('#'*30,'ok','#'*30)
print('数据的大小为:{}'.format(data_all.shape))

# all_events = {'保姆|纵火|蓝色钱江|莫焕晶',
#               '宁晋县|宁晋|河北宁晋县',
#               '诺如|豆各庄',
#               '天嘉宜化工|响水县|盐城市响水县',
#               '别墅|秦岭|秦岭北麓',
#               '灌云县|化工企业'}
# print('*'*50,'提取事件数据','*'*50)

# for event in all_events:
#     print('->->->正在提取的事件是->->->'+ event)
#     data_event = df[df['命中关键词'].str.contains(event)]
#     print('*'*50,'提取完成','*'*50)

print('->->->正在提取的事件是->->->'+ '宁晋县|宁晋|河北宁晋县')
data_event = data_all[data_all['命中关键词'].str.contains('宁晋县|宁晋|河北宁晋县')]
print('*'*50,'提取完成','*'*50)








num_yc = len(data_event[data_event['类型(原创或转发)'] == '原创'])
num_zf = len(data_event[data_event['类型(原创或转发)'] == '转发'])
num_pl = len(data_event[data_event['类型(原创或转发)'] == '评论'])
num_all = num_yc+num_zf+num_pl

from matplotlib import pyplot as plt 
plt.rcParams['font.family'] = ['sans-serif']
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.figure(figsize=(6,9))
labels = [u'原创',u'转发',u'评论']
sizes = [num_yc/num_all,num_zf/num_all,num_pl/num_all]
explode = (0.05,0,0)
colors = ['red','yellowgreen','lightskyblue']
patches,l_text,p_text = plt.pie(sizes,explode=explode,labels=labels,colors=colors,
                                labeldistance = 1.1,autopct = '%3.1f%%',shadow = True,
                                startangle = 90,pctdistance = 0.6)

#labeldistance，文本的位置离远点有多远，1.1指1.1倍半径的位置
#autopct，圆里面的文本格式，%3.1f%%表示小数有三位，整数有一位的浮点数
#shadow，饼是否有阴影
#startangle，起始角度，0，表示从0开始逆时针转，为第一块。一般选择从90度开始比较好看
#pctdistance，百分比的text离圆心的距离
#patches, l_texts, p_texts，为了得到饼图的返回值，p_texts饼图内部文本的，l_texts饼图外label的文本

#改变文本的大小
#方法是把每一个text遍历。调用set_size方法设置它的属性
for t in l_text:
    t.set_size=(30)
for t in p_text:
    t.set_size=(20)
# 设置x，y轴刻度一致，这样饼图才能是圆的
plt.axis('equal')
plt.legend()
plt.savefig('04output/bing.png')
plt.show()
