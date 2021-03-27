import sqlite3
connection = sqlite3.connect("test.db")
cursor = connection.cursor()

data = cursor.execute("""SELECT tblDogs.Name, tblCustomers.Name
FROM ((custDogs
INNER JOIN tblCustomers ON custDogs.CustID = tblCustomers.CustID)
INNER JOIN tblDogs ON custDogs.DogID = tblDogs.DogID)
ORDER BY tblCustomers.Name, tblDogs.Name""")
for x in data:
    print(x[0], 'is owned by', x[1])
