import pandas as pd
d = pd.read_csv('/Users/YAO/.spyder-py3/ForPython/new method/result_last/result1last.csv')
for i in range(1,365):
    dd = pd.read_csv('/Users/YAO/.spyder-py3/ForPython/new method/result_last/result'+str(i+1)+'last.csv')
    d = d.append(dd) 
dsort = d.sort_values('count_in_day',ascending = False)
dsort.drop_duplicates(['testItem','matchItem'],keep='first', inplace=True)
dsort.to_csv('count_in_day.csv',index = False)
