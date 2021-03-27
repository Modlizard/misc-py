import sqlite3
connection = sqlite3.connect("test.db")
cursor = connection.cursor()

cursor.execute("CREATE TABLE tblCustomers(CustID INTEGER PRIMARY KEY, Name TEXT, Telephone TEXT)")
cursor.execute("CREATE TABLE tblDogs(DogID INTEGER PRIMARY KEY, Name TEXT, Weight INTEGER, Gender TEXT)")
cursor.execute("CREATE TABLE custDogs(CustID INTEGER, DogID INTEGER, FOREIGN KEY(CustID) REFERENCES tblCustomers(CustID), FOREIGN KEY(DogID) REFERENCES tblDogs(DogID))")

