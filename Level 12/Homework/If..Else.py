# 1
age = int(input("Enter you age: "))

if age >= 18:
  print("You are now signed up!")
elif age < 0:
  print("You haven't been born yet!")
else:
  print("You must be 18+ to sign up")


# 2
response = input("Would you like food? (Y/N): ")

if response == "Y":
  print("Have some food")
else:
  print("No food for you")


# 3 
name = input("Enter your name: ")

if name == "":
  print("You did not type in your name!")
else:
  print(f"Hello {name}")


# 4
online = False

if online:
  print("The user is online")
else:
  print("The user is offline ")


# 5 
number = 21

if number > 10:
  print("Above 10,")
  if number > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")