#!/usr/bin/env python3

"""
Executable to initially load data from a csv into the database.
Usage:
    python3 init_load_data.py
Note: Make sure you've run db_reset.sql first
"""

import psycopg2
import pandas as pd
from sqlalchemy import create_engine
from getpass import getuser

# cheat: use pd to_sql
full_df = pd.read_csv('MU_REPORT_2015.csv', encoding='Latin1')
full_df.columns = [col.lower().replace('.', '_') for col in full_df.columns]
full_df[full_df['specialty'].isnull()].shape[0]
full_df.loc[full_df['specialty'].isnull(), 'specialty'] = 'UNKNOWN'

engine = create_engine('postgres://{}@localhost/ehr_mu'.format(getuser()))
full_df.to_sql('attest_2015', engine)

# TODO: add some tests to see how this process went
