import numpy as np
import os
import pandas as pd
from matplotlib import pyplot as plt 
tree_dir = r'04data/'


plt.rcParams['font.family'] = ['sans-serif']
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus']=False
plt.rcParams['font.size'] = 18

fig,ax1 = plt.subplots(figsize=(16, 6))
color_list = ['r','g','b','r']
counts = 0
data_all = pd.DataFrame()
num_list = list()
for file in os.listdir(tree_dir):
    print('->->->正在读取->->->'+ os.path.join(tree_dir,file))
    df = pd.read_csv(os.path.join(tree_dir,file), encoding= 'gb18030')
    file_label = file.split('.')[0].split('_')[1]
    ax1.plot(np.array(df['time']),np.array(df['num']),label = file_label,color = color_list[counts])
#     for a,b in zip(df['time'],df['num']):
#         plt.text(a, b+0.001, '%d' % b, ha='center', va= 'bottom',fontsize=9)
    counts+=1
time = df['time'].tolist()
print(time)
print('#'*30,'ok','#'*30)
plt.xlabel('时间',fontsize=16)
plt.ylabel('单日数量',fontsize=16)
xticks=list(range(0,len(time),3))
xlabels=[time[x] for x in xticks]
xticks.append(len(time))
xlabels.append('2018-05-02')
ax1.set_xticks(xticks)
ax1.set_xticklabels(xlabels, rotation=45)
for size in ax1.get_xticklabels():   #获取x轴上所有坐标，并设置字号
    size.set_fontname('Times New Roman')   
    size.set_fontsize('16')
for size in ax1.get_yticklabels():   #获取y轴上所有坐标，并设置字号
    size.set_fontname('Microsoft YaHei')    #雅黑
    size.set_fontsize('12')
font1 = {'family' : 'SimSun',
'weight' : 'normal',
'size'   : 16,
}
plt.legend(prop=font1)
plt.savefig('04output/宁晋线3条曲线.png')
plt.show()
