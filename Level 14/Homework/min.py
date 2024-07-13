# 1
numbers = [5,10,15,20]
print(min(numbers))

# 2 
fruits = ["apple", "banana", "Kiwi", "ww"]
print(min(fruits))

# 3
temperatures = [15, 20, 12, 25, 18]
lowest_temp = min(temperatures)
print(f"The lowest temperature is: {lowest_temp}") 

# 4
price = [10.50, 15.99, 8.25, 12.00]
minimum_price = min(price)
print(f"The minimum price is: ${minimum_price:.2f}")

# 5
numbers = [1,2,3,4,5]
min_number = numbers[0]

for number in numbers:
  if min_number > number:
    min_number = number

print(min_number)