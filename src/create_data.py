#!/usr/bin/python3

import os, average
import pandas as pd
from read_api import df as api
from average import Average as ave

class Parlor:
    def __init__(self, parlor_id, m_ids):
        self.strdate = pd.to_datetime('today').strftime("%Y%m%d")
        self.parlor_id = parlor_id
        self.df = api(parlor_id, m_ids)
        self.average = ave(self.df)

    def write_csv(self):
        self.df.to_csv('../data/{}.{}.csv'.format(self.parlor_id, self.strdate), index = True, header = True)

        total_path  = '../logs/{}.{}.log'.format(self.parlor_id, 'total')
        total_df = pd.read_csv(total_path, index_col = 0).append(self.average.total(), sort=False) if os.path.exists(total_path) else self.average.total()
        total_df.to_csv(total_path, header = True, index = True)

        indivisual_path = '../logs/{}.{}.log'.format(self.parlor_id, 'indivisual')
        indivisual_df = pd.read_csv(indivisual_path, index_col = 0).append(self.average.indivisual(), sort=False) if os.path.exists(indivisual_path) else self.average.indivisual()
        indivisual_df.to_csv(indivisual_path, header = True, index = True)

if __name__ == '__main__':

    write_csv = lambda parlors: [parlor.write_csv() for parlor in parlors]
    sk = lambda: ('sunkainan', list(range(185, 198 + 1)) + list(range(227, 240 + 1)))
    sg = lambda: ('sunginowan', list(range(145, 176 + 1)))

    write_csv([Parlor(*sg()), Parlor(*sk())])