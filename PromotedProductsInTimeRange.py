from DataHandler import DataHandler
from utils import getPromotedProducts

print("Get the amount of items which where promoted in a certain time period per main category.")

begin = input("Input the beginning date (YYYY/MM/DD): ")
until = input("Input the end date (YYYY/MM/DD): ")

data_handler = DataHandler()

promoted_items = getPromotedProducts(data_handler)
promoted_item_IDs_in_range = promoted_items[(promoted_items['date'] >= begin) & (promoted_items['date'] <= until)]['itemID']
if promoted_item_IDs_in_range.size > 0:
    items = data_handler.get_items()
    promoted_items_in_range = items[items['itemID'].isin(promoted_item_IDs_in_range)]
    promoted_products_per_category = promoted_items_in_range[['itemID','category1']].groupby('category1').count()

    print(promoted_products_per_category)
else:
    print("There were no promotions in that time period. Please check the input type of the date again - YYYY/MM/DD!")