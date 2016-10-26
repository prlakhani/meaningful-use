#!/usr/bin/env python3

"""
Executable to initially load data from a csv into the database.
Usage:
    python3 init_load_data.py
Note: Make sure you've run db_reset.sql first
"""

import requests
# Although not needed explicitly, import works to check early that psycopg2 is
# installed. Needed to connect to a postgres db
import psycopg2 
import pandas as pd
from sqlalchemy import create_engine
from getpass import getuser


def dl_csv():
    """Download the source csv, chunk-by-chunk
    Chunk strategy from:
    http://stackoverflow.com/questions/16694907/how-to-download-large-file-in-python-with-requests-py
    """
    url = "http://dashboard.healthit.gov/datadashboard/data/MU_REPORT_2015.csv"
    local_filename = url.split('/')[-1]
    r = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        for i, chunk in enumerate(r.iter_content(chunk_size=1024)): 
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
            print("Chunk {} written to local disk".format(i))
    return local_filename


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
    load_from_csv(dl_csv())
