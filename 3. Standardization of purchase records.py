#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  1 16:01:40 2018

@author: YAO
"""
import csv
import pandas as pd
import itertools

d = pd.read_csv('user_bought_history_remove11and12.csv')
dateSet = set(d['create_at']) #得到有哪些天
dateList = list(dateSet)
dateList.sort() #排序

with open('user_bought_history_remove11and12.csv') as origin_f:
    with open('user_bought_history_standard.csv','w',newline='') as new_f:
        reader = csv.reader(origin_f)
        writer = csv.writer(new_f)
        head = ['user_id','item_id','day','week','month','quarter']
        writer.writerow(head)
        for row in itertools.islice(reader,1,None): #跳过标题进行读取
            for i in range(0,len(dateList)):
                if int(row[2]) == dateList[i]:
                    day = i+1
            week = int((day-1)/7)+1
            month = row[2][4:6]
            quarter =int((int(month)-1)/3)+1
            row.append(day)
            row.append(week)
            row.append(month)
            row.append(quarter)
            del row[2]
            writer.writerow(row)
