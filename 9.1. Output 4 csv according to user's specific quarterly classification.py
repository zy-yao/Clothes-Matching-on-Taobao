import pandas as pd
d = pd.read_csv('user_bought_history_standard.csv')
del d['day']
del d['week']
del d['month']
for i in range(0,len(set(d['quarter']))):
    dPerDay = d[d['quarter'] == i+1]
    del dPerDay['quarter']
    dPerDay.drop_duplicates(keep='first', inplace=True)
    dPerDay.to_csv('/Users/YAO/.spyder-py3/ForPython/new method/quater_sheets/user_bought_history_'+str(i+1)+'_standard.csv',index = False)
