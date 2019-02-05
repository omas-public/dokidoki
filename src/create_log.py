#!/usr/bin/python3

import os, average
import pandas as pd
from read_csv import df as csv
from average import Average as ave

class Parlor:
    def __init__(self, parlor_id, date):
        self.strdate = date
        self.parlor_id = parlor_id
        self.df = pd.read_csv('../data/{}.{}.csv'.format(parlor_id, date), index_col = [0,1])
        self.average = ave(self.df, date)

    def write_csv(self):

        total_path  = '../logs/{}.{}.log'.format(self.parlor_id, 'total')
        total_df = pd.read_csv(total_path, index_col = 0).append(self.average.total(), sort=False) if os.path.exists(total_path) else self.average.total()
        total_df.to_csv(total_path, header = True, index = True)
        # print(total_df)
        indivisual_path = '../logs/{}.{}.log'.format(self.parlor_id, 'indivisual')
        indivisual_df = pd.read_csv(indivisual_path, index_col = 0).append(self.average.indivisual(), sort=False) if os.path.exists(indivisual_path) else self.average.indivisual()
        indivisual_df.to_csv(indivisual_path, header = True, index = True)
        # print(indivisual_df)

if __name__ == '__main__':

    write_csv = lambda parlors: [parlor.write_csv() for parlor in parlors]

    dates  = [
'20190108',
'20190109',
'20190110',
'20190111',
'20190113',
'20190114',
'20190115',
'20190117',
'20190118',
'20190119',
'20190120',
'20190121',
'20190122',
'20190123',
'20190124',
'20190125',
'20190126',
'20190127',
'20190128',
'20190129',
'20190130',
'20190131'
]

    for date in dates:
        for name in ['sunkainan', 'sunginowan']:
            p = Parlor(name, date)
            p.write_csv()