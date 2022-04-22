#Studying functions

pizza_list = {'margarita': 550, 'pepperoni': 650}


# -> dict {'pizza1': cost1, 'pizza2': cost2 ...}
def add_pizza(name, cost):

	if name not in pizza_list.keys():
		pizza_list[name] = cost
		print(' new pizza is in the list. Congratulations!')
	else:
		print('it is already on the list. Get lost')

#def rmv
def del_pizza(name):
	print('not now, buddy! next time')
#if name in pizza.keys():
#	pizza.del()

def order_pizza():

	order = []
	q1 = 'yes'
	cost = 0

	while q1 != 'no':
		q1 = input (' Do you order? ')
		if q1 == 'no' : 
			print(' thank you for the order. we will be back in a few minutes! ')
#			break
		else:
			pizza_name = input(' what kind of pizza do you want to order? ')
			if pizza_name in pizza_list.keys():
				cost += pizza_list[pizza_name]
				order.append(pizza_name)
			else:
				print('we do not have this kind of pizza' )
				print('look what we have and do it again', pizza_list)
	return {'Order:': order, 'COST = ': cost}

#main program
human = input('who are you? user / admin : ')
if human == 'user' :
	print(order_pizza())
else:
	q2 = input(' you are admin! What doy want : add or remove ? ')
	if q2 == 'add' :
		newpizza_name = input('tell me new pizza name ')
		newpizza_cost = int(input(' and its price '))
		add_pizza(newpizza_name, newpizza_cost)
	else:
		delpizza_name = input(' which pizza do you want to delete? ')
		del_pizza(delpizza_name)
