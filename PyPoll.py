# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who recieved votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

# Import the datetime class from the datetime module.
#import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
#now = dt.datetime.now()
# Print the present time.
#print("The time right now is ", now)

# Add our depedencies.
import csv
import os
# Assign a variable for the file that references the path to load the file.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter
total_votes = 0

# Declare a new list
candidate_options = []
# Declare the empty dictionary.
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file, using the with statement to read the file.
with open(file_to_load) as election_data:
    # To do: Read the data and perform analysis here.
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes += 1
        # Print the candidate name from each row
        candidate_name = row[2]

        # Add the candidate name to the candidate list.
        # candidate_options.append(candidate_name)

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

# Determine the percentage of votes for each candidate by looping through the counts.
# Iterate through the candidate list.
for candidate_name in candidate_votes:
    # Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100

    # To do: print out each candidates name, vote count and percentage of votes to the terminal.

    # Determine winning vote count and candidate
    # Determine if the votes is greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # If true then set winning_count = votes and winning_percent = vote percentage.
        winning_count = votes
        winning_percentage = vote_percentage
        # And, set the winning_candidate equal to the candidate's name.
        winning_candidate = candidate_name

    # To do: Print the winning_candidate, vote count and percentage to the terminal.
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)

#print(f"{candidate_name}: received {vote_percentage}% of the vote.")

# Print the candidate vote dictionary.
# print(candidate_votes)

# Print the candidate list.
# print(candidate_options)

# 3. Print the toal votes.
# print(total_votes)


# Using the with statement, open the file as a text file.
# with open(file_to_save, "w") as txt_file:

##txt_file.write("Counties in the Election\n--------------------------\n")

# 1 way: Write three counties to the file.
# txt_file.write("Arapahoe, ")
# txt_file.write("Denver, ")
# txt_file.write("Jefferson")

# 2nd way: Write three counties to the file.
# txt_file.write("Arapahoe, Denver, Jefferson")

# 3rd way: If we want to write each county on a separate line, we need to add the newline escape sequence to the end of each county name.
# The newline escape sequence is the letter "n" preceded by the backward slash like this: \n.
# txt_file.write("Arapahoe\nDenver\nJefferson")
