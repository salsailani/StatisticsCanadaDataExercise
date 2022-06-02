from queries.auxilary.Settings import *


def get_average_total_income(df, province_list):
    # filters the dimensions columns, returns #number_of_provinces x 28 dataframe
    filtered = df[(df["DIM: Income statistics (17)"] == "Average total income ($)")
                  & (df[age_column] == "Total - Age")
                  & (df[sex_column] == "Total - Sex")
                  & (df["DIM: Registered or Treaty Indian status (3)"] == 'Total - Population by Registered or Treaty Indian status')
                  & (df["GEO_NAME"].isin(province_list))]

    # average identity numbers in provinces in region
    aboriginal_avg_income = filtered[aboriginal_column].mean()
    non_aboriginal_avg_income = filtered[non_aboriginal_column].mean()

    # prints
    print("b.")
    print("Average Total Income for Aboriginal Identity and Non-Aboriginal Identity:")
    print("")
    print("Aboriginal Average Income: " + str(aboriginal_avg_income))
    print("Non-Aboriginal Average Income: " + str(non_aboriginal_avg_income))
    print("")
