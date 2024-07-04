# 1
num = 1
while num < 6:
  print(num)
  num += 1

# 2
num = 1
while num < 6:
  print(num)
  num += 1
else:
  print("number is not longer less than 6")


# 3
name = input("Enter your name: ")
while name == "":
  print("You did not enter your name")
  name = input("Enter your name: ")

print(f"Hello, {name}")


# 4
food = input("Enter a food you like (q to quite): ")
while not food == "q":
  print(f"You like {food}")
  food = input("Enter a food you like (q to quite): ")

print("Bye")

# 5
num = int(input("Enter a # beetwen 1 - 10: "))
while num < 1 or num > 10:
  print(f"{num} is not valid")
  num = int(input("Enter a # beetwen 1 - 10: "))

print(f"Your number is {num}")
