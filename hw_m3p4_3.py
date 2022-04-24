print(' welcome to Module 3 Part 4 homework 2! ')
print(' ')
print(' Welcome to registration check-in! ')

import json

def login_function (login, passwd) :

	secret_info = '42'
	with open('users_data.json', 'r') as f:
		users = json.load(f)

	if login in users.keys() :
		if users[login] == passwd :
			print('Congratulations!!! activation is Ok! ')
			print(secret_info)
		else :
			print(' Sorry, password is wrong! ')
	else :
		print(' Sorry, login is wrong! ')

#	with open('users_data.json', 'w') as f:
#		json.dump(users,f)

	pass 

#main program :
login = input(' input your login : ')
passwd = input(' input your password : ')
login_function(login, passwd)

with open('users_data.json', 'r') as f:
	users_from = json.load(f)

print(users_from)
