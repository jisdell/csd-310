# Author: Jacob Isdell
# Date: 09/22/2024
# Assignment: Module 7
# Description: Python script to query and iterate through movies database

import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "movies_user",
    "password": "popcorn",
    "host": "127.0.0.1",
    "database": "movies",
    "raise_on_warnings": True,
}

try:
    db = mysql.connector.connect(**config)
    print(
        "\n Database user {} connected to MySQL on host {} with database {}".format(
            config["user"], config["host"], config["database"]
        )
    )
    input("\n\n Press any key to continue...")

    cursor = db.cursor()
    # Studio display
    cursor.execute("SELECT * FROM studio")
    studios = cursor.fetchall()
    print("-- DISPLAYING Studio RECORDS --")
    for studio in studios:
        print("Studio ID: {}\nStudio Name: {}\n".format(studio[0], studio[1]))
    # Genre display
    cursor.execute("SELECT * FROM genre")
    genres = cursor.fetchall()
    print("-- DISPLAYING Genre RECORDS --")
    for genre in genres:
        print("Genre ID: {}\nGenre Name: {}\n".format(genre[0], genre[1]))
    # Short Film display
    cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime <= 120")
    films = cursor.fetchall()
    print("-- DISPLAYING Short Film RECORDS --")
    for film in films:
        print("Film Name: {}\nRuntime: {}\n".format(film[0], film[1]))
    # Director in Order display
    cursor.execute("SELECT film_name, film_director FROM film ORDER BY film_director")
    director_films = cursor.fetchall()
    print("-- DISPLAYING Director RECORDS in Order --")
    for director_film in director_films:
        print(
            "Film Name: {}\nDirector: {}\n".format(director_film[0], director_film[1])
        )

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")
    else:
        print(err)
finally:
    db.close()
