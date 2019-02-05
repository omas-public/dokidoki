#!/usr/bin/python3

import pandas as pd

class Average:
    def __init__(self, df, date = pd.to_datetime('today').strftime("%Y%m%d")):
        self.df = df
        self.strdate = date

    def _diff(self, df):
        return df['amount'] - df['times'] / 23 * 50

    def total(self):
        percentage = lambda df, limit: df[df < limit].count() / df.count() * 100
        a_time = self.df.query('times > 34')['times']
        f_time = self.df.groupby('no').first()['times']
        total_diff = self._diff(self.df.sum())
        df = pd.DataFrame(
            [[total_diff, a_time.mean(), f_time.mean(), percentage(f_time, 30),percentage(f_time, 50), percentage(f_time, 100), percentage(f_time, 200)]]
            , columns=['total_diff', 'total_average', 'first_average', 'less_30', 'less_50', 'less_100', 'less_200']
            , index = [self.strdate])
        df.index.name = 'date'
        return df.astype(dtype = int)

    def indivisual(self):
        df = self.df.query('times > 33').groupby('no')['times'].agg([lambda _: self.strdate ,'count', 'mean', 'min', 'max']).rename(columns={'<lambda>': 'date'})
        df = df.assign(diff = self._diff(self.df.groupby('no').sum()), first_hit = self.df.groupby('no').first()['times'])
        return df.astype(dtype = int)
