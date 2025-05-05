import datetime
import unittest

from MovieRentalShop.src.movie import Movie, MovieGenre
from MovieRentalShop.src.movie_rental_shop import MovieRentalShop
from MovieRentalShop.src.user import User, UserRole


class TestMovieRentalShop(unittest.TestCase):

    def setUp(self):
        self.valid_movie_rental_shop = MovieRentalShop("Best Movies in Town", "Olsztyn")
        self.test_client = User("Mariusz", "Ser", 123456789,
                                datetime.date(2006,1,23), UserRole.CLIENT)
        self.test_employee = User("Wanda", "Kwiatek", 123456788,
                                  datetime.date(2000,11,23), UserRole.EMPLOYEE)
        self.valid_movie_rental_shop.add_user(self.test_client)
        self.valid_movie_rental_shop.add_user(self.test_employee)
        self.test_movie = Movie(1, "Garfild", "Pedro Pascal", 2013, MovieGenre.COMEDY)
        self.valid_movie_rental_shop.add_movie(self.test_movie)

    def test_movie_rental_shop_initialization(self):
        self.assertEqual(self.valid_movie_rental_shop.name, "Best Movies in Town")
        self.assertEqual(self.valid_movie_rental_shop.location, "Olsztyn")
        self.assertEqual(self.valid_movie_rental_shop.creation_date, datetime.date.today())
        self.assertIn(self.test_client, self.valid_movie_rental_shop.users)
        self.assertIn(self.test_employee, self.valid_movie_rental_shop.users)
        self.assertIn(self.test_movie, self.valid_movie_rental_shop.movies)

    def test_add_movie_positive(self):
        test_movie_rental_shop = MovieRentalShop("test", "Warszawa")
        test_movie_rental_shop.add_movie(self.test_movie)
        self.assertEqual(test_movie_rental_shop.movies, self.valid_movie_rental_shop.movies)

    def test_add_users_positive(self):
        test_movie_rental_shop = MovieRentalShop("test", "Warszawa")
        test_movie_rental_shop.add_user(self.test_client)
        test_movie_rental_shop.add_user(self.test_employee)
        self.assertEqual(test_movie_rental_shop.users, self.valid_movie_rental_shop.users)

    def test_add_the_same_movie_negative(self):
        with self.assertRaises(ValueError) as context:
            self.valid_movie_rental_shop.add_movie(self.test_movie)
        self.assertEqual(str(context.exception), "Movie with this id is already in the shop")

    def test_add_movie_with_used_id_negative(self):
        with self.assertRaises(ValueError) as context:
            self.valid_movie_rental_shop.add_movie(Movie(1, "Smerfy", "George Lukas",
                                                         2013, MovieGenre.COMEDY))
        self.assertEqual(str(context.exception), "Movie with this id is already in the shop")

    def test_add_the_same_user_negative(self):
        with self.assertRaises(ValueError) as context:
            self.valid_movie_rental_shop.add_user(self.test_employee)
        self.assertEqual(str(context.exception), "This user is already in system")

    def test_add_user_invalid_date(self):
        with self.assertRaises(ValueError) as context:
            self.valid_movie_rental_shop.add_user("user")
        self.assertEqual(str(context.exception), "Invalid data")

    def test_add_the_same_phone_negative(self):
        with self.assertRaises(ValueError) as context:
            self.valid_movie_rental_shop.add_user(User("Piotr", "Piotrowski", 123456789,
                                                       datetime.date(2001,1,1), UserRole.CLIENT))
        self.assertEqual(str(context.exception), "This phone number is already in use")

    def test_remove_movie(self):
        self.valid_movie_rental_shop.remove_movie(self.test_movie)
        self.assertNotIn(self.test_movie, self.valid_movie_rental_shop.movies)

    def test_remove_user(self):
        self.test_client.active = False
        self.valid_movie_rental_shop.remove_user(self.test_client)
        self.assertNotIn(self.test_client, self.valid_movie_rental_shop.users)

    def test_error_remove_active_user(self):
        with self.assertRaises(ValueError) as context:
            self.valid_movie_rental_shop.remove_user(self.test_client)
        self.assertEqual(str(context.exception),"Cannot remove active account")

    def test_error_remove_user(self):
        with self.assertRaises(ValueError) as context:
            self.valid_movie_rental_shop.remove_user(User("Maciek", "Mydło", 333666777,
                                                          datetime.date(2000,2,12), UserRole.EMPLOYEE))
        self.assertEqual(str(context.exception),"User not found")

    def test_error_remove_rented_movie(self):
        self.test_movie.available = False
        with self.assertRaises(ValueError) as context:
            self.valid_movie_rental_shop.remove_movie(self.test_movie)
        self.assertEqual(str(context.exception), "This movie is rented right now")

    def test_error_remove_movie(self):
        with self.assertRaises(ValueError) as context:
            self.valid_movie_rental_shop.remove_movie(Movie(4, "Minions", "Lordofon", 2022,
                                                            MovieGenre.ADVENTURE))
        self.assertEqual(str(context.exception), "Movie not found")

    def test_positive_find_movie_by_id(self):
        find_movie = self.valid_movie_rental_shop.find_movie_by_id(1)
        self.assertEqual(self.test_movie, find_movie)

    def test_negative_find_movie_by_id(self):
        with self.assertRaises(ValueError) as context:
            self.valid_movie_rental_shop.find_movie_by_id(3)
        self.assertEqual(str(context.exception), "Movie not found")

    def test_positive_find_movie_by_title(self):
        find_movies = self.valid_movie_rental_shop.find_movie_by_title("Garfild")
        self.assertIn(self.test_movie, find_movies)

    def test_negative_find_movie_by_title(self):
        with self.assertRaises(ValueError) as context:
            self.valid_movie_rental_shop.find_movie_by_title("Shrek")
        self.assertEqual(str(context.exception), "Movie not found")

    def test_positive_find_movies_by_title(self):
        test_movie2 = Movie(2, "Garfild", "Lolek", 2024,
                            MovieGenre.COMEDY)
        self.valid_movie_rental_shop.add_movie(test_movie2)
        find_movies = self.valid_movie_rental_shop.find_movie_by_title("Garfild")
        self.assertEqual(find_movies, [self.test_movie, test_movie2])

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()