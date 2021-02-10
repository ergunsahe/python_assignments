import sqlite3

connection = sqlite3.connect('friend.db')
cursor = connection.cursor()

# cursor.execute('CREATE TABLE friends(first_name TEXT, last_name TEXT, age INTEGER)')
# with open('friends.txt', 'r', encoding='utf-8') as f:
#     for friend in f.readlines():
#         friends = [ x.strip() for x in friend.split(',')]
#         cursor.execute("INSERT INTO friends (first_name, last_name, age) VALUES(?,?,?)", (friends[0], friends[1], friends[2]))
        

# cursor.execute(f"CREATE TABLE users (user TEXT, pass TEXT)")

username = input("please write your name: ")
password= input("please write your password: ")

# cursor.execute(f" INSERT INTO users (user, pass) VALUES('{username}', '{password}')")

""" An example for sql injection with f string. if user type ' OR 4>3-- this peace of code password input field, he can succsfully enter without password. Therefor use not f string in sql execute command. Instead of this prefer to use tuple or dict"""
cursor.execute(f"SELECT * FROM users WHERE user='{username}' AND pass='{password}'")
if cursor.fetchone():
    print('Entry successful')
else:
    print('Entry unsuccesful')


connection.commit()
connection.close()