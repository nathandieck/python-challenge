#n.b. This is the PyPoll script.

import os
import csv

csvpath = os.path.join ('Resources', 'election_data.csv')

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
   
    #Tell it there's a header to contend with

    header = next(csvreader)

# populate the candidate's names

    votelist = []
    for row in csvreader:
        votelist.append(row[2])

    votecount = int(len(votelist))
    
    candidates = set(votelist)

    print(candidates)
    print (votecount)
    


