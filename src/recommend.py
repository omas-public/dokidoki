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

    def recommend(self):
        df = self.average.indivisual().sort_values('mean').head(8)
        print(df)
        print(self.df.query('times > 33').loc[df.index.tolist()].groupby(['no','type']).agg(['count', 'mean']))

if __name__ == '__main__':

    recommend = lambda parlors: [parlor.recommend() for parlor in parlors]
    sk = lambda: ('sunkainan', list(range(185, 198 + 1)) + list(range(227, 240 + 1)))
    sg = lambda: ('sunginowan', list(range(145, 176 + 1)))

    recommend([ Parlor(*sk())])