import datetime
import json
from enum import Enum, auto
from MovieRentalShop.src.user import age_from_date


class MovieGenre(Enum):
    COMEDY = auto()
    HORROR = auto()
    THRILLER = auto()
    FANTASY = auto()
    MYSTERY = auto()
    ROMANCE = auto()
    ACTION = auto()
    ADVENTURE = auto()
    SCIENCE_FICTION = auto()

class Movie:
    def __init__(self,id , title, director, release_year, genre, age_limit = 0):

        self.id =id

        if not title[0].isupper():
            raise ValueError("Title mast start with capital letter")

        self.title = title
        self.director = director

        if not isinstance(genre, MovieGenre):
            raise ValueError("Invalid genre")

        self.genre = genre

        if age_limit < 0 :
            raise ValueError("Age limit can't less than 0")

        self.age_limit = age_limit

        if not isinstance(release_year, int) or release_year < 1888 or release_year > datetime.datetime.now().year:
            raise ValueError(f"Invalid release year: {release_year}")

        self.release_year = release_year

        self.available = True
        self.rent_date = None
        self.rented_by = None

    def rent_movie(self, user):
        if not self.available:
            raise ValueError(f"Movie '{self.title}' is already rented.")

        if age_from_date(user.birth) < self.age_limit:
            raise ValueError("You are too young to rent this movie.")

        self.available = False
        self.rent_date = datetime.datetime.now()
        self.rented_by = user

    def return_movie(self):
        if self.available:
            raise ValueError(f"Movie '{self.title}' is already available.")

        self.available = True
        self.rent_date = None
        self.rented_by = None

    def to_json(self):
        data = {
            "title": self.title,
            "director": self.director,
            "release_date": self.rent_date,
            "genre": self.genre,
            "age_limit": self.age_limit,
            "available": self.available
        }

        return json.dumps(data, ensure_ascii=False)

