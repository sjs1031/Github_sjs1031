# The sqlite Module

'''
# How to Create a Database and INSERT Some data
import sqlite3

conn = sqlite3.connect(".\Python_study_re\Python101\Part02\myDatabase.db") # or use :memory: to put it in RAM
cursor = conn.cursor()

# Create a table
cursor.execute("""CREATE TABLE albums (title text, artist text, release_data text, publisher text, media_type text)""")
conn.commit()
'''

'''
# insert some data
import sqlite3

conn = sqlite3.connect(".\Python_study_re\Python101\Part02\myDatabase.db")
cursor = conn.cursor()

cursor.execute("""INSERT INTO albums VALUES ('Glow', 'Andy Hunter', '7/24/2012', 'Xplore Records', 'MP3')""")

# save data to database
conn.commit()

# insert multiple records using the more secure "?" method
albums = [('Exodus', 'Andy Hunter', '7/9/2002', 'Sparrow Records', 'CD'),
          ('Until We Have Faces', 'Red', '2/1/2011', 'Essential Records', 'CD'),
          ('The End is Where We Begin', 'Thousand Foot Krutch', '4/17/2012', 'TFKmusic', 'CD'),
          ('The Good Life', 'Trip Lee', '4/10/2012', 'Reach Records', 'CD')]
cursor.executemany("INSERT INTO albums VALUES (?,?,?,?,?)", albums)
conn.commit()
'''

'''
# Updating amd Deleting Records
import sqlite3

conn = sqlite3.connect(".\Python_study_re\Python101\Part02\myDatabase.db")
cursor = conn.cursor()

sql = """
UPDATE albums
SET artist = 'John Doe'
WHERE artist = 'Andy Hunter'
"""
cursor.execute(sql)
conn.commit()
'''

'''
import sqlite3

conn = sqlite3.connect(".\Python_study_re\Python101\Part02\myDatabase.db")
cursor = conn.cursor()

sql = "DELETE FROM albums WHERE artist = 'John Doe'"
cursor.execute(sql)
conn.commit()
'''

# Basic SQLite Queries
import sqlite3
conn = sqlite3.connect(".\Python_study_re\Python101\Part02\myDatabase.db")
# conn.row_factory = sqlite3.row
cursor = conn.cursor()

sql = "SELECT * FROM albums WHERE artist =?"
cursor.execute(sql, [("Red")])
print(cursor.fetchall()) # or use fetchone()

print("\nHere's a listing of all the records in the table:\n")
for row in cursor.execute("SELECT rowid, * FROM albums ORDER BY artist"):
    print(row)

print("\nResults from a LIKE query:\n")
sql = "SELECT * FROM albums WHERE title LIKE 'THE%'"
cursor.execute(sql)
print(cursor.fetchall())