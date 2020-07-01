import csv
import pandas as pd
D1=pd.read_table('ruel1_final.csv',sep='\s+',names = ['id','fc'])
D2=pd.read_table('ruel2_final.csv',sep='\s+',names = ['id','fc'])
d1=pd.DataFrame(D1)
d2=pd.DataFrame(D2)
d1.to_csv("11111.csv",index = False)
for i in range(1,5463):
    for t in range(1,2711):
        if ((d1.loc[[i],['id']]) is (d2.loc[[t],['id']])):
            print(11)
            
        