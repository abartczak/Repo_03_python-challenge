# Import the os module and module for reading CSV files
import os
import csv

# United States of America Python Dictionary to translate States,
# Districts & Territories to Two-Letter codes and vice versa.
# Code copied from https://gist.github.com/rogerallen/1583593
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'District of Columbia': 'DC',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Northern Mariana Islands':'MP',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Palau': 'PW',
    'Pennsylvania': 'PA',
    'Puerto Rico': 'PR',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virgin Islands': 'VI',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

# Specify the file to write to
output_path = os.path.join(".", "employee_data_updated.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfilewrite:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfilewrite, delimiter=',')

    #  Define CSV file path and Read CSV input file
    csvpath = os.path.join('.', 'employee_data.csv')
    with open(csvpath, newline='') as csvfile:

        # CSV reader specifies delimiter and variable that holds contents. Also,skip the header
        csvreader = csv.reader(csvfile, delimiter=',')

        # Update the header to split Name into First and Last Name
        csv_header = next(csvreader)
        csv_header[1] = "First Name"
        csv_header.insert(2,"Last Name")
        csvwriter.writerow(csv_header)

        # Read each row of data after the header and update it as per the requirements
        for row in csvreader:
            # Process each original record to split name, reformat DOB, SS, and state
            new_name = row[1].split(' ', 1)
            row[1] = new_name[0]
            row.insert(2,new_name[1])
            new_dob = row[3].split('-', 2)
            row[3] = new_dob[1] + '/' + new_dob[2] + '/' + new_dob[0]
            new_ss = row[4].split('-', 2)
            row[4] = '***-**-' + new_ss[2]
            row[5] = us_state_abbrev[row[5]]
            
            # Write each record to the updated output file
            csvwriter.writerow(row)

