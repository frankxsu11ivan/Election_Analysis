# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""
#Open the data file.
#Write down the names of all the candidates.A complete list of candidates who received votes
#Write down the names of all the candidates. A complete list of candidates who received votes
#Add a vote count for each candidate.
#Total number of votes cast
#Get the total votes for each candidate.
#Get the total votes cast for the election.
#Percentage of votes each candidate won
#The winner of the election based on popular vote
#3.3.2 Total number of votes cast
#3.3.2 Get the total votes for each candidate.
#3.3.2 Get the total votes cast for the election.
#3.3.2 Percentage of votes each candidate won
#3.3.2 The winner of the election based on popular vote
#voter turnout for each county
#percentage of votes from each county out of the total count
#county with the highest turnout
# Add our dependencies.
import csv
import os

#Ching GOw
#Narritive. use for loops and conditional statements with membership and logical operators to find the requested results. 
#Deliverable 1: The Election Results Printed to the Command Line
#Deliverable 2: The Election Results Saved to a Text File election_results.txt file.

print('Hello World')
# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
###Step 2
#3.2.7 Create and add Keys and values to a Dictionary
#initialize empty list for 
#3.2.7 Create and add Keys and values to a dictionary
    #initialize empty list for 
# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

# 1: Create a county list and county votes dictionary.



# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#na. it only printed the string, not the dict.
    #na. it only printed the string, not the dict.

# 2: Track the largest county and county voter turnout.
#To get all the keys and values printed to the screen, simply print the dictionary name. 
    #To get all the keys and values printed to the screen, simply print the dictionary name.


# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
#run and well --- nope. Hmm
##initialize Initialize an empty string, like winning_candidate, 
#that will hold the county name for the county with the largest turnout.
    #run and well --- nope. Hmm
        ##initialize Initialize an empty string, like winning_candidate, 
        #that will hold the county name for the county with the largest turnout.

        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.


            # 4b: Add the existing county to the list of counties.


            # 4c: Begin tracking the county's vote count.
            #3.2.11 Write print statements using f-strings
                #When writing an algorithm that performs the same task over and over, 
                #it's a lot easier to write the code for the algorithm once, 
                #and then place that algorithm in a repetition structure 
                #that can be repeated as many times as necessary.
                #this will be required for the RTM.
                    #for loops == a req uired number of times.
                    #while loops uses a T/F condition 
                        #X=0
                        #while x,=5:
                        #print(x)
                        #x=x+1

        # 5: Add a vote to that county's vote count.

#3.2.9 apply Membership and local operators to decision statements
    #Ok`...not sure why this is here. or how to tell if this works. 
    #Does this list need to be zeroed out?
    #Hmm...nope . no output 3.2.7

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")

    txt_file.write(election_results)

    # 6a: Write a for loop to get the county from the county dictionary.

        # 6b: Retrieve the county vote count.

        # 6c: Calculate the percentage of votes for the county.


         # 6d: Print the county results to the terminal.

         # 6e: Save the county votes to a text file.

         # 6f: Write an if statement to determine the winning county and get its vote count.


    # 7: Print the county with the largest turnout to the terminal.


    # 8: Save the county with the largest turnout to a text file.
    ##How many votes did you get? thinking to add candidate names here.
    #my_votes = int(input("How many votes did you get in the election? "))
    #Total votes in the election
    #total_votes = int(input("What is the total votes in the election? "))
    #Calculate the percentage of votes you received.
    #Percentage_votes = (my_votes / total_votes) * 100
    #Print("I received " + str(percentage_votes)+"% of the total votes.")
    #3.2.9 Apply Membership and local operators to decision statements
    #Deleverable operators == < > =
        #Could also use if-else statement
            #if condition:
                #  statement 1
                #  statement 2
            #else:
                #   statement 1
                #   statement 2

    # Save the final candidate vote count to the text file.
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the
        # terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
