#!/usr/bin/python3

import requests, json
import pandas as pd
from itertools import count, chain

def df(parlor_id, m_ids):

    columns = ['no', 'timestamp', 'type', 'times', 'amount']
    uri = 'http://{}.p-moba.net/ajax_dedama_log.php'.format(parlor_id)

    def gen_page(m_id):
        bonus_type  = lambda c: {'0':'BB','1':'RB'}[c]
        create_data = lambda d:[d['machine_no'] ,d['targettime'],bonus_type(d['data12']), float(d['data10']), float(d['data11'])]
        for page in count(1):
            res =  json.loads(requests.get(uri, {'id': str(m_id), 'page': str(page)}).text)
            yield [create_data(bonus) for bonus in res['list']]
            if res['next_btn_flg'] == 0: break

    def indivisual_data(m_id):
        return pd.DataFrame(list(chain.from_iterable(gen_page(m_id)))
            , columns = columns).astype({'times':int, 'amount': int}).set_index(columns[:2])

    return pd.concat([indivisual_data(id) for id in m_ids]).sort_values(['no', 'timestamp'])