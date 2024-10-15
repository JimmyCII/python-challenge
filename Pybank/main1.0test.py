# -*- coding: UTF-8 -*-
"""PyBank Homework main file."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
budget_data_csv =os.path.join("Resources", "budget_data.csv")
budget_analysis_txt = os.path.join("analysis","budget_analysis.txt")  

# Define variables to track the financial data
total_months = 0
total_net = 0

# Add more variables to track other necessary financial data
net_change_list =[]  #each time we go throuth the loop cal dif and add it to the distionary. 
net_change= 0
avg_change = 0
previous_value = 0
greatest_inc_profit= 0
greatest_inc_profit_Month = None
greatest_dec_profit= 0
greatest_dec_profit_Month = None
 

# Open and read the csv
with open(budget_data_csv) as budget_data:
    reader = csv.reader(budget_data, delimiter=',')
    header=next(reader) #remove the header row
    #firstvalue =next(reader) # this did not return the correct number of months or total value
    #data = list(reader) # used in main.py
    #previous_value = int(data[0][1]) #used in main.py to set the previous value of the profit/lost
    #print(previous_value)
    # print statements have been added to test variables during the build.  Remove the # to retest.
    #print(previous_value)
    #for row in data:
    for row in reader:
        # add the total number or rows min the header to equal the number of months counted
        total_months += 1
        # add the $ amount in index 1 as it goes through the loop
        total_net += float(row[1])
        #print(row[1]) 
             
        net_change = int(row[1])-previous_value # calculate net change per row based on current row and previous row value. 
        #print(greatest_inc_profit)
        #print(row[1])
    
        if int(row[1]) >= int(greatest_inc_profit):
            greatest_inc_profit = int(row[1])  
            greatest_inc_profit_Month = str(row[0])
        
        if int(row[1]) <= int(greatest_dec_profit):
            greatest_dec_profit = int(row[1])
            greatest_dec_profit_Month = str(row[0])
        previous_value = int(row[1]) # set previous_value to new row
        net_change_list +=[net_change] # add net_change to the net_change_list
    net_change_list.pop(0)
    #print(net_change_list)
        
    avg_change = sum(net_change_list)/len(net_change_list)

    output = f'Financial Analysis\n ---------------------------\n Total Months: {total_months}\n Total: {total_net}\n Avarage Change: {avg_change}\n Greatest Increase in Profit: {greatest_inc_profit_Month} {greatest_inc_profit}\n Greatest Decrease in Profit: {greatest_dec_profit_Month} {greatest_dec_profit}'
    financial_analysis ="finanical_analysis_test.txt"

   
    output_path= os.path.join("Resources", "financial_analysis_test.txt")
    with open('financial_analysis_test.txt', "w") as file:
        file.write(output) 
        
    print(f"{output}")

     
