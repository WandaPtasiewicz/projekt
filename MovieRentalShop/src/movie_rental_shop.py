import datetime

from MovieRentalShop.src.user import User
from MovieRentalShop.src.movie import Movie

class MovieRentalShop:
    def __init__(self, name, location):

        self.name = name
        self.location = location
        self.movies = list()
        self.users = list()
        self.creation_date = datetime.date.today()

    def add_movie(self, new_movie):
        if any(movie.id == new_movie.id for movie in self.movies):
            raise ValueError("Movie with this id is already in the shop")

        self.movies.append(new_movie)

    def remove_movie(self, movie):
        if movie not in self.movies:
            raise ValueError("Movie not found")

        if not movie.available:
            raise ValueError("This movie is rented right now")

        return self.movies.remove(movie)

    def remove_user(self, user):
        if user not in self.users:
            raise ValueError("User not found")

        if user.active:
            raise ValueError("Cannot remove active account")

        return self.users.remove(user)

    def add_user(self, new_user):
        if not isinstance(new_user, User):
            raise ValueError("Invalid data")
        if new_user in self.users:
            raise ValueError("This user is already in system")
        if any(user.phone == new_user.phone for user in self.users):
            raise ValueError("This phone number is already in use")
        self.users.append(new_user)

    def find_movie_by_id(self, movie_id):
        for movie in self.movies:
            if movie.id == movie_id:
                return movie
        raise ValueError("Movie not found")

    def find_movie_by_title(self, movie_title):
        find_movies = [movie for movie in self.movies if movie.title == movie_title]
        if not find_movies:
            raise ValueError ("Movie not found")
        return find_movies

    def all_movies(self):
        return self.movies

    def all_users(self) :
        return self.users