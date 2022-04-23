print(' welcome to Module 3 Part 2 homework! ')

l = [1, 4, 1, 6, 'hello', 'a', 5, 'hello']

l_unique = []
for i in l:
	if i not in l_unique:
		l_unique.append(i)

print('l_unique by for : ', l_unique)

l_unique = []
l_unique = list(set(l))
print('l_unique by set : ', l_unique)