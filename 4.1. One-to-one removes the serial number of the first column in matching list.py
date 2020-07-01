#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue April  8 22:14:16 2018

@author: YAO
"""
import pandas as pd
# load data
dim_fashion_matchsets = pd.read_table(r'搭配套餐dim_fashion_matchsets（new).txt',sep='\s+',names = ['coll_id','item_list'])
del dim_fashion_matchsets['coll_id']
dim_fashion_matchsets.to_csv('dim_fashion_matchsets_remove_coll_id.csv',index = False)

