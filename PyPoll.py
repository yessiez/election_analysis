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

# Open the election results and read the file, using the with statement to read the file.
with open(file_to_load) as election_data:
    # To do: Read the data and perform analysis here.
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes += 1

# 3. Print the toal votes.
print(total_votes)


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
