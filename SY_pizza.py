#Studying functions
import json

# 1. pizza_list = {'margarita': 550, 'pepperoni': 650}

# 2. with open('data_pizza.json', 'w') as f:
#	     json.dump(pizza_list,f)

# -> dict - pizza_list{'pizza1': cost1, 'pizza2': cost2 ...}
# -> list - order['pizza1 in order', 'pizza2 in order,...']
# -> cost - total sum of order
# -> data_pizza - json file for saving pizza_list

def add_pizza(name, cost):
	with open('data_pizza.json', 'r') as f:
		pizza_list = json.load(f)

	if name not in pizza_list.keys():
		pizza_list[name] = cost
		print(' new pizza is in the list. Congratulations!')

		with open('data_pizza.json', 'w') as f:
			json.dump(pizza_list,f)
	else:
		print('it is already on the list. Get lost')

def del_pizza(name):
#	print('not now, buddy! next time')
	with open('data_pizza.json', 'r') as f:
			pizza_list = json.load(f)

	if name in pizza_list.keys():
		del pizza_list[name]

	with open('data_pizza.json', 'w') as f:
		json.dump(pizza_list,f)

def order_pizza():

	order = []
	q1 = 'yes'
	cost = 0

	with open('data_pizza.json', 'r') as f:
		pizza_list = json.load(f)

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
	return {'Order list:': order, 'Order COST = ': cost}

#main program
print(' You are in Pizzeria! You are supposed to order pizzas... ')
while True:
	break_point = input('Stop or Continue/Go?')
	if break_point == 'Stop' or break_point == 'stop':
		break

	else:
		human = input('who are you? user / admin : ')
		if human == 'user' :
			print(order_pizza())
		else:
			q2 = input(' you are admin! What do you want : add or remove ? ')
			if q2 == 'add' :
				newpizza_name = input('tell me new pizza name ')
				newpizza_cost = int(input(' and its price '))
				add_pizza(newpizza_name, newpizza_cost)
			elif q2 == 'remove' :
				delpizza_name = input(' which pizza do you want to delete? ')
				del_pizza(delpizza_name)
			else:
				print('Nothing to do - GOOD!. See what we have on the list')
				with open('data_pizza.json', 'r') as f:
					print(json.load(f))
