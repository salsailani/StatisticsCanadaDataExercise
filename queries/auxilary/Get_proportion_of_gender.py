from queries.auxilary.Settings import *


def get_proportion_of_gender(df, province_list):
    filtered = df[(df["DIM: Income statistics (17)"] == "Total - Income statistics")
                  & (df[age_column] == "Total - Age")
                  & (df["DIM: Registered or Treaty Indian status (3)"] == 'Total - Population by Registered or Treaty Indian status')
                  & (df["GEO_NAME"].isin(province_list))]

    # filter by sex
    filter_total_sex = filtered[(filtered[sex_column] == "Total - Sex")]
    filter_male = filtered[(filtered[sex_column] == "Male")]
    filter_female = filtered[(filtered[sex_column] == "Female")]

    # sum aboriginal numbers in provinces in region
    filter_total_aboriginal = filter_total_sex[aboriginal_column].sum()
    filter_male_aboriginal = filter_male[aboriginal_column].sum()
    filter_female_aboriginal = filter_female[aboriginal_column].sum()

    # sum non aboriginal numbers in provinces in region
    filter_total_non_aboriginal = filter_total_sex[non_aboriginal_column].sum()
    filter_male_non_aboriginal = filter_male[non_aboriginal_column].sum()
    filter_female_non_aboriginal = filter_female[non_aboriginal_column].sum()

    # proportions
    male_aboriginal_proportion = filter_male_aboriginal / filter_total_aboriginal
    female_aboriginal_proportion = filter_female_aboriginal / filter_total_aboriginal
    male_non_aboriginal_proportion = filter_male_non_aboriginal / filter_total_non_aboriginal
    female_non_aboriginal_proportion = filter_female_non_aboriginal / filter_total_non_aboriginal

    # prints
    print("c.")
    print("Proportion of male vs female population by Aboriginal Identity and Non-Aboriginal Identity:")
    print("")
    print("Aboriginal Proportions:")
    print("Male Proportion: " + str(male_aboriginal_proportion) + " Female Proportion: " + str(
        female_aboriginal_proportion))
    print("")
    print("Non_Aboriginal Proportions:")
    print("Male proportion: " + str(male_non_aboriginal_proportion) + " Female proportion: " + str(
        female_non_aboriginal_proportion))
    print("")
