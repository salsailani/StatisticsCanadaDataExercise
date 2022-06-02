def get_province_list(region):
    # implementing Four-Region Model

    if region == "Western":
        province_list = ['British Columbia', 'Alberta', 'Saskatchewan', 'Manitoba']
    elif region == "Central":
        province_list = ['Ontario', 'Quebec']
    elif region == "Atlantic":
        province_list = ['New Brunswick', 'Prince Edward Island', 'Nova Scotia', 'Newfoundland and Labrador']
    elif region == "Northern":
        province_list = ['Yukon', 'Northwest territories', 'Navanut']
    elif region == "Canada":
        province_list = ['Canada']

    return province_list
