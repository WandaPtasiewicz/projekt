import datetime
import json
from enum import Enum, auto

class UserRole(Enum):
    CLIENT = auto()
    EMPLOYEE= auto()
    ADMIN = auto()

def age_from_date(date):
    age = datetime.datetime.now().year - date.year
    if (datetime.datetime.now().month, datetime.datetime.now().day) < (date.month, date.day):
        age -= 1
    return age

class User:
    def __init__(self, first_name, last_name, phone, birth, role):

        if not first_name[0].isupper():
            raise ValueError("First name must start with capital letter")

        if any(char.isdigit() for char in first_name):
            raise ValueError("First name must only contain letters")
        self.first_name = first_name

        if not last_name[0].isupper():
            raise ValueError("Last name must start with capital letter")

        if any(char.isdigit() for char in last_name):
            raise ValueError("Last name must only contain letters")
        self.last_name = last_name

        if not isinstance(role, UserRole):
            raise ValueError("Invalid role")
        self.role = role

        if not isinstance(phone, int):
            raise ValueError("Phone number must only contain numbers")

        if not len(str(phone)) == 9:
            raise ValueError("Phone number is too short")
        self.phone = phone

        if not isinstance(birth, datetime.date):
            raise ValueError("Invalid birth date")
        self.birth = birth

        if age_from_date(birth) < 10:
            raise ValueError("You are too young to rent movies")

        self.register_date = datetime.date.today()
        self.rented_movies = []
        self.all_rented_movies = []
        self.active = True

    def rent_movie(self, movie):
        if not self.active:
            raise ValueError("Your account has been deactivated")

        if movie in self.rented_movies:
            raise ValueError("You already rented this movie")

        movie.rent_movie(self)
        self.rented_movies.append(movie)
        self.all_rented_movies.append(movie)
        return True

    def return_movie(self, movie):
        if not self.active:
            raise ValueError("Your account has been deactivated")

        if movie not in self.rented_movies:
            raise ValueError("You already returned this movie")

        movie.return_movie()
        self.rented_movies.remove(movie)

    def deactivate(self):
        if self.rented_movies:
            raise ValueError("Cannot deactivate user with rented movies")
        self.active = False
        return True

    def activate(self):
        self.active = True
        return True

    def to_json(self):
        data = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "phone": self.phone,
            "role": self.role.name,
            "register_date": self.register_date,
            "active": self.active,
            "rented_movies": len(self.rented_movies)
        }

        return json.dumps(data, ensure_ascii=False)
