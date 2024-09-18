# 1
message = "what kind of rental car you would like?"
while True:
    car = input(message)
    print(f"let me see if I can find {car}")
    break
# 2
message = "how many people are in your dinner group?"
while True:
    count = int(input(message))
    if count > 8:
        print("wait for a table")
    else:
        print("your table is ready")
    break
# 3
message = "write a number\n"
the_number = input (message)
if int(the_number) % 10 == 0:
    print("multiple of 10")
else:
    print("not multiple of 10")
# 4
while True:
    prompt = input("Enter a pizza topping (or type 'quit' to stop):")
    if prompt.lower() == "quit":
        break
    else:
        print(f"I will add {prompt} to your pizza")
# 5
while True:
    age = int(input("What's your age?"))
    if age < 3:
        print("free")
    elif age <=12 and age >= 3:
        print("10$")
    elif age >12:
        print("15$")
    break
# 6
while True:
    print("never ending loop \npress ctrl + c to quit")
    break
# Stretch and Challenge

# A

sandwich_orders = ['Pastrami Sandwich','Turkey Sandwich','Pastrami Sandwich', 'Ham Sandwich', 'Veggie Sandwich', 'Tuna Sandwich', 'Chicken Sandwich','Pastrami Sandwich']
finished_sandwiches = []
print("we are out of Pastrami Sandwich")
while "Pastrami Sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami Sandwich")

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"I have made your {current_sandwich}")
    finished_sandwiches.append(current_sandwich)
print("\nFinished sandwiches:")
for item in finished_sandwiches:
    print(f"-{item}")

# B
dream_list=[]
while True:
    prompt=input("what is your dream destination?")
    if prompt.lower() == "quit":
        break
    dream_list.append(prompt)
print("\nPoll Results:")
for i, destination in enumerate(dream_list, start=1):
    print(f"{i}. {destination}")
