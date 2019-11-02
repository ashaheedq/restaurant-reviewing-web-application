#
# get_best_pics.py
#
# A simple front-end for our movie database in SQLite.
# That will return all movies that WON BEST-PICTURE award between two years specifid by the user
# This program only works if you put the movie database
# (movie.sqlite) in the same folder as the program.
#
# Abdulshaheed Alqunber
# asq@bu.edu

import sqlite3

# Connect to the database and create a cursor for it.
con = sqlite3.connect('db.db')
cursor = con.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cursor.fetchall())

db.commit()
db.close()
