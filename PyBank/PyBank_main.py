# Import the os module and module for reading CSV files
import os
import csv

# Define a function to stream to the standard output (print) and to a output file specified below
outpath = os.path.join('.', 'output.txt')
def printLog(*args, **kwargs):
    print(*args, **kwargs)
    with open(outpath,'a') as file:
        print(*args, **kwargs, file=file)

#  Define CSV file path and Read CSV input file
csvpath = os.path.join('.', 'Resources', 'budget_data.csv')
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip the header)
    csv_header = next(csvreader)

    # Initialize working variables
    count = 0
    total = 0
    max_increase = ['', '0']
    max_decrease = ['', '0']

    # Read each row of data after the header
    for row in csvreader:
        if count == 0:
            first = int(row[1])
        count = count + 1
        total = total + int(row[1])
        if int(row[1]) > int(max_increase[1]):
            max_increase = row
        elif int(row[1]) < int(max_decrease[1]):
            max_decrease = row

last = int(row[1])
average_change = format((last - first) / count, ",.2f")

# Generate the report to the console and the output file

printLog("Financial Analysis")
printLog("----------------------------")
printLog(f"Total Months: {count}")
printLog(f"Total: ${total}")
printLog(f"Average Change: ${average_change}")
printLog(f"Greatest Increase in Profits: {max_increase[0]} (${max_increase[1]})")
printLog(f"Greatest Increase in Profits: {max_decrease[0]} (${max_decrease[1]})")
