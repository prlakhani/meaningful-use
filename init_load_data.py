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


def load_from_csv(fn='MU_REPORT_2015.csv'):
    # cheat: use pd to_sql
    print("Loading data from csv into DataFrame")
    full_df = pd.read_csv('MU_REPORT_2015.csv', encoding='Latin1')
    print("CSV data loaded!")
    
    print("Beginning data cleaning")
    full_df.columns = [col.lower().replace('.', '_') for col in full_df.columns]
    full_df[full_df['specialty'].isnull()].shape[0]
    full_df.loc[full_df['specialty'].isnull(), 'specialty'] = 'UNKNOWN'
    print("Data cleaned!")
    
    print("Beginning to add records to database")
    engine = create_engine('postgres://{}@localhost/ehr_mu'.format(getuser()))
    full_df.to_sql('attest_2015', engine)
    print("Records added to database table `attest_2015'!")

# TODO: add some tests or asserts to see how this process went

if __name__ == '__main__':
    load_from_csv()
