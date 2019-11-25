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
# this is written so it works regardless of what the 4 candidates' names actually are. 

    votelist = []
    for row in csvreader:
        votelist.append(row[2])

    votecount = int(len(votelist))
    candidates = set(votelist)
    candidate_list = list(candidates)
    #cand1 = "Null"
    #cand2 = "Null"
    #cand3 = "Null"
    #cand4 = "Russian Troll Farm"
    #cand0 = "Null"

    cand0 = candidate_list[0]
    cand1 = candidate_list[1]
    cand2 = candidate_list[2]
    cand3 = candidate_list[3]
    cand4 = "Russian Troll Farm"

    #Prepare to count some votes. 
    cand0_count = votelist.count(cand0)
    cand1_count = votelist.count(cand1)
    cand2_count = votelist.count(cand2)
    cand3_count = votelist.count(cand3)
    cand4_count = votelist.count(cand4)

    print(cand0)
    print(cand0_count)
    print(cand1)
    print(cand1_count)
    print(cand2)
    print(cand2_count)
    print(cand3)
    print(cand3_count)
    print(cand4)
    print(cand4_count)
    

