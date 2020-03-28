# Import the os module and module for reading CSV files
import os
import csv

# Define a function to stream to the standard output (print) and to a output file secified below
outpath = os.path.join('.', 'output.txt')
def printLog(*args, **kwargs):
    print(*args, **kwargs)
    with open(outpath,'a') as file:
        print(*args, **kwargs, file=file)

#  Define CSV file path and Read CSV input file
csvpath = os.path.join('.', 'Resources', 'election_data.csv')
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents. Also,skip the header
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    # Initialize working variables
    count = 0
    VoterCandidate = {}

    # Read each row of data after the header
    for row in csvreader:
        count = count + 1
        #print(row[2])
        if row[2] not in list(VoterCandidate.keys()):
            Candidate = {row[2]: 1}
            VoterCandidate.update(Candidate)
        else:
            VoterCandidate[row[2]] = VoterCandidate[row[2]] + 1

# Generate the first parat of the report to the console based on total count only
printLog("Election Results")
printLog("-------------------------")
printLog(f"Total Votes: {count}")
printLog("-------------------------")

# Loop through only candidates with votes, calculate their percentage of total votes, and print final vote tallies
# Additionally, figure out who the winner is by comparing the number of votes each candidate received
votes = 0
for candidate in VoterCandidate:
    candidate_votes_percentage = format(VoterCandidate[candidate] / count * 100, ",.3f")
    printLog(f"{candidate}: {candidate_votes_percentage}% ({VoterCandidate[candidate]})")
    if VoterCandidate[candidate] > votes:
        votes = VoterCandidate[candidate]
        winner = candidate

# Declare the winner at this time and finish the script
printLog("-------------------------")
printLog(f"Winner: {winner}")
printLog("-------------------------")
