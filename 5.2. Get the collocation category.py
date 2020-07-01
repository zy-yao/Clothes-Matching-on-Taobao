import pandas as pd
d_fashion = pd.read_csv('dim_fashion_matchsets_remove_coll_id_standard_ii.csv')
d_item = pd.read_csv('itemCategory.csv')
d_testItem_category = pd.merge(d_fashion,d_item,left_on = 'testItem',right_on = 'item',how = 'left')
d_testItem_matchItem_category = pd.merge(d_testItem_category,d_item,left_on = 'matchItem',right_on = 'item',how = 'left')
del d_testItem_matchItem_category['testItem']
del d_testItem_matchItem_category['matchItem']
del d_testItem_matchItem_category['item_x']
del d_testItem_matchItem_category['item_y']
d_testItem_matchItem_category.drop_duplicates(keep='first', inplace=True)
d_testItem_matchItem_category.to_csv('dim_fashion_matchsets_category.csv',index = False)
