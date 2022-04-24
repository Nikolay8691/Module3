print (' welcome to Module 3 Part 4 homework 1! - Start Part')
import json

users = {'startlogin' : 'brunoym123'}
datafile = 'users_data.json'

with open(datafile, 'w') as f:
	json.dump(users,f)
