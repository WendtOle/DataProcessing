import pandas as pd


class DataHandler:

    def __init__(self, data_path = 'Data'):
        self.data_path = data_path

    def get_items(self):
        return self.get_csv_file('items')

    def get_csv_file(self,name):
        return pd.read_csv(r'' + self.data_path + '/' + name + '.csv', sep='|')

    def get_orders(self):
        return self.get_csv_file('orders')

    def get_infos(self):
        return self.get_csv_file('infos')