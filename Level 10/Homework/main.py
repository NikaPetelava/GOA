# Homework #6
    #Option #1
for num1 in range(101):
  for num2 in range(101):
    addition = num1 + num2
    print(addition)

    substraction = num1 - num2
    print(substraction)

    multiplication = num1 * num2
    print(multiplication)

    if num2 != 0:
      division = num1 / num2
      print(division)

    #Option #2
for i in range(101):
    addition = i + 10 
    subtraction = i - 5  
    multiplication = i * 2  
    division = i / 3
    print(i)
    print(addition)
    print(subtraction)
    print(multiplication)
    print(division)


# Homework #7
user_number = int(input("Enter a Number: "))
total_sum = 0

for number in range(1, user_number):
  total_sum += number

print("The sum of all numbers is:", total_sum)

# Homework #8
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

for i in range(2):
    addition = num1 + num2
    print(addition)

    multiplication = num1 * num2
    print(multiplication)

