import datetime

from movie_rental_shop import  MovieRentalShop
from user import User
from movie import Movie

Sklep = MovieRentalShop("Super sklep", "warszawa")
Tomek = User("Tomek", "Komji",444333222, datetime.date(2002,12,20),"CLIENT")
Tomek1 = User("Krzys", "Komji",445333222, datetime.date(2001,12,12),"CLIENT")
Tomek2 = User("Mia", "Komji",447333222, datetime.date(2000,12,2),"CLIENT")

film1 = Movie(1,"hobbit","obama",2000,"FANTASY",0)
film2 = Movie(2,"czarodziej z oz","obama",2003,"FANTASY",0)
film3 = Movie(3,"hary poter","obama",2004,"FANTASY")

Sklep.add_movie(film1)
Sklep.add_movie(film2)
Sklep.add_movie(film3)

Sklep.add_user(Tomek1)
#Sklep.add_user("kkk")
Sklep.add_user(Tomek2)
Tomek.rent_movie(film1)
Sklep.all_users()