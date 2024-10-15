# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast
can_name = None
votes = 0
name =None
percentage_votes = 0

# Define lists and dictionaries to track candidate names and vote counts
candidates_name=[]
can_votes ={}

# Winning Candidate and Winning Count Tracker
winning_Can = None

# Open the CSV file and process it
with open(file_to_load,encoding='utf-8') as election_data:
    reader = csv.reader(election_data, delimiter=',')

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
        print(". ", end="")

        # Increment the total vote count for each row
        total_votes += 1

        # Get the candidate's name from the row
        can_name = row[2]
        # If the candidate is not already in the candidate list, add them
            # notes: I only see a need to create a candidates name list if we had a seperate csv file with a list of names. Since we are using the same CSV file the candiate dictionary is capturing all the names. 
        if can_name not in candidates_name:
            candidates_name.append(can_name)
        # Add a vote to the candidate's count
        
        if can_name not in can_votes:
           can_votes[can_name] = 0
        else:
            can_votes[can_name] += 1   
    
    print('.') # Start results on next line after the loading indicator.
        
    winning_Can =max(can_votes, key=can_votes.get)
                 
    header = 'Election Results'
    line = '------------------------'

# Open a text file to save the output
with open(file_to_output, "w",newline="") as text_file:
    writer = csv.writer(text_file)
    writer.writerow([header])
    print(header)
    writer.writerow([line])
    print(line)
    writer.writerow([f'total Vote Count: {total_votes}'])
    print(f'Total Vote Count:{total_votes}')
    writer.writerow([line])
    
    for can_name, votes in can_votes.items():
        percentage_votes=(votes/total_votes)*100
        writer.writerow([f'{can_name}: {percentage_votes:.3f}% ({votes})'])
        print(f'{can_name}: {percentage_votes:.3f}% ({votes})')
    writer.writerow([line])
    writer.writerow([f'Winner: {winning_Can}'])
    print(f"Winner: {winning_Can}")
  
