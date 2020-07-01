import pandas as pd
d_result = pd.read_csv('merge_d_w_m_q_y.csv')
d_item = pd.read_csv('itemCategory.csv')
d_testItem_category = pd.merge(d_result,d_item,left_on = 'testItem',right_on = 'item',how = 'left')
d_testItem_matchItem_category = pd.merge(d_testItem_category,d_item,left_on = 'matchItem',right_on = 'item',how = 'left')
del d_testItem_matchItem_category['item_x']
del d_testItem_matchItem_category['item_y']
d_testItem_matchItem_category.to_csv('merge_d_w_m_q_y_category.csv',index = False)
