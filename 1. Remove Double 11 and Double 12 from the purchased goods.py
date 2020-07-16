#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue April  1 16:01:40 2018

@author: YAO
"""
import pandas as pd
d= pd.read_table('user_bought_history.txt',sep='\s+',names = ['user_id','item_id','create_at'])
dRemove11and12 = d[(d['create_at'] != 20141111) & (d['create_at'] != 20141212)]
dRemove11and12.to_csv('user_bought_history_remove11and12.csv',index = False)

