print(' welcome to Module 3 Part 4 homework 2! ')
print(' ')
print(' Welcome to registration list! Please follow instructions!')

import json

def register (login, passwd) :

	with open('users_data.json', 'r') as f:
		users = json.load(f)

	if login in users.keys() :
		print (' OOOps! This login is already on the list!')
	else :
		users[login] = passwd

	with open('users_data.json', 'w') as f:
		json.dump(users,f)

	pass 

#main program
login = input(' input your login : ')
passwd = input(' input your password : ')
register(login, passwd)

with open('users_data.json', 'r') as f:
	users_from = json.load(f)

print(users_from)
