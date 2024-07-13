# 1
numbers = [1,2,3,4,5]
print(numbers.pop(-1))

# 2 
letter_list = ["A", "B", "C", "D"]
print(letter_list.pop(0))

# 3
names = ["Nika", "Ana", "Giorgi", "Loki"]
names.pop(2)
print(names)

# 4 
my_tuple = ("apple", "banana", "cherry", "kiwi")
print(f"Original tuple: {my_tuple}")

# Using list
# Convert the tuple to a list
tuple_list = list(my_tuple)

# Remove and print the last element from the list
print(f"Removed element: {tuple_list.pop()}")

# Using tuple
# Convert the list back to a tuple
new_tuple = tuple(tuple_list)
print(f"After removing last element from tuple: {new_tuple}")




# 5 
my_list = []
print(my_list.pop()) # IndexError: pop from empty list

# Using if statement
if my_list:
  element = my_list.pop()
  print(f"Removed element: {element}")
else:
  print("List is empty, cannot pop")

# Using len()
if len(my_list) > 0:
  element = my_list.pop()
  print(f"Removed element: {element}")
else:
  print("List is empty, cannot pop")



