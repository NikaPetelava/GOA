# Classwork #1
i = 20

while i >= 1:
  print(i)
  i -= 1


# Classwork #2
i = 0

while i <= 10:
  print(i)
  i += 2


# Classwork #3
i = 1
sum = 0

while i <= 10:
  sum += i
  i += 1


# Classwork 4
correct_password = "Nikunikusha@1"
user_input = ""

while correct_password != user_input:
  user_input = input("Enter password: ")

  if user_input == correct_password:
    print("Welcome!")
  else:
    print("Please, try again!")


# Classwork 5
i = 1

while i <= 10:
  print(i)
  i += 1


# Classwork 6
user_age = 1

while user_age <= 18:
  user_age = int(input("How old are you? "))

  if user_age < 18:
    print("You cannot enter the program.")
    break # ციკლიდან გამოსვლა 
  else:
    print("Welcome to the program!")
    break


# Classwork 7
user_input = int(input("Enter your number: "))

if user_input == 1:
  print("Monday")
elif user_input == 2:
  print("Tuesday")
elif user_input == 3:
  print("Wednesday")
elif user_input == 4:
  print("Thursday")
elif user_input == 5:
  print("Friday")
elif user_input == 6:
  print("Saturday")
elif user_input == 7:
  print("Sunday")
else:
  print("Wrong number!")


# Classwork 8
i = 1

while i < 11:
  if i % 2 == 0:
    print("Even number")
  else:
    print("Odd number")
    i += 1

# Classwork 9
user_age = int(input("How old are you? "))

if user_age >= 5 and user_age <= 12:
  print("You are a Kid")
elif user_age > 12 and user_age < 18:
  print("You are a Teeneger")
elif user_age >= 18:
  print("You are an Adult") 


# Classwork 10
user_age = int(input("How old are you? "))

if user_age < 18:
  print("You cannot participate in the elections.")
else:
  print("You can participate in the elections.")