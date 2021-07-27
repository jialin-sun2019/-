import os
import numpy as np
import pandas as pd
from datetime import *
from matplotlib import pyplot as plt

"""************ 1、针对不同的文件夹，读取舆情数据！************"""
def read_data(tree_dir):
    data_all = pd.DataFrame()
    for dirs in tree_dir:
        print('*' * 26, dirs, '*' * 26)
        for file in os.listdir(dirs):
            print('->->->正在读取->->->' + os.path.join(dirs, file))
            df = pd.read_csv(dirs + file, encoding='gb18030')
            data_all = data_all.append(df)
    print('数据的大小为:{0}'.format(data_all.shape))
    print('#' * 30, 'data read ok', '#' * 30)
    return data_all

"""************ 2、 开始提取特定事件！************"""
# @function--input  '宁晋','保姆','豆各庄','响水县','别墅','灌云县'
def get_event(event, data_all):
    print('**********开始提取{0}事件'.format(event))
    if (event == '宁晋'):
        print('->->->正在提取的事件是->->->' + '宁晋县|宁晋|河北宁晋县')
        data_event = data_all[data_all['命中关键词'].str.contains('宁晋县|宁晋|河北宁晋县')]
        print('**********read data for {0} ok'.format(event))

        data_event['发表时间'] = pd.to_datetime(data_event['发表时间'], format='%Y-%m-%d %H:%M')
        data_event['发表时间'] = data_event['发表时间'].apply(lambda x: datetime.strftime(x, '%Y-%m-%d %H:%M'))
        """宁晋污染"""
        start_time = datetime(2018, 3, 29, 14, 0)  # 最初的开始时间
        now_time = datetime(2018, 3, 30, 0, 0)  # 现在的时间
        end_time = datetime(2018, 4, 30, 20, 0)  # 最后的截止时间
        last_time = start_time
        out_all_time = dict()  # 存储所有时间节点的字典
        out_all_time[start_time.strftime('%Y-%m-%d')] = 0
        while (now_time < end_time):  # 当前时间小于最后的截止时间
            data_shape = data_event[data_event["发表时间"].str.startswith(last_time.strftime('%Y-%m-%d'))].shape
            out_all_time[now_time.strftime('%Y-%m-%d')] = data_shape[0]
            last_time = now_time
            now_time = now_time + timedelta(days=1)
        return out_all_time
    elif (event == '保姆'):
        print('->->->正在提取的事件是->->->' + '保姆|纵火|蓝色钱江|莫焕晶')
        data_event = data_all[data_all['命中关键词'].str.contains('保姆|纵火|蓝色钱江|莫焕晶')]
        print('**********read data for {0} ok'.format(event))
        data_event['发表时间'] = pd.to_datetime(data_event['发表时间'], format='%Y-%m-%d %H:%M')
        data_event['发表时间'] = data_event['发表时间'].apply(lambda x: datetime.strftime(x, '%Y-%m-%d %H:%M'))
        """保姆事件"""
        start_time = datetime(2017, 6, 22, 14, 0)  # 最初的开始时间
        now_time = datetime(2017, 6, 23, 0, 0)  # 现在的时间
        end_time = datetime(2019, 9, 29, 0, 0)  # 最后的截止时间
        last_time = start_time
        out_all_time = dict()  # 存储所有时间节点的字典
        out_all_time[start_time.strftime('%Y-%m-%d')] = 0
        while (now_time < end_time):  # 当前时间小于最后的截止时间
            data_shape = data_event[data_event["发表时间"].str.startswith(last_time.strftime('%Y-%m-%d'))].shape
            out_all_time[now_time.strftime('%Y-%m-%d')] = data_shape[0]
            last_time = now_time
            now_time = now_time + timedelta(days=1)
        return out_all_time
    elif (event == '豆各庄'):
        print('->->->正在提取的事件是->->->' + '诺如|豆各庄')
        data_event = data_all[data_all['命中关键词'].str.contains('诺如|豆各庄')]
        print('**********read data for {0} ok'.format(event))
        data_event['发表时间'] = pd.to_datetime(data_event['发表时间'], format='%Y-%m-%d %H:%M')
        data_event['发表时间'] = data_event['发表时间'].apply(lambda x: datetime.strftime(x, '%Y-%m-%d %H:%M'))
        """诺如，豆各庄水污染"""
        start_time = datetime(2019, 7, 13, 11, 0)  # 最初的开始时间
        now_time = datetime(2019, 7, 14, 0, 0)  # 现在的时间
        end_time = datetime(2019, 7, 30, 0, 0)  # 最后的截止时间
        last_time = start_time
        out_all_time = dict()  # 存储所有时间节点的字典
        out_all_time[start_time.strftime('%Y-%m-%d')] = 0
        while (now_time < end_time):  # 当前时间小于最后的截止时间
            data_shape = data_event[data_event["发表时间"].str.startswith(last_time.strftime('%Y-%m-%d'))].shape
            out_all_time[now_time.strftime('%Y-%m-%d')] = data_shape[0]
            last_time = now_time
            now_time = now_time + timedelta(days=1)
        return out_all_time
    elif (event == '响水县'):
        print('->->->正在提取的事件是->->->' + '天嘉宜化工|响水县|盐城市响水县')
        data_event = data_all[data_all['命中关键词'].str.contains('天嘉宜化工|响水县|盐城市响水县')]
        print('**********read data for {0} ok'.format(event))
        data_event['发表时间'] = pd.to_datetime(data_event['发表时间'], format='%Y-%m-%d %H:%M')
        data_event['发表时间'] = data_event['发表时间'].apply(lambda x: datetime.strftime(x, '%Y-%m-%d %H:%M'))
        """盐城市响水县， 响水县， 爆炸"""
        start_time = datetime(2019, 3, 21, 15, 0)  # 最初的开始时间
        now_time = datetime(2019, 3, 22, 0, 0)  # 现在的时间
        end_time = datetime(2019, 9, 9, 0, 0)  # 最后的截止时间
        last_time = start_time
        out_all_time = dict()  # 存储所有时间节点的字典
        out_all_time[start_time.strftime('%Y-%m-%d')] = 0
        while (now_time < end_time):  # 当前时间小于最后的截止时间
            data_shape = data_event[data_event["发表时间"].str.startswith(last_time.strftime('%Y-%m-%d'))].shape
            out_all_time[now_time.strftime('%Y-%m-%d')] = data_shape[0]
            last_time = now_time
            now_time = now_time + timedelta(days=1)
        return out_all_time
    elif (event == '别墅'):
        print('->->->正在提取的事件是->->->' + '别墅|秦岭|秦岭北麓')
        data_event = data_all[data_all['命中关键词'].str.contains('别墅|秦岭|秦岭北麓')]
        print('**********read data for {0} ok'.format(event))
        data_event['发表时间'] = pd.to_datetime(data_event['发表时间'], format='%Y-%m-%d %H:%M')
        data_event['发表时间'] = data_event['发表时间'].apply(lambda x: datetime.strftime(x, '%Y-%m-%d %H:%M'))
        """别墅事件"""
        start_time = datetime(2018, 2, 11, 15, 0)  # 最初的开始时间
        now_time = datetime(2018, 2, 12, 0, 0)  # 现在的时间
        end_time = datetime(2019, 10, 1, 0, 0)  # 最后的截止时间
        last_time = start_time
        out_all_time = dict()  # 存储所有时间节点的字典
        out_all_time[start_time.strftime('%Y-%m-%d')] = 0
        while (now_time < end_time):  # 当前时间小于最后的截止时间
            data_shape = data_event[data_event["发表时间"].str.startswith(last_time.strftime('%Y-%m-%d'))].shape
            out_all_time[now_time.strftime('%Y-%m-%d')] = data_shape[0]
            last_time = now_time
            now_time = now_time + timedelta(days=1)
        return out_all_time
    elif (event == '灌云县'):
        print('->->->正在提取的事件是->->->' + '灌云县|化工企业')
        data_event = data_all[data_all['命中关键词'].str.contains('灌云县|化工企业')]
        print('**********read data for {0} ok'.format(event))
        data_event['发表时间'] = pd.to_datetime(data_event['发表时间'], format='%Y-%m-%d %H:%M')
        data_event['发表时间'] = data_event['发表时间'].apply(lambda x: datetime.strftime(x, '%Y-%m-%d %H:%M'))
        """灌云县"""
        start_time = datetime(2018, 4, 18, 21, 0)  # 最初的开始时间
        now_time = datetime(2018, 4, 19, 0, 0)  # 现在的时间
        end_time = datetime(2018, 5, 24, 0, 0)  # 最后的截止时间
        last_time = start_time
        out_all_time = dict()  # 存储所有时间节点的字典
        out_all_time[start_time.strftime('%Y-%m-%d')] = 0
        while (now_time < end_time):  # 当前时间小于最后的截止时间
            data_shape = data_event[data_event["发表时间"].str.startswith(last_time.strftime('%Y-%m-%d'))].shape
            out_all_time[now_time.strftime('%Y-%m-%d')] = data_shape[0]
            last_time = now_time
            now_time = now_time + timedelta(days=1)
        return out_all_time
    else:
        print("不存在输入的{}该事件，请从新检查后输入".format(event))
        exit()

"""************ 3、 画单日数量变化图！************"""
def show_v_graph(event, time_num):
    plt.rcParams['font.family'] = ['sans-serif']
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.rcParams['font.size'] = 18
    counts = pd.DataFrame.from_dict(time_num, orient='index', columns=['num'])
    counts['time'] = counts.index  # 加入时间节点
    c_s = 0
    y1 = counts['num'].tolist()
    x1 = counts['time'].tolist()
    print(y1, x1)
    fig, ax1 = plt.subplots(figsize=(16, 6))
    ax1.plot(np.array(x1), np.array(y1), label='舆情数量', color='r')
    plt.xlabel('时间', fontsize=16)
    plt.ylabel('单日舆情数量', fontsize=16)
    xticks = list(range(0, len(x1), 3))
    xlabels = [x1[x] for x in xticks]
    xticks.append(len(x1))
    xlabels.append('2018-05-02')
    ax1.set_xticks(xticks)
    ax1.set_xticklabels(xlabels, rotation=45)
    # plt.xticks(rotation = 45) #完整标签的显示
    for size in ax1.get_xticklabels():  # 获取x轴上所有坐标，并设置字号
        size.set_fontname('Times New Roman')
        size.set_fontsize('16')
    for size in ax1.get_yticklabels():  # 获取y轴上所有坐标，并设置字号
        size.set_fontname('Microsoft YaHei')  # 雅黑
        size.set_fontsize('12')
    # plt.axis('equal')
    font1 = {'family': 'SimSun',
             'weight': 'normal',
             'size': 16,
             }
    plt.legend(prop=font1)
    for a, b in zip(x1, y1):
        plt.text(a, b + 0.001, s='%d' % b, ha='center', va='bottom', fontsize=14)
    plt.savefig('{0}v_t图.png'.format(event))
    plt.show()

"""************ 4、 画总体数量变化图！************"""
def show_c_graph(event, time_num):
    plt.rcParams['font.family'] = ['sans-serif']
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.rcParams['font.size'] = 18
    counts = pd.DataFrame.from_dict(time_num, orient='index', columns=['num'])
    counts['time'] = counts.index  # 加入时间节点
    c_s = 0
    y = counts['num'].tolist()

    y1 = list()
    for i in y:
        c_s += i
        y1.append(c_s)
    x1 = counts['time'].tolist()
    fig, ax1 = plt.subplots(figsize=(16, 6))
    ax1.plot(np.array(x1), np.array(y1), label='评论数', color='r')
    plt.xlabel('时间', fontsize=16)
    plt.ylabel('舆情总数量', fontsize=16)
    xticks = list(range(0, len(x1), 3))
    xlabels = [x1[x] for x in xticks]
    xticks.append(len(x1))
    xlabels.append(x1[-1])
    ax1.set_xticks(xticks)
    ax1.set_xticklabels(xlabels, rotation=45)
    # plt.xticks(rotation = 45) #完整标签的显示
    for size in ax1.get_xticklabels():  # 获取x轴上所有坐标，并设置字号
        size.set_fontname('Times New Roman')
        size.set_fontsize('16')
    for size in ax1.get_yticklabels():  # 获取y轴上所有坐标，并设置字号
        size.set_fontname('Microsoft YaHei')  # 雅黑
        size.set_fontsize('12')
    # plt.axis('equal')
    font1 = {'family': 'SimSun',
             'weight': 'normal',
             'size': 16,
             }
    plt.legend(prop=font1)

    xticks = list(range(0, len(x1), 3))
    num_x = [x1[x] for x in xticks]
    num_y = [y1[x] for x in xticks]

    for a, b in zip(num_x, num_y):
        plt.text(a, b + 0.001, s='%d' % b, ha='center', va='bottom', fontsize=14)
    plt.savefig('{0}c_t图.png'.format(event))
    plt.show()
    
    
    tree_dir = {'../00data/data-export/2019/'}  # {'00data/data-export/2017/','00data/data-export/2018/','00data/data-export/2019/'}

data_all = read_data(tree_dir)  # 读原始数据库
# @function--input  '宁晋','保姆','豆各庄','响水县','别墅','灌云县'
time_num = get_event('宁晋', data_all)  # 读取某一事件
show_v_graph('宁晋', time_num)  # 显示画图
show_c_graph('宁晋', time_num)  # 显示画图


import numpy as np
import pandas as pd
from datetime import *
from matplotlib import pyplot as plt

"""************ 1、读取舆情数据！************"""
def read_data(file_dir):
    data_all = pd.DataFrame()
    print('->->->正在读取->->->' + file_dir)
    df = pd.read_csv(file_dir, encoding='gb18030')
    data_all = df
    print('数据的大小为:{0}'.format(data_all.shape))
    print('#' * 30, 'data read ok', '#' * 30)
    
    event = file_dir.split('.')[0]
    if (event == '宁晋'):
        data_event = data_all
        data_event['发表时间'] = pd.to_datetime(data_event['发表时间'], format='%Y-%m-%d %H:%M')
        data_event['发表时间'] = data_event['发表时间'].apply(lambda x: datetime.strftime(x, '%Y-%m-%d %H:%M'))
        """宁晋污染"""
        start_time = datetime(2018, 3, 29, 14, 0)  # 最初的开始时间
        now_time = datetime(2018, 3, 30, 0, 0)  # 现在的时间
        end_time = datetime(2018, 4, 30, 20, 0)  # 最后的截止时间
        last_time = start_time
        out_all_time = dict()  # 存储所有时间节点的字典
        out_all_time[start_time.strftime('%Y-%m-%d')] = 0
        while (now_time < end_time):  # 当前时间小于最后的截止时间
            data_shape = data_event[data_event["发表时间"].str.startswith(last_time.strftime('%Y-%m-%d'))].shape
            out_all_time[now_time.strftime('%Y-%m-%d')] = data_shape[0]
            last_time = now_time
            now_time = now_time + timedelta(days=1)
        return out_all_time
    elif (event == '豆各庄'):
        data_event = data_all
        data_event['发表时间'] = pd.to_datetime(data_event['发表时间'], format='%Y-%m-%d %H:%M')
        data_event['发表时间'] = data_event['发表时间'].apply(lambda x: datetime.strftime(x, '%Y-%m-%d %H:%M'))
        """诺如，豆各庄水污染"""
        start_time = datetime(2019, 7, 13, 11, 0)  # 最初的开始时间
        now_time = datetime(2019, 7, 14, 0, 0)  # 现在的时间
        end_time = datetime(2019, 7, 30, 0, 0)  # 最后的截止时间
        last_time = start_time
        out_all_time = dict()  # 存储所有时间节点的字典
        out_all_time[start_time.strftime('%Y-%m-%d')] = 0
        while (now_time < end_time):  # 当前时间小于最后的截止时间
            data_shape = data_event[data_event["发表时间"].str.startswith(last_time.strftime('%Y-%m-%d'))].shape
            out_all_time[now_time.strftime('%Y-%m-%d')] = data_shape[0]
            last_time = now_time
            now_time = now_time + timedelta(days=1)
        return out_all_time
    else:
        print("不存在输入的{}该事件，请从新检查后输入".format(event))
        exit()

"""************ 2、 画单日数量变化图！************"""
def show_v_graph(event, time_num):
    plt.rcParams['font.family'] = ['sans-serif']
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.rcParams['font.size'] = 18
    counts = pd.DataFrame.from_dict(time_num, orient='index', columns=['num'])
    counts['time'] = counts.index  # 加入时间节点
    c_s = 0
    y1 = counts['num'].tolist()
    x1 = counts['time'].tolist()
    print(y1, x1)
    fig, ax1 = plt.subplots(figsize=(16, 6))
    ax1.plot(np.array(x1), np.array(y1), label='舆情数量', color='r')
    plt.xlabel('时间', fontsize=16)
    plt.ylabel('单日舆情数量', fontsize=16)
    xticks = list(range(0, len(x1), 3))
    xlabels = [x1[x] for x in xticks]
    xticks.append(len(x1))
    xlabels.append('2018-05-02')
    ax1.set_xticks(xticks)
    ax1.set_xticklabels(xlabels, rotation=45)
    # plt.xticks(rotation = 45) #完整标签的显示
    for size in ax1.get_xticklabels():  # 获取x轴上所有坐标，并设置字号
        size.set_fontname('Times New Roman')
        size.set_fontsize('16')
    for size in ax1.get_yticklabels():  # 获取y轴上所有坐标，并设置字号
        size.set_fontname('Microsoft YaHei')  # 雅黑
        size.set_fontsize('12')
    # plt.axis('equal')
    font1 = {'family': 'SimSun',
             'weight': 'normal',
             'size': 16,
             }
    plt.legend(prop=font1)
    for a, b in zip(x1, y1):
        plt.text(a, b + 0.001, s='%d' % b, ha='center', va='bottom', fontsize=14)
    plt.savefig('{0}v_t图.png'.format(event))
    plt.show()

"""************ 3、 画总体数量变化图！************"""
def show_c_graph(event, time_num):
    plt.rcParams['font.family'] = ['sans-serif']
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.rcParams['font.size'] = 18
    counts = pd.DataFrame.from_dict(time_num, orient='index', columns=['num'])
    counts['time'] = counts.index  # 加入时间节点
    c_s = 0
    y = counts['num'].tolist()

    y1 = list()
    for i in y:
        c_s += i
        y1.append(c_s)
    x1 = counts['time'].tolist()
    fig, ax1 = plt.subplots(figsize=(16, 6))
    ax1.plot(np.array(x1), np.array(y1), label='评论数', color='r')
    plt.xlabel('时间', fontsize=16)
    plt.ylabel('舆情总数量', fontsize=16)
    xticks = list(range(0, len(x1), 3))
    xlabels = [x1[x] for x in xticks]
    xticks.append(len(x1))
    xlabels.append(x1[-1])
    ax1.set_xticks(xticks)
    ax1.set_xticklabels(xlabels, rotation=45)
    # plt.xticks(rotation = 45) #完整标签的显示
    for size in ax1.get_xticklabels():  # 获取x轴上所有坐标，并设置字号
        size.set_fontname('Times New Roman')
        size.set_fontsize('16')
    for size in ax1.get_yticklabels():  # 获取y轴上所有坐标，并设置字号
        size.set_fontname('Microsoft YaHei')  # 雅黑
        size.set_fontsize('12')
    # plt.axis('equal')
    font1 = {'family': 'SimSun',
             'weight': 'normal',
             'size': 16,
             }
    plt.legend(prop=font1)

    xticks = list(range(0, len(x1), 3))
    num_x = [x1[x] for x in xticks]
    num_y = [y1[x] for x in xticks]

    for a, b in zip(num_x, num_y):
        plt.text(a, b + 0.001, s='%d' % b, ha='center', va='bottom', fontsize=14)
    plt.savefig('{0}c_t图.png'.format(event))
    plt.show()
    


# @function--input  '宁晋','保姆','豆各庄','响水县','别墅','灌云县'
time_num = read_data('宁晋.csv')
show_v_graph('宁晋', time_num)  # 显示画图
show_c_graph('宁晋', time_num)  # 显示画图
time_num = read_data('豆各庄.csv')
show_v_graph('豆各庄', time_num)  # 显示画图
show_c_graph('豆各庄', time_num)  # 显示画图
