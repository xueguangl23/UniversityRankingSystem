import sqlite3
from os.path import expanduser

sqlite_file = expanduser("~") + "/data/db.sqlite"

connection = sqlite3.connect(sqlite_file)
cursor = connection.cursor()
#sql = "CREATE TABLE SelectedAffiliations (id INTEGER PRIMARY KEY AUTOINCREMENT, AffiliationID TEXT, AffiliationName TEXT)"
sql = "CREATE TABLE PaperAuthorAffiliations (id INTEGER PRIMARY KEY AUTOINCREMENT,PaperID TEXT, AuthorID TEXT, AffiliationID TEXT, OriginalAffiliationName TEXT, NormalizedAffiliationName TEXT, AuthorSequenceNumber TEXT)"
# Creating a new SQLite table
cursor.execute(sql)
# Committing changes and closing the connection to the database file
connection.commit()
connection.close()