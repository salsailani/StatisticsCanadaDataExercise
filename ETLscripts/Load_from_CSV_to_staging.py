from ETLscripts.auxilary.Connect_to_mongoDB import connect
from queries.auxilary.Settings import *

data_set1_csv = 'datasets/98-400-X2016170_English_CSV_data.csv'
data_set2_csv = 'datasets/98-400-X2016131_English_CSV_data.csv'


def create_staging(client):

    # creates database stats_staging
    db = client["stats_staging"]

    # get table names
    tables = db.list_collection_names()

    # if the datasets are not in the database, then insert (upsert does not make sense in this case)
    if "DataSet1" not in tables:
        data_set1 = pd.read_csv(data_set1_csv)
        data = data_set1.to_dict(orient="records")
        db.DataSet1.insert_many(data)

    if "DataSet2" not in tables:
        data_set2 = pd.read_csv(data_set2_csv)
        data2 = data_set2.to_dict(orient="records")
        db.DataSet2.insert_many(data2)


def main():
    client = connect()
    create_staging(client)


main()
