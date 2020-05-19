import argparse
import os
import sys
import pandas as pd

from DataHandler import DataHandler
from utils import get_item_revenue, getPromotedProducts

#TODO
my_parser = argparse.ArgumentParser(description='missing')

my_parser.add_argument('Path',
                       metavar='path',
                       type=str,
                       help='The path to the data folder containing infos.csv, items.csv and orders.csv')

my_parser.add_argument('begin',
                       metavar='begin',
                       type=str,
                       help='missing')#TODO

my_parser.add_argument('until',
                       metavar='until',
                       type=str,
                       help='missing')#TODO

#from_date = input("Input the beginning date:")
#print(from_date)

# Execute the parse_args() method
args = my_parser.parse_args()
data_folder_path = args.Path
begin = args.begin
until = args.until

if not os.path.isdir(data_folder_path):
    print('The path specified does not exist')
    sys.exit()

data_handler = DataHandler(data_folder_path)

promoted_items = getPromotedProducts(data_folder_path)
promoted_item_IDs_in_range = promoted_items[(promoted_items['date'] >= begin) & (promoted_items['date'] <= until)]['itemID']
items = data_handler.get_items()
promoted_items_in_range = items[items['itemID'].isin(promoted_item_IDs_in_range)]
promoted_products_per_category = promoted_items_in_range[['itemID','category1']].groupby('category1').count()

print(promoted_products_per_category)