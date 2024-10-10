import MySQLdb
import csv

#Create a connection
myconnection = MySQLdb.Connection(host = "localhost", user = "root", passwd = "ceit")

# Create a cursor object used to hold connection
mycursor = myconnection.cursor()

#now lets start with SQL queries
#mycursor.execute('CREATE DATABASE CEITLIBRARY')
#mycursor.execute('USE CEITLIBRARY')
tablebook = """CREATE TABLE book(bookID int primary key, title varchar(20), author varchar(20),genre varchar(20))"""
tablreader = """CREATE TABLE READER(readerID int primary key, Rname varchar(10),Phone varchar(10),BookID int)"""

book1 = """INSERT INTO book VALUES(101,"intro to Python","Tom Jerry","Programming")"""
reader1= """INSERT INTO reader VALUES( 201,"Peter P", 3267424, 101)"""

#to execute tablebook
#mycursor.execute(tablebook)
#mycursor.execute(book1)
#mycursor.execute(reader1)
#mycursor.execute('SHOW DATABASE')
file = open('book.csv')
contents = csv.reader(file)
insertVal = "INSERT INTO book (bookID, title, author,genre) VALUES (?,?,?,?)"
mycursor.executemany(insertVal,contents)
selectall = "SELECT * FROM book"
rows = mycursor.execute(selectall).fetchall()
for row in rows:
    print(row)
#to fetch data and display output
#result = mycursor.fetchall()

# commit changes
myconnection.commit()
myconnection.close()
