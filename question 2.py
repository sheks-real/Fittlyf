"""
star  printing :
option 1 ->  upside down triangle , option 2 -> upside down triangle continuing with increase
star  line
"""
choice = int(input("Enter your choice (1 or 2): "))

if choice == 2:
  
  for i in range(5):
    print(" " * i + "* " * (5-i))
  for i in range(5):
    print(" " * (4-i) + "* " * (i+1))
elif choice == 1:
  
  for i in range(5):
    print(" " * i + "* " * (5-i))
else:
  print("Invalid Input")
