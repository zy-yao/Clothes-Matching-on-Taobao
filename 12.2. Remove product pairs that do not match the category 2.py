
import pandas as pd
d_result = pd.read_csv('merge_d_w_m_q_y_category.csv')
d_fashion = pd.read_csv('dim_fashion_matchsets_category.csv')
d = pd.merge(d_result,d_fashion,on = ['category_x','category_y'])
dsort = d.sort_values(['count_in_day','count_in_week','count_in_month','count_in_quater','count_in_halfyear'],ascending = False)
dsort.to_csv('merge_d_w_m_q_yRemoveNotCompareCategory.csv',index = False)
