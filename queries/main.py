from queries.auxilary.Get_aboriginal_proportions import *
from queries.auxilary.Get_average_total_income import *
from queries.auxilary.Get_max_aboriginal_age_group import *
from queries.auxilary.Get_proportion_of_gender import *
from queries.auxilary.Get_province_list import *
from queries.auxilary.Read_from_target_db import read_dataset1_from_target_db
from queries.auxilary.Settings import regions_list
import sys


def run(df, region):
    print(region + " region")
    print("-------------------------")

    province_list = get_province_list(region)  # we take the region and return a province list

    get_aboriginal_proportions(df, province_list)
    get_average_total_income(df, province_list)
    get_proportion_of_gender(df, province_list)
    get_max_aboriginal_age_group(df, province_list)


def main():

    df = read_dataset1_from_target_db()

    # run(df, 'Central')

    # calling run for all regions and outputting to a text file
    sys.stdout = open('queries/output.txt', 'w')
    for region in regions_list:
        run(df, region)
    sys.stdout.close()


main()
