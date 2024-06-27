# 1
for x in range(1, 11):
  print(x)

# 2
for x in reversed(range(1, 11)):
  print(x)

print("HAPPY NEW YEAR!")

# 3
for x in range(1, 11, 2):
  print(x)

# 4
credit_card = "1234-5678-9012-5063"

for x in credit_card:
  print(x)

# 5
for x in range(1, 21):
  if x == 13:
    continue
  else:
    print(x)

# 6 
for x in range(1, 21):
  if x == 13:
    break
  else:
    print(x)