from typing import TypedDict

class Movie(TypedDict):
    title: str
    year: int
    rating: float

my_movie: Movie = {
    "title": "Inception",
    "year": 2010,
}

print(my_movie)
print(my_movie["title"])
print(my_movie.get("title"))
print(my_movie["year"])
my_movie["rating"] = 9

print(my_movie["rating"])

def process_movie(mov: Movie) -> None:
    print(f'Processing movie: {mov.get("title")} ({mov.get("year")} with rating {mov.get("rating")}')

amovie = {
    "title": "The Matrix",
    "year": 1999,
    "rating": 8.7
}

process_movie(amovie)


# - Class
# - Object
# - Encapsulation / abstraction
# - Overriding
# - Inheritance




