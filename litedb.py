import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = "CREATE TABLE users (id int, username text, password text)"
cursor.execute(create_table)

michaelUser = (1, 'michael', 'passwordString')

users = [
	(2, 'vinit', 'passwordString')
	(3, 'don', 'passwordString')
	(4, 'brook', 'passwordString')
	(5, 'paul', 'passwordString')	
]
insert_user = "INSERT INTO users VALUES (?, ?, ?)"
cursor.execute(insert_user, michaelUser)
cursor.executemany(insert_user, users)

select_query = "SELECT * FROM users"
for row in cursor.execute(select_query):
	print(row)

connection.commit()

connection.close()