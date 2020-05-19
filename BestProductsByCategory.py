from DataHandler import DataHandler
from utils import get_item_revenue, get_itemIDs_in_second_level_category

print("Get the items with the highest revenue by its category.")
category1 = int(input('Category One: '))
category2 = int(input('Category Two: '))

data_handler = DataHandler()
items = data_handler.get_items()

second_level_category_item_ids = get_itemIDs_in_second_level_category(data_handler, category1, category2)

if second_level_category_item_ids.size > 0:
    item_revenue_complete = get_item_revenue(data_handler)
    second_level_category_item_revenue = item_revenue_complete[item_revenue_complete['itemID'].isin(second_level_category_item_ids)]

    print(second_level_category_item_revenue.sort_values(by=['revenue'], ascending=False).head(5))
else:
    print("There are now items in that category!")
