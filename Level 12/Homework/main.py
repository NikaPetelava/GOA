# Homework #9
budget = int(input("Enter your budget: "))

if budget == 2:
  print("You can buy a bread")
elif budget == 5:
  print("You can buy an egg")
elif budget == 8:
  print("You can buy a fruits")
elif budget == 10:
  print("You can buy a vegetables")
elif budget == 12:
   print("You can buy a chicken")
else:
  print("You dont have enought money!")
  
# Homework #10
choice = input("Choose Arithetic symbol(+, -, *, /): ")

num1 = int(input("Enter First number: "))
num2 = int(input("Enter Second number: "))

if choice == "+":
  print(num1 + num2)
elif choice == "-":
  print(num1 - num2)
elif choice == "*":
  print(num1 * num2)
elif choice == "/":
  print(num1 / num2)
else:
  print("Invalid Arithetic symbol")

# Homework #11
sum = 0
count = 1

while count <= 100:
  sum += count
  count += 1

print(f"The sum is: {sum}")

