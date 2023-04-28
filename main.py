# -------------------------------- TERMINAL INSTALL REQUIREMENTS --------------------------------
# pip install mysql-connector-python

# -------------------------------- IMPORTS --------------------------------
import pandas as pd
import mysql.connector
from datetime import date

# -------------------------------- CONNECT TO MySQL TO RETRIEVE THE DATA FROM THE DATABASE --------------------------------

# Establish the connection:
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database = 'lab_data'
)

# Create a cursor object using the cursor() method
cursor = connection.cursor()

# Receive the data
sql = '''SELECT * FROM chromatography_results'''

# Execute the query
cursor.execute(sql)

# Retrieve the results.  fetchall() method retrieves all the rows in the result set of a query and returns them as a list of tuples
database_data = cursor.fetchall()
print(database_data)

# -------------------------------- LOAD DATA FROM DATABASE INTO DICTIONARY --------------------------------
data_dictionary = {
    'SSID': [],
    'RSID': [],
    'LIMS_ID': [],
    'result': [],
    'time': []
}

for row in database_data:
    # Iterate through each row of data from the SQL database and append it to the data dictionary
    SSID = row[0]
    RSID = row[1]
    LIMS_ID = row[2]
    result = row[3]
    time = row[4]

    data_dictionary['SSID'].append(SSID)
    data_dictionary['RSID'].append(RSID)
    data_dictionary['LIMS_ID'].append(LIMS_ID)
    data_dictionary['result'].append(result)
    data_dictionary['time'].append(time)

# -------------------------------- PUSH THE data_dictionary TO CSV WITH PANDAS --------------------------------
df = pd.DataFrame.from_dict(data_dictionary)
# Make the name of the csv file
today = date.today()
new_filename = f"{today}" + ".csv"

# Create the CSV out of the data frame
df.to_csv(new_filename, index = False, header = True) 
# index = False <-- Makes CSV file without index column
# header = True <-- Sets the headers of the dictionary to the column names of the CSV file

