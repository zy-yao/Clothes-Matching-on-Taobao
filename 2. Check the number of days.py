#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  1 16:01:40 2018

@author: YAO
"""
import pandas as pd
d = pd.read_csv('user_bought_history_remove11and12.csv')
dateSet = set(d['create_at']) #得到有哪些天，set集合可去除重复
dateList = list(dateSet)
dateList.sort() #排序
