#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  8 22:59:55 2018

@author: YAO
"""
import csv
import re
import itertools

with open('dim_fashion_matchsets_remove_coll_id.csv') as origin_f:
    with open('dim_fashion_matchsets_remove_coll_id_standard.csv','w',newline='') as new_f:
        reader = csv.reader(origin_f,delimiter = ';' ,  quotechar = '|')
        writer = csv.writer(new_f)
        for row in reader:
            count = 0 #第几个多商品项，或多商品项的数量
            oneMoreItem = [] #包含多商品的项
            divideOneMoreItem = [] #分解多商品的项
            index = [] #多商品项在记录中的位置
            for i in range(len(row)):
                if ',' in row[i]:
                    oneMoreItem.append(row[i])
                    index.append(i)
                    divideOneMoreItem.append(re.split(',',str(oneMoreItem[count])))
                    count += 1
            for decare in itertools.product(*[divideOneMoreItem[j] for j in range(count)]):
                for k in range(len(index)):
                    row[index[k]] = decare[k]
                writer.writerow(row)
