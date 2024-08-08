# 1
car_spec = {
    "mark": "Nissan",
    "name": "GT-R",
    "Year": 2024,
    "engine": "3.8-liter V6, 24-valve, twin-turbocharged"
}

print(car_spec)
print("---------------------------")

# 2 
personal_info = {
    "name": "Nika",
    "age": 28
}

personal_info.update({"surname": "Petelava"})
personal_info["email"] = "nicolasbro96@gmail.com"


print(personal_info)
print("---------------------------")

# 3
for key, values in personal_info.items():
    print(key, values)
print("---------------------------")

# 4
my_dict = {}

for i in range(1, 101):
    my_dict[f"item_{i}"] = i

print(my_dict)
