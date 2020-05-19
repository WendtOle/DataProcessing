import argparse
import os
import sys
import pandas as pd

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

promotion = getPromotedProducts(data_folder_path)
itemIDs_in_promotion = promotion[(promotion['date'] >= begin) & (promotion['date'] <= until)]['itemID']

items = pd.read_csv(r'' + data_folder_path + '/items.csv', sep='|')

items_in_promotion = items[items['itemID'].isin(itemIDs_in_promotion)]
promoted_products = items_in_promotion[['itemID','category1']].groupby('category1').count()
print(promoted_products.head())