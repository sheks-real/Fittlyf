"""
Create a tuple t_1 = (1, 4, 9, 16, 25, 36).
Square each element of the tuple using tuple comprehension and store the result in a variable known as t_modified
Find element at index position 4 of the tuple t_modified.
Now slice the modified tuple in such a way that the sliced  tuple includes only elements from index position 1 to 3 and store this sliced tuple in a variable known as t_sliced. 
"""
t_1 = (1, 4, 9, 16, 25, 36)


t_modified = tuple(i**2 for i in t_1)


element_at_index_4 = t_modified[4]

#  sliced tuple includes only elements from index position 1 to 3
t_sliced = t_modified[1:4]

print("t_1:", t_1)
print("t_modified:", t_modified)
print("Element at index postiion 4 of t_modified:", element_at_index_4)
print("t_sliced:", t_sliced)
