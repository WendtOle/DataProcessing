import argparse
import os
import sys
import pandas as pd

from DataHandler import DataHandler
from utils import getAggregatedRevenue

#TODO
my_parser = argparse.ArgumentParser(description='missing')

my_parser.add_argument('Path',
                       metavar='path',
                       type=str,
                       help='The path to the data folder containing infos.csv, items.csv and orders.csv')

my_parser.add_argument('category1',
                       metavar='category1',
                       type=int,
                       help='missing')#TODO

my_parser.add_argument('category2',
                       metavar='category2',
                       type=int,
                       help='missing')#TODO

# Execute the parse_args() method
args = my_parser.parse_args()
data_folder_path = args.Path
category1 = args.category1
category2 = args.category2

if not os.path.isdir(data_folder_path):
    print('The path specified does not exist')
    sys.exit()

data_handler = DataHandler(data_folder_path)
items = data_handler.get_items()
selected_items02 = items.loc[(items['category1'] == category1) & (items['category2'] == category2)]['itemID']

agg_orders = getAggregatedRevenue(data_folder_path)

print("Category1:",category1, "- Category2:", category2)
print(agg_orders[agg_orders['itemID'].isin(selected_items02)].sort_values(by=['agg_salesPrice'], ascending=False).head())
