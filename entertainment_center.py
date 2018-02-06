# Designate modules to use for program
import media  # Holds custom Movie class
import fresh_tomatoes

# Call class and assign instance variables
nacho_libre = media.Movie(
    "Nacho Libre",
    "A monk persues his dream of being a wrestler",
    "https://images-na.ssl-images-amazon.com/images/I/51r382egkVL.jpg",
    "https://www.youtube.com/watch?v=ElVSw6xpQ70")

emperors_new_groove = media.Movie(
    "Emperor's New Groove",
    "A selfish young emperor learns humility when he's turned into a llama",
    "https://i.ytimg.com/vi/PaKn5-o6a6s/movieposter.jpg",
    "https://www.youtube.com/watch?v=ppYOZ4eFU2M")

les_miserables = media.Movie(
    "Les Miserables",
    "A broken man turns his life around in the name of God",
    "https://goo.gl/RTtJih",
    "https://www.youtube.com/watch?v=ebSQ7A1FCtc")

catching_fire = media.Movie(
    "The Hunger Games: Catching Fire",
    "Katniss and Peeta are sent back into the arena to fight off past victors",
    "https://goo.gl/6sW57h",
    "https://www.youtube.com/watch?v=E1pnXxmNL24")

the_help = media.Movie(
    "The Help",
    "A writer and two maids come together to expose racism in their hometown",
    "https://goo.gl/BeiekZ",
    "https://www.youtube.com/watch?v=WbuKgzgeUIU")

fiddler_roof = media.Movie(
    "The Fiddler on the Roof",
    "A Jewish Dairyman deals with the breaking of tradition in 1905 Russia",
    "https://upload.wikimedia.org/wikipedia/en/5/5e/Fiddler_on_the_roof.jpg",
    "https://www.youtube.com/watch?v=PjfTNnznJXw")

# Movies list for fresh_tomatoes to create web interface
movies = [nacho_libre, emperors_new_groove, les_miserables,
          catching_fire, the_help, fiddler_roof]

fresh_tomatoes.open_movies_page(movies)
