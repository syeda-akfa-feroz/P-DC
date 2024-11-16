class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def introduce(self):
        return f"Hello! My name is {self.name}, I am {self.age} years old, and I live in {self.city}."

person1 = Person("Ali", 25, "Lahore")
print(person1.introduce())
