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

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()