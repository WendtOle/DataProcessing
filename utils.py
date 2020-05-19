import pandas as pd

from DataHandler import DataHandler

def get_item_revenue(data_handler):
    orders = data_handler.get_orders()
    orders['revenue'] = orders['order'] * orders['salesPrice']
    agg_orders = orders[["itemID", "revenue"]].groupby("itemID").sum()
    return agg_orders.reset_index([0, 'itemID'])

def getPromotedProducts(data_handler):
    infos_cleaned = data_handler.get_infos().dropna()
    promotion = pd.DataFrame(infos_cleaned.promotion.str.split(',').tolist(),
                             index=infos_cleaned.itemID).stack()
    promotion = promotion.reset_index([0, 'itemID'])
    promotion.columns = ['itemID', 'date']
    promotion['date'] = promotion['date'].astype('datetime64[ns]')
    return promotion

def get_itemIDs_in_second_level_category(data_handler, category1,category2):
    items = data_handler.get_items()
    return items.loc[(items['category1'] == category1) & (items['category2'] == category2)]['itemID']