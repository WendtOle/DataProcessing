#https://realpython.com/command-line-interfaces-python-argparse/
import argparse
import os
import sys
import pandas as pd

from utils import getAggregatedRevenue

my_parser = argparse.ArgumentParser(description='Get the revenue of a product by its itemID')

my_parser.add_argument('Path',
                       metavar='path',
                       type=str,
                       help='The path to the data folder containing infos.csv, items.csv and orders.csv')

my_parser.add_argument('itemID',
                       metavar='itemID',
                       type=int,
                       help='The itemID of the product ')

# Execute the parse_args() method
args = my_parser.parse_args()
data_folder_path = args.Path
item_id = args.itemID

if not os.path.isdir(data_folder_path):
    print('The path specified does not exist')
    sys.exit()

def getRevenueOfProductByID(item_id):
    agg_orders = getAggregatedRevenue(data_folder_path)
    result = agg_orders[agg_orders['itemID'] == item_id]['agg_salesPrice'].values[0]
    return result

print("revenue for itemID", item_id, "->" , getRevenueOfProductByID(item_id))