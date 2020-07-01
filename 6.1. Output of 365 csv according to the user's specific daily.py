import pandas as pd
d = pd.read_csv('user_bought_history_standard.csv')
del d['week']
del d['month']
del d['quarter']
for i in range(0,len(set(d['day']))):
    dPerDay = d[d['day'] == i+1]
    del dPerDay['day']
    dPerDay.drop_duplicates(keep='first', inplace=True)
    dPerDay.to_csv('/Users/YAO/.spyder-py3/ForPython/new method/365sheets/user_bought_history_'+str(i+1)+'_standard.csv',index = False)
