#n.b. This is the PyBank script. 

import os
import csv

csvpath = os.path.join('Resources','budget_data.csv')

#This comes from the read_csv.py class exercise.

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
   
    #Tell it there's a header to contend with

    header = next(csvreader)

    #Set the requested variables as integers and strings
    
    months = 0
    profit = 0
    average = 0
    big_gain = 0
    gain_month = "Null"
    big_loss = 0
    loss_month = "Null"

    #do the math
    for row in csvreader:

        #calculate the number of months
        months = months + 1

        #calculate the net profit
        profit = profit + int(row[1])

        #calculate the month and amount of the largest gain
        if big_gain < int(row[1]):
            big_gain = int(row[1])
            gain_month = str(row[0])
        
        #and the largest loss. 
        if big_loss > int(row[1]):
            big_loss = int(row[1])
            loss_month = str(row[0])

    #calculate the average change

    average = profit / months
    
    #print it all
    #learned how to bold text here: https://stackoverflow.com/questions/8924173/how-do-i-print-bold-text-in-python
    
    print('\033[1m' + "Financial Analysis")
    print('\033[0m' + "----------------------------")
    print(f"Total Months: {str(months)} months")
    print(f"Total Profit: ${str(profit)}")
    print(f"Average Monthly Change: ${str(int(average))}")
    print(f"Biggest Gain: {str(gain_month)} (${str(big_gain)})")
    print(f"Biggest Loss: {str(loss_month)} (${str(big_loss)})")