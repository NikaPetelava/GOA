# 1
person = {
    "name": "Nika",
    "age": 28,
    "city": "Zugdidi",
    "work": "unemployed"
}

print(f"My name is {person['name']} i'm {person['age']} years old.I live in {person['city']} and currently {person['work']}.")
print("---------------------------")
# 2
grades = {
    "math": 70,
    "history": 90,
    "literature": 90
}

average_grade = sum(grades.values()) / len(grades)

print(f"Average grade is: {int(average_grade)}")
print("---------------------------")
# 3
favorite_book = {
    "title": "Kafka on the Shore",
    "author": "Haruki Murakami",
    "published": 2002,
    "genre": "Magical Realism, Fantasy Fiction"

}

print(f"My favorite book is {favorite_book['title']} by {favorite_book['author']}, publishe in {favorite_book['published']}.It's a {favorite_book['genre']} novel.")
print("---------------------------")
# 4 

shopping_cart = {}

num_items = int(input("How many items do you want to buy? "))

for i in range(num_items):
    item_name = input("Enter item name: ")
    quantity = int(input("Enter item quantity: "))
    shopping_cart[item_name] = quantity

print("\nYour shopping cart: ")
for item, quantity in shopping_cart.items():
    print(f"{item}: {quantity}")


