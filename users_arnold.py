class User: 
    def __init__(self, first_name, middle_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.age = age

    def describe_user(self):
        print(f"User Profile: ")
        print(f"Name: {self.first_name} {self.middle_name} {self.last_name}")
        print(f"Age: {self.age}")

    def greet_user(self): 
        print(f"Hello {self.first_name}! Welcome!")

    
user1 = User("Colby", "Ryan", "Arnold", 14)
user2 = User("Jamie", "Elizabeth", "Arnold", 42)
user3 = User("Kevin", "Scott", "Arnold", 49)

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()
print()