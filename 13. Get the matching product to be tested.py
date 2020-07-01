import pandas as pd
import csv
d = pd.read_csv('merge_d_w_m_q_yRemoveNotCompareCategory.csv')
with open('II.csv','w',newline='') as f:
    writer = csv.writer(f)
    #writer.writerow(['order','testItem'])
    for name,group in d.groupby('testItem'): 
        line = [int(group.iloc[0]['testItem']),int(group.iloc[0]['matchItem'])] #要写入的东西，这是每个group组的第一行，包含user_id和买的第一件商品
        for i in range(1,len(group)): #len(group)表示这个user_id买了多少个商品
            if int(group.iloc[i]['count_in_quater']) == 0:
                break
            line.append(int(group.iloc[i]['matchItem'])) 
            if len(line) == 201: #首列为为预测列
                break
        writer.writerow(line)