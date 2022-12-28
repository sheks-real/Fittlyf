""" 
Write a python program to remove items in a list containing the character 'a' or 'A'. 
Use lambda function for it. For this program pass in as argument the list: 
list_a = ["car", "place", "tree", "under", "grass", "price"] to the lambda function named remove_items_containing_a_or_A.
"""


list_a = ["car", "place", "tree", "under", "grass", "price"]

# Define the lambda function

remove_items_containing_a_or_A = lambda x: 'a' not in x.lower()


new_list = filter(remove_items_containing_a_or_A, list_a)


print(list(new_list))  