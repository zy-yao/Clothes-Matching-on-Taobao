import pandas as pd
import csv
for i in range(0,53):
    d = pd.read_csv('/Users/YAO/.spyder-py3/ForPython/new method/week_53sheets/user_bought_history_'+str(i+1)+'_standard.csv')     
    with open('/Users/YAO/.spyder-py3/ForPython/new method/rule1_weekresult/result'+str(i+1)+'_1.csv','w',newline='') as f:
        writer = csv.writer(f)
        for name,group in d.groupby('user_id'): 
            line = [] 
            for i in range(0,len(group)): 
                line.append(group.iloc[i]['item_id'])
            if len(line) > 1: 
                writer.writerow(line)
