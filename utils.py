import pandas as pd

def getAggregatedRevenue(data_folder_path):
    orders = pd.read_csv(r'' + data_folder_path + '/orders.csv', sep='|')
    orders['agg_salesPrice'] = orders['order'] * orders['salesPrice']
    agg_orders = orders[["itemID", "agg_salesPrice"]].groupby("itemID").sum()
    return agg_orders.reset_index([0, 'itemID'])