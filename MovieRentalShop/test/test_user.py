import datetime
import unittest

from MovieRentalShop.src.movie import Movie, MovieGenre
from MovieRentalShop.src.user import User, UserRole


class TestUser(unittest.TestCase):

    def setUp(self):
        self.valid_user = User ("Jacek", "Placek", 123444555,
                                datetime.date(2010,7,25), UserRole.CLIENT)
        self.test_movie = Movie (4, "Notatnik", "Rayn Gosling", 1998, MovieGenre.ROMANCE)

    def test_user_initialization(self):
        self.assertEqual(self.valid_user.first_name, "Jacek")
        self.assertEqual(self.valid_user.last_name, "Placek")
        self.assertEqual(self.valid_user.phone, 123444555)
        self.assertEqual(self.valid_user.birth, datetime.date(2010,7,25))
        self.assertEqual(self.valid_user.role, UserRole.CLIENT)
        self.assertEqual(self.valid_user.register_date, datetime.date.today())
        self.assertEqual(self.valid_user.rented_movies, [] )
        self.assertEqual(self.valid_user.all_rented_movies, [])
        self.assertEqual(self.valid_user.active,True)

    def test_creation_positive(self):
        user1 = User("Mariusz", "Gork", 999666333,
                     datetime.date(2000, 3, 12), UserRole.EMPLOYEE)
        self.assertIsInstance(user1, User)

    def test_error_too_short_phone(self):
        with self.assertRaises(ValueError) as context:
            user1 = User("Mariusz", "Gork", 99966,
                         datetime.date(2000, 3, 12), UserRole.EMPLOYEE)
        self.assertEqual(str(context.exception), "Phone number is too short")

    def test_error_letters_phone(self):
        with self.assertRaises(ValueError) as context:
            user1 = User("Mariusz", "Gork", "233abc",
                         datetime.date(2000, 3, 12), UserRole.EMPLOYEE)
        self.assertEqual(str(context.exception), "Phone number must only contain numbers")

    def test_error_too_young_user(self):
        with self.assertRaises(ValueError) as context:
            user1 = User("Mariusz", "Gork", 999666123,
                         datetime.date(2020, 3, 12), UserRole.CLIENT)
        self.assertEqual(str(context.exception), "You are too young to rent movies")

    def test_error_birth(self):
        with self.assertRaises(ValueError) as context:
            user1 = User("Mariusz", "Gork", 999900866,
                         "marzec", UserRole.EMPLOYEE)
        self.assertEqual(str(context.exception), "Invalid birth date")

    def test_error_role(self):
        with self.assertRaises(ValueError) as context:
            user1 = User("Mariusz", "Gork", 999900866,
                         datetime.date(1993, 5, 8), "klient")
        self.assertEqual(str(context.exception), "Invalid role")

    def test_error_first_name_capital(self):
        with self.assertRaises(ValueError) as context:
            user1 = User("mariusz", "Gork", 999900866,
                         datetime.date(1993, 5, 8), UserRole.CLIENT)
        self.assertEqual(str(context.exception), "First name must start with capital letter")

    def test_error_last_name_capital(self):
        with self.assertRaises(ValueError) as context:
            user1 = User("Mariusz", "ork", 999900866,
                         datetime.date(1993, 5, 8), UserRole.CLIENT)
        self.assertEqual(str(context.exception), "Last name must start with capital letter")

    def test_error_numbers_in_first_name(self):
        with self.assertRaises(ValueError) as context:
            user1 = User("M4riusz", "Gork", 999900866,
                         datetime.date(1993, 5, 8), UserRole.CLIENT)
        self.assertEqual(str(context.exception), "First name must only contain letters")

    def test_error_numbers_in_last_name(self):
        with self.assertRaises(ValueError) as context:
            user1 = User("Mariusz", "L0rk", 999900866,
                         datetime.date(1993, 5, 8), UserRole.CLIENT)
        self.assertEqual(str(context.exception), "Last name must only contain letters")

    def test_rent_movie_positive(self):
        self.valid_user.rent_movie(self.test_movie)
        self.assertFalse(self.test_movie.available)
        self.assertEqual(self.test_movie.rented_by, self.valid_user)
        self.assertIsNotNone(self.test_movie.rent_date)
        self.assertIn(self.test_movie, self.valid_user.rented_movies)

    def test_error_rent_movie_already_rented(self):
        pass

    def test_error_rent_movie_too_young_user(self):
        pass

    def test_error_rent_movie_inactive_user(self):
        pass

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()