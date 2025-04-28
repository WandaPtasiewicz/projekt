import datetime
import unittest

from MovieRentalShop.src.movie import Movie, MovieGenre
from MovieRentalShop.src.user import User, UserRole


class TestMovie(unittest.TestCase):

    def setUp(self):
        self.valid_movie = Movie(2, "Rambo", "Adam Nowak", 2000, MovieGenre.ACTION,
                                 10)
        self.test_user = User("Maria", "Kowal", 123456789,
                              datetime.date(2000,1,13), UserRole.CLIENT)

    def test_movie_initialization(self):
        self.assertEqual(self.valid_movie.id, 2)
        self.assertEqual(self.valid_movie.title, "Rambo")
        self.assertEqual(self.valid_movie.director, "Adam Nowak")
        self.assertEqual(self.valid_movie.release_year, 2000)
        self.assertEqual(self.valid_movie.genre, MovieGenre.ACTION)
        self.assertTrue(self.valid_movie.available)
        self.assertIsNone(self.valid_movie.rent_date)
        self.assertIsNone(self.valid_movie.rented_by)

    def test_creation_positive(self):
        movie1 = Movie(1,"Indiana Jones", "John Bon",2002, MovieGenre.ACTION,12)
        self.assertIsInstance(movie1, Movie)

    def test_creation_error_too_old_date(self):
        with self.assertRaises(ValueError) as context:
            movie1 = Movie(1,"Indiana Jones", "John Bon",2,MovieGenre.ACTION,12)
        self.assertEqual(str(context.exception), "Invalid release year: 2")

    def test_creation_error_date_from_future(self):
        with self.assertRaises(ValueError) as context:
            movie1 = Movie(1,"Indiana Jones", "John Bon",2222,MovieGenre.ACTION,12)
        self.assertEqual(str(context.exception), "Invalid release year: 2222")

    def test_creation_error_genre(self):
        with self.assertRaises(ValueError) as context:
            movie1 = Movie(1,"Indiana Jones", "John Bon",2,"fajny",12)
        self.assertEqual(str(context.exception), "Invalid genre")

    def test_rent_movie(self):
        self.valid_movie.rent_movie(self.test_user)
        self.assertFalse(self.valid_movie.available)
        self.assertEqual(self.valid_movie.rented_by, self.test_user)
        self.assertIsNotNone(self.valid_movie.rent_date)

    def test_error_movie_is_rented(self):
        self.valid_movie.rent_movie(self.test_user)

        with self.assertRaises(ValueError):
            self.valid_movie.rent_movie(self.test_user)

    def test_error_too_young_to_rent_movie(self):
        young_user = User("Michał", "Kot", 123111222,
                          datetime.date(2010,12,11), UserRole.CLIENT)
        adult_movie = Movie(3, "Krwawa masakra", "John Miller", 2002, MovieGenre.HORROR, 18)

        with self.assertRaises(ValueError):
            adult_movie.rent_movie(young_user)

    def test_error_age_limit_less_than_zero(self):
        with self.assertRaises(ValueError):
            invalid_movie = Movie(1,"Mama", "King", 2002, MovieGenre.FANTASY, -2)

    def test_error_title(self):
        with self.assertRaises(ValueError):
            invalid_movie = Movie(1,"mama", "King", 2002, MovieGenre.FANTASY, 2)

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()