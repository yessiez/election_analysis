print("Hello World")

counties = ["Arapahoe", "Denver", "Jefferson"]

'To declare an empty list'
'my_list = []'
'my_list = list()'

'To confirm that this list is declared.'
print(counties)

'To get the first item in the counties list in the terminal.'
counties[0]

'To print the county to the screen.'
print(counties[2])

'To find the last item in the counties list, use negative indexes.'
print(counties[-1])

'To find the second-to-last item in a list.'
print(counties[-2])

'To find the length of a list.'
print(len(counties))

'''Slicing is used to get specific items from a list.
Format: list[start:end]
1. The start refers to the index of the first item in the slice.
2. the end is the index marking the end of the slice.
3. the espression list[start:end] returns a list containing a copy of the items in the list from the starting index value up to, but not including the ending index value.'''

'To find the first and second items from the counties list'
print(counties[0:2])
print(counties[:2])

'To print second to last counties'
print(counties[1:])

'To print the first item from the list'
print(counties[0:1])

'To add items to a list'
'Using the append() function on a list will always add the new item at the end of the list'
counties.append("El Paso")
print(counties)

'''To specify where in a list to add a new item, select the location with an index by using the following syntax, list.insert(index, obj).
index represents where we would like the new item to be placed.
obj represents the item.'''

'Add another instance of "El Paso" at index two'
counties.insert(2, "El Paso")
print(counties)

'To remove an instance of "El Paso from our list, we append the .remove method and specify the list item were removing.'
counties.remove("El Paso")
print(counties)

'''Another method to remove items from a list
pop() method removes the item at a given index from the list and then returns the removed item.
To remove the last instance of "El Paso" using the pop(method)'''
counties.pop(3)
print(counties)

'To change an element in a list, use the syntax list[index] on the left side of the equals sign; on the right side, you assign the index a new data value.'
'Change Jefferson county to El Paso'
counties[2] = "El Paso"
print(counties)

'Original couties list'
counties = ["Arapahoe", "Denver", "Jefferson"]
print(counties)

'Add El Paso to the second position in the list.'
counties.insert(1, "El Paso")
print(counties)

'Remove Arapahoe from the list.'
counties.remove("Arapahoe")
print(counties)

'Make Denver the third item in the list, but eep Jefferson the second item in the list.'
counties.insert(3, "Denver")
counties.pop(1)
print(counties)

'Add Arapahoe to the list.'
counties.append("Arapahoe")
print(counties)

counties = ["Arapahoe", "Denver", "Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])

counties = ["Arapahoe", "Denver", "Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

'''You can create an empty tuple with the following syntax:
my_tuple = ( )

Alternatively, you can use the built-in tuple() method:
my_tuple = tuple()'''

counties_tuple = ("Arapahoe", "Denver", "Jefferson")
print(counties_tuple)

'To get the length of tuple.'
print(len(counties_tuple))

'To get an item from a tuple, we can apply indexing and slicing, using square brackets after the tuple, just like with lists.'
print(counties_tuple[1])
print(counties_tuple[:-1])


'''The syntax for a dictionary is the key followed by a colon, which is followed by a value: {key:value}.
To initialize or create an empty dictionary, we use the following syntax: my_dictionary = {}. Or you can create a dictionary with the built-in Python dict() method, my_dictionary = dict().

Let's create a dictionary with the counties as keys and the number of registered voters of each county as values.
Create the empty counties dictionary'''
counties_dict = {}

'Add the county "Arapahoe" to the dictionary as the key and the number of registered voters for Arapahoe as the values for this key.'
counties_dict["Arapahoe"] = 422829

'Add the counties "Denver" and "Jefferson" with their respective number of registered voters.'
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
print(counties_dict)

'Get the length of dictionary'
print(len(counties_dict))

'''To get all the keys and values printed to the screen, simply print the dictionary name.
Or, we can use the items() method on the dictionary.
This will return a list of tuples where the first element in each tuple is the key of the dictionary, and the second element in each tuple is the value corresponding to that key.
If we add the items() method to the end of counties_dict, we'll get this output:'''
print(counties_dict.items())

'To get only the keys from a dictionary.'
print(counties_dict.keys())

'To retrieve values from a dictionary.'
print(counties_dict.values())

'To get a specific value from a dictionary.'
print(counties_dict.get("Denver"))

'To get the number of registered voters in Arapahoe County, we can also wrap the key in brackets using this format: dictionary_name[key].'
print(counties_dict['Arapahoe'])

voting_data = []
voting_data.append({"county": "Arapahoe", "registered_voters": "422829"})
voting_data.append({"county": "Denver", "registered_voters": "463353"})
voting_data.append({"county": "Jefferson", "registered_voters": "432438"})
print(voting_data)

print(len(voting_data))


'Add the new county “El Paso” and its registered voters, 461149, to the second position in voting_data.'
voting_data.insert(1, {"county": "El Paso", "registered_voters": "461149"})
print(voting_data)

# Remove “Arapahoe” and its registered voters from voting_data.
voting_data.remove({"county": "Arapahoe", "registered_voters": "422829"})
print(voting_data)

# Make “Denver” and its registered voters the third item in voting_data, but keep “Jefferson” and its registered voters as the second item.
voting_data.insert(3, {"county": "Denver", "registered_voters": "463353"})
voting_data.pop(1)
print(voting_data)

# Add “Arapahoe” and its registered voters to voting_data.
voting_data.append({"county": "Arapahoe", "registered_voters": "422829"})
print(voting_data)

if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")


if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso are not in the list of countries.")

'''while loops test if a condition is true. If the condition is true, then the code will perform a task. This type of loop has two parts:
A condition that is tested for a true or false value.
A statement or statements that are repeated as long as the condition is true.
x = 0
while x <= 5:
    print(x)
    x = x + 1

# for loops iterate, or run through, a program a specific number of times before it stops. A for loop can be written like if and if-else statements. Here's the general format:
for item in [items]:
    statement 1
    statement 2'''

for county in counties:
    print(county)

# range(), that simplifies the process of writing a for loop.
# The range() function creates an iterable object or a list.
# for loop
numbers = [0, 1, 2, 3, 4]
for num in numbers:
    print(num)

# for loop with range().
numbers = [0, 1, 2, 3, 4]
for num in range(5):
    print(num)

# to iterate through the counties list using the range() function
for i in range(len(counties)):
    print(counties[i])


# to get only the keys from a dictionary using a for loop
for county in counties_dict:
    print(county)
counties = ["Arapahoe", "Denver", "Jefferson"]
if "Arapahoe" in counties:
    print("True")
else:
    print("False")

counties = ["Arapahoe", "Denver", "Jefferson"]
if "El Paso" not in counties:
    print("True")
else:
    print("False")

# to get only the keys from a dictionary using a for loop
for county in counties_dict:
    print(county)
