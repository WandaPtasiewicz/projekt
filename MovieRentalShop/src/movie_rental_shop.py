import datetime

from user import User


class MovieRentalShop:
    def __init__(self, name, location):

        self.name = name
        self.location = location
        self.movies = {}
        self.users = {}
        self.creation_date = datetime.datetime.now()

    def add_movie(self, movie):
        if movie.id in self.movies:
            raise ValueError("Movie with this is is already in the shop")

        self.movies[movie.id] = movie

    def remove_movie(self, id):
        if id not in self.movies:
            raise ValueError("Movie not found in the shop")

        movie = self.movies[id]
        if not movie.available:
            raise ValueError(f"Cannot remove movie '{movie.title}' as it is currently rented")

        return self.movies.pop(id)

    def find_movie_by_id(self, id):
        if id not in self.movies:
            raise ValueError(f"Movie with {id} not found.")
        return self.movies.get(id)

    def find_movie_by_title(self, title):
        movies = [movie for movie in self.movies.values() if title.lower() in movie.title.lower()]
        if not movies:
            raise ValueError(f"Movie '{title}' not found.")
        return movies

    def find_movies_by_genre(self, genre):
        movies = [movie for movie in self.movies.values() if genre in movie.genre]
        if not movies:
            raise ValueError(f"Movie from '{genre}' not found.")
        return movies

    def find_movies_by_director(self, director):
        movies = [movie for movie in self.movies.values() if director.lower() in movie.director.lower()]
        if not movies:
            raise ValueError(f"Movie directed by '{director}' not found.")
        return movies

    def add_user(self, new_user):
        if not isinstance(new_user, User):
            raise ValueError("User not found")
        if new_user.phone in self.users:
            raise ValueError(f"User {new_user} is already in system.")
        self.users[new_user.phone] = new_user
        return True

    def find_user_by_phone(self, phone):
        if phone not in self.users:
            raise ValueError("User not found")
        return self.users.get(phone)

    def find_users_by_first_name(self, first_name):
        users = [user for user in self.users.values() if first_name.lower() in user.first_name.lower()]
        if not users:
            raise ValueError("User not found.")
        return users

    def find_users_by_last_name(self, last_name):
        users = [user for user in self.users.values() if last_name.lower() in user.last_name.lower()]
        if not users:
            raise ValueError("User not found.")
        return users

    def find_users_by_role(self, role):
        users = [user for user in self.users.values() if role in user.role]
        if not users:
            raise ValueError("User not found.")
        return users
    def all_movies(self):
        for movie_id, movie in self.movies.items():
            print(f"id: {movie_id}, title: {movie.title}, release year: {movie.release_year}, director: {movie.director}")

    def all_users(self) -> object:
        for user_phone, user in self.users.items():
            print(f"phone: {user_phone}, first name: {user.first_name},last name: {user.last_name}, birth: {user.birth},"
                  f" role: {user.role} ")