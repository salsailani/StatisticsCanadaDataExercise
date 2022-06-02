from ETLscripts.auxilary.Connect_to_mongoDB import connect
from queries.auxilary.Settings import *


def load_from_staging_to_target(client):

    db_staging = client["stats_staging"]
    db_target = client["stats_target"]
    tables_staging = db_staging.list_collection_names()
    tables_target = db_target.list_collection_names()

    # if the datasets are not in the database, then insert (upsert does not make sense in this case)

    if "DataSet1Cleaned" not in tables_target:
        data_set1 = pd.DataFrame(list(db_staging.DataSet1.find()))

        # defining the identity value columns and replacing non numeric cells with NaN
        data_set1[total_aboriginal_column] = pd.to_numeric(data_set1[total_aboriginal_column], errors='coerce')
        data_set1[aboriginal_column] = pd.to_numeric(data_set1[aboriginal_column], errors='coerce')
        data_set1[non_aboriginal_column] = pd.to_numeric(data_set1[non_aboriginal_column], errors='coerce')

        data = data_set1.to_dict(orient="records")
        db_target.DataSet1Cleaned.insert_many(data)

    if "DataSet2Cleaned" not in tables_target:
        data_set2 = pd.DataFrame(list(db_staging.DataSet2.find()))
        data2 = data_set2.to_dict(orient="records")
        db_target.DataSet2Cleaned.insert_many(data2)


def main():
    client = connect()
    load_from_staging_to_target(client)


main()
