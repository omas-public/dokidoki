#!/usr/bin/python3

import pandas as pd

def df(parlor_id, date):
  return pd.read_csv('../data/{}.{}.csv'.format(parlor_id, date), index_col = [0,1]).sort_values(['no','timestamp'])