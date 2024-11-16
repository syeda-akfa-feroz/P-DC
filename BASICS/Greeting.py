def greet_user(name):
    return f"Welcome, {name.capitalize()}! Have a great day!"

user_name = input("Please enter your name: ").strip()
print(greet_user(user_name))
