# 1
cars = []

for x in range(5):
  fav_cars = input("Enter your favorite car: ")
  cars.append(fav_cars)

print(f"Your favorite cars are: {cars}")

# 2
movies = ["The Prestige", "Interstellar", "The Dark Knight", "Oppenheimer"]

print(movies[3])

# 3
random_info = [1, 2.2, True, "nika"]
random_info[1] = 28

print(random_info)

# 4
fav_fruits = ["Banana", "Peach", "Cherry", "Plum", "Strawberry"]
fav_fruits.append("Watermelon")
fav_fruits.remove("Peach")
print(fav_fruits)

# 5
numbers = [1,2,3,4,5,6,7,8,9,10]
# max
max_number = numbers[0]
for number in numbers:
  if max_number < number:
    max_number = number

print(max_number)

# min
min_number = numbers[0]
for number in numbers:
  if min_number > number:
    min_number = number

print(min_number)

# sum 
sum_number = 0

for number in numbers:
  sum_number += number

print(sum_number)

# 6 
name_list = []

 
# შევქმენი ციკლი, რომ მივიღო 5 სახელი მომხმარებლისგან და შევინახო ისინი სიაში  
for i in range(2):
  name = input("Enter your name: ")
  name_list.append(name)

# ითვლის თუ რამდენჯერ გამოჩნდა არჩეული სახელი სიაში
Selected_name = input("Enter the name you want to count: ")
name_count = name_list.count(Selected_name)

# გამომაქვს შედეგი
print(f"Number of times {Selected_name}, is repeated: {name_count}")

# 7 
number_list = [1,2,3,4,5]

number_list.pop(0)
number_list.pop()

print(number_list)

