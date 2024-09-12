
names = ["Adele", "Coldplay", "Beyoncé", "Bruno Mars"]

for name in names:
    print(f"Hey {name}, I love your music!")


movies_with_directors = [("Inception", "Christopher Nolan"), 
                         ("Interstellar", "Christopher Nolan"), 
                         ("The Dark Knight", "Christopher Nolan")]

for movie, director in movies_with_directors:
    print(f"Dear {director}, I loved your movie {movie}! It's a masterpiece.")



guests = ["Albert Einstein", "Marie Curie", "Nikola Tesla"]

for guest in guests:
    print(f"Dear {guest}, you are cordially invited to dinner!")

print(f"\nUnfortunately, {guests[2]} can't make it to dinner.")
guests[2] = "Isaac Newton"

for guest in guests:
    print(f"Dear {guest}, you are cordially invited to dinner!")

print("\nGood news! We found a bigger dinner table and can invite more guests.")
guests.insert(0, "Charles Darwin")
guests.insert(2, "Leonardo da Vinci")
guests.append("Galileo Galilei")

for guest in guests:
    print(f"Dear {guest}, you are cordially invited to dinner!")

print("\nUnfortunately, the new dinner table won't arrive in time, and we can only invite two guests.")
while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Sorry {removed_guest}, I can't invite you to dinner anymore.")

for guest in guests:
    print(f"Dear {guest}, you are still invited to dinner!")

del guests[0]
del guests[0]

print(f"\nFinal guest list: {guests}")
print(f"Number of people invited to dinner: {len(guests)}")
