# 1
numbers = [34, 7, 23, 32, 5, 62]
min_number = numbers[0]

for number in numbers:
  if number < min_number:
    min_number = number

print(min_number)

# 2 
numbers = [34, 7, 23, 32, 5, 62]
max_number = numbers[0]

for number in numbers:
  if number > max_number:
    max_number = number

print(max_number)

# 3
my_list = [11, 22, 33, 44, 55, 66]

extracted_elements = [my_list[1], my_list[2], my_list[3], my_list[5]]
print(extracted_elements)


# 4
list1 = ["hello", "world", "how", "are", "you"]
list2 = [1, 2, 3, 4, 5,]

combined_line = []

shorter_box = min(len(list1), len(list2))


for i in range(shorter_box):
  combined_line.append(list1[i])
  combined_line.append(list2[i])

print(combined_line)

# 5 
my_list = ["apple", "banana", "cherry", "1", "2", "3"]

num_list = []
string_list = []

for x in my_list:
  if x.isdigit():
    num_list.append(int(x))
  else:
    string_list.append(x)

print(num_list)
print(string_list)

# 6
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

sum_of_evens = 0
sum_of_odds = 0

combined_list = list1 + list2

for num in combined_list:
  if num % 2 == 0:
    sum_of_evens += num
  else:
    sum_of_odds += num

print(sum_of_evens)
print(sum_of_odds)

# 7
list1 = [1, 4, 7, 9]
list2 = [2, 5, 8, 10]

even_number = []
odd_number = []

for num in list1 + list2:
  if num % 2 == 0:
    even_number.append(num)
  else:
    odd_number.append(num)

print(even_number)
print(odd_number)

# 8
string_list = ["apple", "banana", "cherry"]
lenght_list = []

for string in string_list:
  curent_lenght = 0
  for char in string:
    curent_lenght += 1
  lenght_list.append(curent_lenght)

print(lenght_list)

# 9 
lists = [
  [1, "hello ", 2],
  ["world ", 3, 4],
  [5, "python", 6]
]

all_integers = []
concatenated_strings = ""

for lst in lists:
    for item in lst:
        if isinstance(item, int):
            all_integers.append(item)
        elif isinstance(item, str):
            concatenated_strings += item

print(all_integers)
print(concatenated_strings)

# 10
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_index_list = []

for x in range(0, len(my_list), 2):
  even_index_list.append(my_list[x])

print(even_index_list)








