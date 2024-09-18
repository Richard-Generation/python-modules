pizzas = ['pepperoni', 'margherita', 'bbq chicken']
for pizza in pizzas:
    print(f"I like {pizza} pizza.")
print("\nI really love pizza!")

animals = ['dog', 'cat', 'rabbit']
for animal in animals:
    print(f"A {animal} would make a great pet.")
print("\nAny of these animals would make a great pet!")

for number in range(1, 21):
    print(number)

numbers = list(range(1, 1000001))
print(f"Minimum: {min(numbers)}")
print(f"Maximum: {max(numbers)}")
print(f"Sum: {sum(numbers)}")

multiples_of_3 = list(range(3, 31, 3))
for number in multiples_of_3:
    print(number)
