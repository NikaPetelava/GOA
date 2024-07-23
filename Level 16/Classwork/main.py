# 1
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
sliced_half = fruits[0:3]

print(sliced_half)

# 2
my_list = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
new_list = []

# შევქმენი ახალი ცვლადი რომელიც ინახავს my_lists_ის ჩამოჭროლ ნახევარს apple, banana და cherry_ს 
sliced_half = my_list[:3]

# ჩამოჭრილი სიის ნახევარე რომელიც ინახება ცვლად sliced_half_ში დავამატე ცარიელი სიის ცვლად new_list_ში  exdent მეთოდის მეშვეობით
new_list.extend(sliced_half)

print(new_list)

# 3
my_list = ["a", "b", "c", "d", "e", "f"]


index_0 = my_list.index(my_list[0])
index_1 = my_list.index(my_list[1])
index_2 = my_list.index(my_list[2])

print(f"{index_0}{index_1}{index_2}")

# 4 / 5
my_list = [1, 2, 3, 4, 5]

# შევინახე უმცირესი და უდიდესი რიცხვები ცვლადებში. min/max ფუნქციის მეშვეობით კი ვიპოვე უმცირესი და უდიდესი რიცხვები.
min_number = min(my_list)
max_number = max(my_list)

# remove მეთოდის მეშვეობით უმცირესი და უდიდესი რიცხვები ამოვიღე სიიდან
my_list.remove(min_number)
my_list.remove(max_number)


new_list = [] # შევქმენი ცარიელი სია

# min/max number_ი  დავამატე ცარიელ სიაში append მეთოდის მეშვეობით
new_list.append(min_number)
new_list.append(max_number)

print(f"Original List after removal: {my_list}")
print(f"New List with removed values: {new_list}")

# 6
first_list = [1, 2, 3, 4, 5]
secont_list = [1, 2, 3, 4, 5]

# min/max ფუნქციის მეშვეობით secont_list_ის მაქსიმალურ რიცხვს და first_list_ის მინიმალურ რიცხვს გამოვაკლებთ ერთმანეთს და 
# ჯამს შევინახავ ახალ list_count ცვლადში
list_count = max(secont_list) - min(first_list)

# შევქმენი ცარიელი სია
new_list = []

# ვამატებ list_count ცვლადის ჯამს new_list_ში append მეთოდის მეშვეობით
new_list.append(list_count)

# გამომყავს შედეგი ტერმინალში
print(new_list)

# 7
integer_list = [1, 2, 3, 4, 5]
total_sum = 0

for number in integer_list:
  total_sum += number

print(total_sum)

# 8 
my_list = ["hello", "5", "world", "10", "how", "are", "you", "20"]
num_list = []
string_list = []

for x in my_list:
  if x.isdigit():
    num_list.append(int(x))
  else:
    string_list.append(x)

print(sum(num_list))
print(string_list)


# 9
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

sum_list1 = sum(list1)
sum_list2 = sum(list2)

print(f"The  sum of the integers of list is: {sum_list1}")
print(f"The  sum of the integers of list is: {sum_list2}")