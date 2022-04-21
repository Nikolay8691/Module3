#Registration procedure

data = {'testlog': 'testpswd'}
secret_info = '42'
i = 0

while True & i < 3:
	i += 1
	q1 = input(' Registration or login? ')
	
	if q1 == 'login':
		log = input(' Hello! Please input your login ')
		pswd = input(' Please input your password ')
		if log in data.keys() :
			if data[log] == pswd :
				print('Congratulations!!! Activation is Ok! ')
				print(secret_info)
			else : 
				print(' password is wrong, try it again!')
		else :
			print(' login is wrong! Try it again')

	elif q1 == 'registration':
		log = input(' Hello! Please input your login ')
		pswd = input(' Please input your password ')
		if log in data.keys() :
			print(' Login is busy ')
		else :
			data[log] = pswd
			print(' registration is Ok. Thanks for_joining us! ')

