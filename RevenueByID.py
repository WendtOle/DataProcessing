from DataHandler import DataHandler
from utils import get_item_revenue

print("Get the overall revenue of item by its ID.")

data_handler = DataHandler()
agg_orders = get_item_revenue(data_handler)

item_id = int(input("Input ItemID: "))

try:
    result = agg_orders[agg_orders['itemID'] == item_id]['revenue'].values[0]
    print("revenue for itemID:",item_id)
    print("{:.2f}".format(result), "€")
except IndexError as e:
    print("ItemID is not valid")