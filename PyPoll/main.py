#n.b. This is the PyPoll script.
import os
import csv

csvpath = os.path.join ('Resources', 'election_data.csv')

with open(csvpath, newline='') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #Tell it there's a header to contend with
    header = next(csvreader)

    #sets "votecount" as an integer
    votecount = 0
    
    #sets "votelist" as a list
    votelist = []

    #sets "tallies" as a library
    tallies = {}

    for row in csvreader:
        votelist.append(row[2])

        tallies[str(row[2])] = tallies.get(str(row[2]), 0) + 1

    votecount = len(votelist)

#sets descend_val as a dictionary
descend_val = {}



for k in sorted(list(tallies.values()), reverse=True):
    descend_val[dict(zip(tallies.values(), tallies.keys()))[k]] = k

linebreak = "-----------------------------------"

#print to terminal
print('\033[1m' + "Election Results" + '\033[0m')
print(linebreak)
print(f"Total Votes: {str(votecount):>8}")
print(linebreak)

for k in descend_val:
    print(f"{k:>8}: {round(((tallies[k]/votecount)*100),2):>8}% ({tallies[k]} votes)")

print(linebreak)

candlist=[]
candlist = list(descend_val.keys())

winner = candlist[0]
print(f"Winner: {winner:>8}")

print(linebreak)

#print to file - https://stackoverflow.com/questions/13794873/how-to-export-all-print-to-a-txt-file-in-python

import sys

sys.stdout = open('Vote_report.txt', 'w')

print("Election Results:")
print(linebreak)
print(f"Total Votes: {str(votecount):>8}")
print(linebreak)

for k in descend_val:
    print(f"{k:>8}: {round(((tallies[k]/votecount)*100),2):>8}% ({tallies[k]} votes)")

print(linebreak)

candlist=[]
candlist = list(descend_val.keys())

winner = candlist[0]
print(f"Winner: {winner:>8}")

print(linebreak)

sys.stdout.close()