# აბრუნებს True_ს თუ სტრიქონში ყველა სიმბოლო არის პატარა
print("--------islower------------")
txt = "Hello! Welcome to GOA!"
print(txt.islower())

txt = "hello-welcome-to-goa!"
print(txt.islower())

txt = "welcome123"
print(txt.islower())

# აბრუნებს True_ს თუ სტრიქონში ყველა სიმბოლო არის დიდი
print("--------isupper------------")
txt = "PYTHON"
print(txt.isupper())

txt = "PY-TH-ON"
print(txt.isupper())

txt = "Cod3iN#g"
print(txt.isupper())

#აბრუნებს True-ს, თუ სტრიქონის ყველა სიმბოლო რიცხვითია
print("--------isnumeric------------")
txt = "2024"
print(txt.isnumeric())

txt = "Welcome2024"
print(txt.isnumeric())

txt = "123-456-789"
print(txt.isnumeric())

# აბრუნებს True_ს თუ სტრიქონის ყველა სიმბოლო არის ანბანში
print("--------isalpha------------")
txt = "Welcome"
print(txt.isalpha())

txt = "Hello! Welcome to GOA!"
print(txt.isalpha())

txt = "Welcome123"
print(txt.isalpha())