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
    candidate_list.sort() #sort the list for forms sake; https://thispointer.com/python-how-to-sort-a-list-of-strings-list-sort-tutorial-examples/

    cand0 = candidate_list[0]
    cand1 = candidate_list[1]
    cand2 = candidate_list[2]
    cand3 = candidate_list[3]
    cand4 = "Russian Troll Farm"

    #Count some votes!
    cand0_count = votelist.count(cand0)
    cand1_count = votelist.count(cand1)
    cand2_count = votelist.count(cand2)
    cand3_count = votelist.count(cand3)
    cand4_count = votelist.count(cand4)

    #Calculate the vote percentages!
    cand0_pct = int((cand0_count / votecount) * 100)
    cand1_pct = int((cand1_count / votecount) * 100)
    cand2_pct = int((cand2_count / votecount) * 100)
    cand3_pct = int((cand3_count / votecount) * 100)
    cand4_pct = int((cand4_count / votecount) * 100)

    #and find our winner.

    win_votes = 0
    winner = "Null"

    if cand0_count > win_votes:
        win_votes = cand0_count
        winner = cand0

    if cand1_count > win_votes:
        win_votes = cand1_count
        winner = cand1

    if cand2_count > win_votes:
        win_votes = cand2_count
        winner = cand2
    
    if cand3_count > win_votes:
        win_votes = cand3_count
        winner = cand3

    if cand4_count > win_votes:
        win_votes = cand4_count
        winner = cand4

    #Print the return.
    line1 = "Poll Results"
    print('\033[1m' + line1 + '\033[0m')
    linebreak = "-------------------------------------"
    print(linebreak)
    line2 = "Total Votes: " + str(votecount)
    print(line2)
    print(linebreak)
    line3 = "1 - " + str(cand0) + " (Votes: " + str(cand0_count) + ", " + str(cand0_pct) + "%)"
    print(line3)
    line4 = "2 - " + str(cand1) + " (Votes: " + str(cand1_count) + ", " + str(cand1_pct) + "%)"
    print(line4)
    line5 = "3 - " + str(cand2) + " (Votes: " + str(cand2_count) + ", " + str(cand2_pct) + "%)"
    print(line5)
    line6 = "4 - " + str(cand3) + " (Votes: " + str(cand3_count) + ", " + str(cand3_pct) + "%)"
    print(line6)
    line7 = "5 - " + str(cand4) + " (Votes: " + str(cand4_count) + ", " + str(cand4_pct) + "%)"
    print(line7)
    print(linebreak)
    line8 = "Winner: " + str(winner)
    print(line8)
    print(linebreak)

    #Export the Return to a .txt file
    #learned it here: https://www.geeksforgeeks.org/reading-writing-text-files-python/

    file1 = open("Vote_report.txt", "w")
    L = [line1 + "\n", 
        linebreak + "\n",
        line2 + "\n", 
        linebreak + "\n",
        line3 + "\n", 
        line4 + "\n", 
        line5 + "\n",
        line6 + "\n",
        line7 + "\n",
        linebreak + "\n",
        line8 + "\n",
        linebreak + "\n"
        ]
    file1.writelines(L)
    file1.close()