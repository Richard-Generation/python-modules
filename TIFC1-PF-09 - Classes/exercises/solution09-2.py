class User:
    def __init__(self, first_name, last_name, age, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.location = location
        self.login_attempts = 0  # Attribute to store login attempts

    def describe_user(self):
        """Prints a summary of the user's information."""
        print(f"User Profile:\n"
              f"First Name: {self.first_name}\n"
              f"Last Name: {self.last_name}\n"
              f"Age: {self.age}\n"
              f"Email: {self.email}\n"
              f"Location: {self.location}\n")

    def greet_user(self):
        """Prints a personalized greeting to the user."""
        print(f"Hello, {self.first_name} {self.last_name}! Welcome back!")

    def increment_login_attempts(self):
        """Increments the value of login_attempts by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Resets the login_attempts attribute to 0."""
        self.login_attempts = 0


# Creating several instances representing different users
user1 = User("John", "Doe", 30, "johndoe@example.com", "New York")
user2 = User("Jane", "Smith", 25, "janesmith@example.com", "Los Angeles")
user3 = User("Emily", "Brown", 35, "emilybrown@example.com", "Chicago")

# Calling describe_user() and greet_user() methods for each user
user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()

# Stretch and Challenge: Working with login_attempts
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()

print(f"\nLogin attempts for {user1.first_name}: {user1.login_attempts}")

# Resetting login attempts
user1.reset_login_attempts()
print(f"Login attempts after reset: {user1.login_attempts}")
