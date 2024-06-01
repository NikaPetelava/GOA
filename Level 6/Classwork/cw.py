"""
input_ი გვთხოვს რომ ჩავწეროთ რიცხვი, ამისათვის კი Input ფუნქცია 
გადაგვყავს Integer_ში, რადგანაც სხვა შემთხვევაში ჩაწერილი რიცხვები 
გამოისახება String_ის სახით.
"""
# input_ის მეშვეობით მომხმარებელს ვაძლევ ინფორმაციის შეტანის შესაძლებლობას ჩემს პროგრამაში
# Output_ის მეშვეობით კი მომხმარებლის მიერ შეტანილი ონფორმაია გამომაქვს ტერმინალში

# Input_ში ჩაწერილი რიცხვი გადამყავს Integer_ში, int ფუნქციის მეშვეობით
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
num4 = int(input("Enter fourth number: "))

#შედეგი გამოგვყავს ტერმინალში
print((num1 + num2) * num3 - num4 )

#შედარებითი ოპერატორები
print(num1 == num2) # ტოლია
print(num1 != num2) # არ არის ტოლი
print(num1 > num2) # მეტია
print(num1 >= num2) # ტოლია ან მეტია
print(num1 < num2) # ნაკლებია
print(num1 <= num2) # ტოლია ან ნაკლებია

