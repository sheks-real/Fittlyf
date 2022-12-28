#a custom exception class to handle IndexError and ValueError:
# Create a custom exception class named MyException
class MyException(Exception):
  def __init__(self, message):
    self.message = message

# Define the list of items
list_a = [1, 2, 3, 4, 5]

# Read the index from the user
index = input("Enter the index = ")

try:
  # Convert the index to an integer
  index = int(index)
  
  # Check if the index is within the bounds of the list
  if index < -len(list_a) or index >= len(list_a):
    # If the index is out of bounds, raise a custom exception
    raise MyException("The index {} is incorrect and index should lie between {} and {}.".format(index, -len(list_a), len(list_a)-1))
  else:
    # If the index is within bounds, print the element at the index
    print("The element at index {} is {}.".format(index, list_a[index]))

except ValueError:
  # If the index is not a valid integer, print an error message
  print("Use an Integer value as the input.")

except MyException as e:
  # If the index is out of bounds, print the custom error message
  print(e.message)



