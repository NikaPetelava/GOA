# ყოფს სტრიქონს მითითებულ გამყოფზე და აბრუნებს სიას
txt = "welcome to the jungle"
print(txt.split())

txt = "hello, my name is Nika, I am 28 years old"
print(txt.split(", "))

# # ეძებს მითითებულ მნიშვნელობას სტრიქონში და აბრუნებს პოზიციას, სადაც ის იქნა ნაპოვნი
txt = "Hello, welcome to my world."
print(txt.index("welcome"))


# გამოიყენება ელემენტების თანმიმდევრობის (სიის, ტუპლის ან სტრიქონის) ერთ სტრიქონში შესაერთებლად.
# ის აბრუნებს სტრიქონს, სადაც თანმიმდევრობის ელემენტები გაერთიანებულია მითითებული გამყოფის გამოყენებით.
words = ['Hello', 'world', 'from', 'Python']
separator = "-".join(words)
print(separator)
