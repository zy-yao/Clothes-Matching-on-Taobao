
import pandas as pd
for i in range(0,2):
    d = pd.read_csv('/Users/YAO/.spyder-py3/ForPython/new method/rule1_halfyearesult3/result'+str(i+1)+'_3.csv')
    testItems = pd.read_csv('testItems.csv')
    predict = pd.merge(testItems,d)
    predict.to_csv('/Users/YAO/.spyder-py3/ForPython/new method/rule1_halfyearesult_last/result'+str(i+1)+'last.csv',index = False)



