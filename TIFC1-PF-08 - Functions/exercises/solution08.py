# 1
def display_message(message):
    print(message)
message_show=display_message("hello")

# 2

def favorite_book(title):
    print(f"my favorite book is {title.title()}")
fav_show=favorite_book("alice")

# 3
def make_shirt(size="large",message="I love python"):
    print(f"your size is {size} and the message is {message}")

shirt=make_shirt(5,"HI")
shirt=make_shirt(message="Hello",size=10)
shirt=make_shirt()
shirt=make_shirt(size="medium")

# 4
def describe_city(city, country="Iceland"):
    print(f"{city} is in {country}.")
    describe_city('Reykjavik')             
    describe_city('Oslo', 'Norway')       
    describe_city('Tokyo', 'Japan')

# 5
def make_album(artist_name,album_title,track=None):
    album_info = {
        "name":artist_name,
        "title":album_title
        }
    if track is not None:
        album_info["track"]=track
    return album_info
album1 = make_album('The Beatles', 'Abbey Road')
album2 = make_album('Pink Floyd', 'The Dark Side of the Moon', 10)
album3 = make_album('Adele', '25', 11)
print(album1)
print(album2)
print(album3)

while True:

    artist = input("Enter the artist's name (or type 'quit' to exit): ")
    if artist.lower() == 'quit':
        break
    title = input("Enter the album title: ")

    tracks_input = input("Enter the number of tracks (or press Enter to skip): ")
    if tracks_input:
        try:
            tracks = int(tracks_input)
        except ValueError:
            print("Invalid number of tracks. It must be an integer.")
            continue
    else:
        tracks = None
    album = make_album(artist, title, tracks)
    

    print(album)

# 6