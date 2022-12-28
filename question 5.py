""" 
Create a frozenset named frozen_set_1 containing the elements: 'A', 'B', 'C' and 'D' 
combine it using union with a frozenset named frozen_set_2 containing elements 'A', 2, 'C' and 4.
The final combined frozenset must be named frozenset_union
Now find the common elements in frozen_set_1 and frozen_set_2 and store the result in a variable named frozenset_common
Lastly, in a new forzenset named forzenset_difference store the elements of frozen_set_1 
which are not in frozen_set_2 and in a new frozenset named frozenset_distinct store the elements which are unique to frozen_set_1 and frozen_set_2.

"""
frozen_set_1 = frozenset(['A', 'B', 'C', 'D'])
frozen_set_2 = frozenset(['A', 2, 'C', 4])


frozenset_union = frozen_set_1 | frozen_set_2


frozenset_common = frozen_set_1 & frozen_set_2

frozenset_difference = frozen_set_1 - frozen_set_2


frozenset_distinct = frozen_set_1 ^ frozen_set_2

print("frozen_set_1:", frozen_set_1)
print("frozen_set_2:", frozen_set_2)
print("frozenset_union:", frozenset_union)
print("frozenset_common:", frozenset_common)
print("frozenset_difference:", frozenset_difference)
print("frozenset_distinct:", frozenset_distinct)
