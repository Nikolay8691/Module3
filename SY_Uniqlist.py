# Unique list extracting

l = [1, 2, 3, '1234', 3, 'stop']
luniq_list = []

for i in l:
	if i not in luniq_list:
		luniq_list.append(i)

print(luniq_list)

print(list(set(l)))