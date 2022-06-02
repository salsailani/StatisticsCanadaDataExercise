
# Statistics Canada Data Exercise

Must download the datasets and place them in the dataset folder (could not push due to file size)

Dataset 1: https://www12.statcan.gc.ca/census-recensement/2016/dp-pd/dt-td/Rp-eng.cfm?TABID=1&LANG=E&A=R&APATH=3&DETAIL=0&DIM=0&FL=A&FREE=0&GC=01&GL=-1&GID=1341679&GK=1&GRP=1&O=D&PID=110523&PRID=10&PTYPE=109445&S=0&SHOWALL=0&SUB=0&Temporal=2017&THEME=122&VID=0&VNAMEE=&VNAMEF=&D1=0&D2=0&D3=0&D4=0&D5=0&D6=0

Dataset 2: https://www12.statcan.gc.ca/census-recensement/2016/dp-pd/dt-td/Rp-eng.cfm?TABID=2&Lang=E&APATH=3&DETAIL=0&DIM=0&FL=A&FREE=0&GC=0&GID=1235625&GK=0&GRP=1&PID=110270&PRID=10&PTYPE=109445&S=0&SHOWALL=0&SUB=0&Temporal=2016&THEME=119&VID=0&VNAMEE=&VNAMEF=&D1=0&D2=0&D3=0&D4=0&D5=0&D6=0

Task 1
-----------------------------------------------------------------------------------------------------------------

Task 1: Download and Ingest the following datasets in a data store of your choice

1.1) Setup a NoSQL (MongoDB) server on a cloud AWS shared server using MongoDB Atlas

1.2) Python PyMongo module installed, MongoDB Compass (Database client) installed

1.3) In ETLscripts/auxilary/Connect_to_mongoDB.py, set up connection to the cluster, stored connection string in .env in .gitignore

1.4) In ETLscripts/Load_from_csv_to_staging.py, read the two datasets using pandas, create a staging database, create the two dataset tables, and insert the records into the staging database tables

1.5) In ETLscripts/Load_from_staging_to_target.py, read the two datasets from the staging database, do transformations on the "total aboriginal", "aboriginal", and "non-aboriginal" columns value where the values are non numeric, convert them to NaN using pandas, create the target database with the two dataset tables, and insert the records


Task 2
-----------------------------------------------------------------------------------------------------------------

Task 2: Using Dataset 1, using any programming language, calculate and store the following metrics by Canadian regions based on the “Four-Region Model”

2.1) In queries/auxilary/Get_province_list.py, a four region function was implemented the takes a region and returns the corresponding province list

2.2) In queries/auxilary/Settings.py, a the long value columns string were stored in variables for ease of reading

2.3) In queries/auxilary/Read_from_target_db.py, connection to the server is established, query dataset 1 from the target database, and remove the first two columns created by MongoDB

a) In queries/auxilary/Get_aboriginal_proportions.py, proportion of population by “Aboriginal Identity” and “Non-Aboriginal Identity” was implemented

b) In queries/auxilary/Get_average_total_income.py, average Total Income for “Aboriginal Identity” and “Non-Aboriginal Identity” was implemeted

c) In queries/auxilary/Get_proportion_of_gender.py, proportion of male vs. female population by “Aboriginal Identity” and “Non-Aboriginal Identity” was implemented 

d) In queries/auxilary/Get_max_aboriginal_age_group.py, age group with most number of individuals with “Aboriginal identity” was implemented

2.4) In queries/main.py, loop through the regions array and run all the query functions (the app was designed at first to accept one region at a time), output all print statements to output.txt in queries folder

