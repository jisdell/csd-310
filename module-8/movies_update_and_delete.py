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
    input("\n\n Press any key to continue... \n")

    cursor = db.cursor()

    def show_films(cursor, title):
        cursor.execute(
            "SELECT film_name as Name, film_director as Director, genre_name as Genre, studio_name as 'Studio Name' FROM film INNER JOIN genre ON film.genre_id = genre.genre_id INNER JOIN studio ON film.studio_id = studio.studio_id"
        )
        films = cursor.fetchall()
        print("--  '{}' --".format(title))
        for film in films:
            print(
                "Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudio Name: {}\n".format(
                    film[0], film[1], film[2], film[3]
                )
            )

    # Show the OG films
    show_films(cursor, "DISPLAYING FILMS")
    # Add a new film
    cursor.execute(
        "INSERT INTO film (film_id, film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id) VALUES(4, 'Scott Pilgrim vs. the World', '2010', 112, 'Edgar Wright', 3, 2)"
    )
    # Show the new films
    show_films(cursor, "DISPLAYING FILMS AFTER INSERT")
    # Update Alien to a Horror film
    cursor.execute("UPDATE film SET genre_id = 1 WHERE film_name = 'Alien'")
    # Show the updated films
    show_films(cursor, "DISPLAYING FILMS AFTER UPDATE- Changed Alien to Horror")
    # Delete Gladiator from films
    cursor.execute("DELETE FROM film WHERE film_name = 'Gladiator'")
    # Show the remaining films
    show_films(cursor, "DISPLAYING FILMS AFTER DELETE")


except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")
    else:
        print(err)
finally:
    db.close()
