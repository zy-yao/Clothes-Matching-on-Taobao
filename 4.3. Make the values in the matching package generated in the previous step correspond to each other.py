import csv
import pandas as pd

with open('dim_fashion_matchsets_remove_coll_id_standard.csv') as origin_f:
    with open('dim_fashion_matchsets_remove_coll_id_standard_ii.csv','w',newline='') as new_f:
        reader = csv.reader(origin_f)
        writer = csv.writer(new_f)
        writer.writerow(['testItem','matchItem'])
        for row in reader:
            for i in range(0,len(row)):
                for j in range(0,len(row)):
                    line = []
                    if i != j:
                        line.append(row[i])  
                        line.append(row[j])
                        writer.writerow(line)
                        
d = pd.read_csv('dim_fashion_matchsets_remove_coll_id_standard_ii.csv')
d.drop_duplicates(keep='first', inplace=True) #去重，保留第一个重复的
d.to_csv('dim_fashion_matchsets_remove_coll_id_standard_ii.csv',index = False)
