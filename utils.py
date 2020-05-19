import pandas as pd

from DataHandler import DataHandler

def getAggregatedRevenue(data_folder_path):
    data_handler = DataHandler(data_folder_path)
    orders = data_handler.get_orders()
    orders['agg_salesPrice'] = orders['order'] * orders['salesPrice']
    agg_orders = orders[["itemID", "agg_salesPrice"]].groupby("itemID").sum()
    return agg_orders.reset_index([0, 'itemID'])

def getPromotedProducts(data_folder_path):
    data_handler = DataHandler(data_folder_path)
    infos_cleaned = data_handler.get_infos().dropna()
    promotion = pd.DataFrame(infos_cleaned.promotion.str.split(',').tolist(),
                             index=infos_cleaned.itemID).stack()
    promotion = promotion.reset_index([0, 'itemID'])
    promotion.columns = ['itemID', 'date']
    promotion['date'] = promotion['date'].astype('datetime64[ns]')
    return promotion