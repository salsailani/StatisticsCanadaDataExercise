from queries.auxilary.Settings import *


def get_aboriginal_proportions(df, province_list):
    # filters the dimensions columns, returns provinces in region x28 dataframe
    filtered = df[(df["DIM: Income statistics (17)"] == "Total - Income statistics")
                  & (df[age_column] == "Total - Age")
                  & (df[sex_column] == "Total - Sex")
                  & (df["DIM: Registered or Treaty Indian status (3)"] == 'Total - Population by Registered or Treaty Indian status')
                  & (df["GEO_NAME"].isin(province_list))]

    # sum identity numbers in provinces in region
    total_aboriginal_and_non_aboriginal_population = filtered[total_aboriginal_column].sum()
    aboriginal_population = filtered[aboriginal_column].sum()
    non_aboriginal_population = filtered[non_aboriginal_column].sum()

    # proportions
    aboriginal_proportion = aboriginal_population / total_aboriginal_and_non_aboriginal_population
    non_aboriginal_proportion = non_aboriginal_population / total_aboriginal_and_non_aboriginal_population

    # prints
    print("")
    print("a.")
    print("Proportion of population by Aboriginal Identity and Non-Aboriginal Identity:")
    print("")
    print("Aboriginal Proportion: " + str(aboriginal_proportion))
    print("Non_Aboriginal Proportion: " + str(non_aboriginal_proportion))
    print("")
