# A list is an array that contains multiple data items, like the following list of counties.
counties = ["Arapahoe", "Denver", "Jefferson"]

# Use indexing and slicing to retreive specific items from the list.
counties[2]
print(counties[2])

# Negative indexes are used to identify a list item's position relative to the end of the list
print(counties[-1])

# Add or remove items from a list

# Change the contents in a list

# When we want to add items to a list but the list has not been declared, we must first declare an empty list.

# An empty list can be declared with the following syntax:
# my_list = [ ]

# Alternatively, you can use the built-in function list() to create an empty list:
# my_list = list()

Slicing is used to get specific items from a list. The format for slicing a list is as follows: list[start: end].

Let's break down how slicing works.

The start refers to the index of the first item in the slice.
The end is the index marking the end of the slice.
The expression list[start: end] returns a list containing a copy of the items in the list from the starting index value up to, but not including, the ending index value.
For example, to find the first and second items from the counties list, we type counties[0:2], not counties[0:1].

The output of counties[0:2] will be Arapahoe and Denver, the first and second items from the counties list.

>> > counties[0:2]
['Arapahoe', 'Denver']

Items can be added to an empty list or a list that already exists by using the append() function and the syntax list.append(). In the parentheses, add the data you want, whether integers, floats, strings, or another data type or data structure.
Using the append() function on a list will always add the new item at the end of the list.
To specify where in a list to add a new item, select the location with an index by using the following syntax, list.insert(index, obj).

Here, index represents where we would like the new item to be placed, and obj represents the item.
