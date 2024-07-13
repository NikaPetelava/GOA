# 1 
number = [1,5,8,10,15]
print(max(number))

# 2
fruits = ["apple", "banana", "Kiwi"]
longest_string = max(fruits)

print(longest_string)

# 3
age = [10,20,30,40]
olders_person = max(age)

print(olders_person)

# 4
numbers = [1,2,3,4,5]
max_number = numbers[0]

for number in numbers:
  if max_number < number:
    max_number = number

print(max_number)


