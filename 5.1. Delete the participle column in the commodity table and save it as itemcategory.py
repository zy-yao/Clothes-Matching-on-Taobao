import pandas as pd
import csv
# load data
dim_fashion_matchsets = pd.read_table(r'商品信息dim_items（new).txt',sep='\s+',names = ['item','category','terms'])
del dim_fashion_matchsets['terms']
dim_fashion_matchsets.to_csv('itemCategory.csv',index = False)

