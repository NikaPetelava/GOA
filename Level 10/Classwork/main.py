# Classwork #1
password = input("Enter password: ")
correct_password = "luka123"

if password == correct_password:
  print("Your password is corect, Welcome!")
else:
  print("Your password is incorect, try again!")


# Classwork #2
addition_num = 1

for i in range(5):
  number = int(input("Enter your number: "))
  addition_num *= number

print("Sum Is:", addition_num)

# Classwork #3
num = 0

for x in range(5, 16):
  num += x

print(num)

