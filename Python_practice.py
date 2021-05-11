counties = ["Arapahoe", "Denver", "Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])

counties = ["Arapahoe", "Denver", "Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not in the list of counties.")

if "Arapahoe" not in counties and "El Paso" not in counties:
    print("Arapahoe and El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")

for county in counties:
    print(county)

numbers = [0, 1, 2, 3, 4]
for num in numbers:
    print(num)

for num in range(3):
    print(num)

# Iterate through the counties list using the range() function.
for i in range(len(counties)):
    print(counties[i])

# Iterate over a dictionary and get all the keys.
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties_dict:
    print(county)

# Use .keys() method
for county in counties_dict.keys():
    print(county)

# Iterate over a dictionary and get all the values.
for voters in counties_dict.values():
    print(voters)

# Reference the value of a key by using the format dictionary_name[key].
for county in counties_dict:
    print(counties_dict[county])

# Get the values of a key using get() method.
for county in counties_dict:
    print(counties_dict.get(county))

# Get the Key-Value Pairs of a Dictionary.
for county, voters in counties_dict.items():
    print(county, voters)

# SKILL DRILL: Print each county and registered voter from the counties dictionary.
# My code
for county, voters in counties_dict.items():
    print(county, ' county has', voters, ' registered voters.')

# Their code
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")

# To print each dictionary in voting_data, use the standard format for iterating over the list of dictionaries with a for loop.
voting_data = [{"county": "Arapahoe", "registered_voters": 422829},
               {"county": "Denver", "registered_voters": 463353},
               {"county": "Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

# Use the range() function to iterate over the list of dictionaries and print the counties in voting_data.
for i in range(len(voting_data)):
    print(voting_data[i])

# Get the Values from a List of Dictionaries
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

# Retrieve the number of registered voters from each dictionary.
for county_dict in voting_data:
    print(county_dict['registered_voters'])

# Print the county name from each dictionary.
for county_dict in voting_data:
    print(county_dict['county'])

# F STRINGS: Formatted String Literals
# Original code
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes)+"% of the total votes.")

# Edit with f string
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
print(f"I received {my_votes / total_votes * 100}% of the total votes.")

# Using F-Strings with Dictionaries
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

# Multiline F-Strings
candidate_votes = int(
    input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100}% of the total votes.")

print(message_to_candidate)

# Format Floating-Point Decimals
# General format: f'{value:{width}.{precision}}'
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

# SKILL DRILL: Print each county and registered voter from the dictionary.
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county, value in voting_data.items():
    print(f"{county} county has {voters} registered voters.")
