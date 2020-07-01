import pandas as pd
for i in range(0,365):
    d = pd.read_csv('/Users/YAO/.spyder-py3/ForPython/new method/rule1_result2/result'+str(i+1)+'_2.csv')
    dcount = d.groupby(['testItem','matchItem']).size()
    dcount.to_csv('/Users/YAO/.spyder-py3/ForPython/new method/rule1_result3/result'+str(i+1)+'_3.csv',header = ['count_in_day']) 
