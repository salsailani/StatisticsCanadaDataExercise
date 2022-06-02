from queries.auxilary.Settings import *


def get_max_aboriginal_age_group(df, province_list):
    # filters the dimensions columns, returns provinces in the region x28 dataframe

    filtered = df[(df["DIM: Income statistics (17)"] == "Total - Income statistics")
                  & (df[sex_column] == "Total - Sex")
                  & (df[
                         "DIM: Registered or Treaty Indian status (3)"] == 'Total - Population by Registered or Treaty Indian status')
                  & (df["GEO_NAME"].isin(province_list))]

    # exclude total age age group
    filtered = filtered[filtered[age_column] != "Total - Age"]

    # find max out of all age groups
    max_aboriginal_row = filtered[filtered[aboriginal_column] == filtered[aboriginal_column].max()]

    # print max age group
    max_age_group = max_aboriginal_row[age_column].sum()
    print("d.")
    print("Age group with the most number of individuals with Aboriginal Identity:")
    print("")
    print(max_age_group)
    print("")
