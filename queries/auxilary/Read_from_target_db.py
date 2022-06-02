from ETLscripts.auxilary.Connect_to_mongoDB import connect
from queries.auxilary.Settings import *
import pandas as pd


def read_dataset1_from_target_db():

    client = connect()

    db = client["stats_target"]
    df = pd.DataFrame(list(db.DataSet1Cleaned.find()))

    # remove the first 2 columns added by MongoDB
    df = df.iloc[:, 2:]

    # cast numerics to float
    df[total_aboriginal_column].astype('float')
    df[aboriginal_column].astype('float')
    df[non_aboriginal_column].astype('float')

    return df


