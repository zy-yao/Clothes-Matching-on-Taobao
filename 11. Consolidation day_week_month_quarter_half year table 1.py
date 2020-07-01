import pandas as pd
dDay = pd.read_csv('count_in_day.csv') #日表
dWeek = pd.read_csv('count_in_week.csv') #周表
dMonth = pd.read_csv('count_in_month.csv') #月表
dQuarter = pd.read_csv('count_in_quater.csv') #季表
dHalfYear = pd.read_csv('count_in_halfyear.csv') #半年表
dYandQ = pd.merge(dHalfYear,dQuarter,on=['testItem','matchItem'],how='left') #左连接半年、季度
dYandQandM = pd.merge(dYandQ,dMonth,on=['testItem','matchItem'],how='left') #左连接半年季度、月
dYandQandMandW = pd.merge(dYandQandM,dWeek,on=['testItem','matchItem'],how='left')#左连接半年季度月、周
dYandQandMandWandD = pd.merge(dYandQandMandW,dDay,on=['testItem','matchItem'],how='left') #左连接半年季度月周、日
dYandQandMandWandD.fillna(0,inplace=True) #空值赋0
dYandQandMandWandDsort = dYandQandMandWandD.sort_values(['count_in_day','count_in_week','count_in_month','count_in_quater','count_in_halfyear'],ascending = False) #按日、周、月、季度、半年的优先级降序排列
dYandQandMandWandDsort.drop_duplicates(['testItem','matchItem'],keep='first', inplace=True) #去重
dYandQandMandWandDsort.to_csv('merge_d_w_m_q_y.csv',index = False)
