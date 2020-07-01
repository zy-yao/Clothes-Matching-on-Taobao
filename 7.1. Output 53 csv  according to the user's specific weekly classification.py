import pandas as pd
d = pd.read_csv('user_bought_history_standard.csv')
del d['day']
del d['month']
del d['quarter']
for i in range(0,len(set(d['week']))):
    dPerDay = d[d['week'] == i+1]
    del dPerDay['week']
    dPerDay.drop_duplicates(keep='first', inplace=True)
    dPerDay.to_csv('/Users/YAO/.spyder-py3/ForPython/new method/week_53sheets/user_bought_history_'+str(i+1)+'_standard.csv',index = False)
