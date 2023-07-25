print(' welcome to Module 3 Part 2 homework! ')

l = [1, 4, 1, 6, 'hello', 'a', 1, 'hello']

l_unique = []
for i in l:
	if i not in l_unique:
		l_unique.append(i)

print('l_unique by for : ', l_unique)

l_unique = []
l_unique = list(set(l))
print('l_unique by set : ', l_unique)

l_repeat = []
for i in l_unique :
	j = 0
	for k in l : 
		if k == i :
			j += 1
			if j > 1 :
				l_repeat.append(i)

l_repeat_unique = []
l_repeat_unique = list(set(l_repeat))
print('repeated elements of the list : ', l_repeat_unique)

print('repeated elements of the list : ', l_repeat)

l_repeat2 = []
for i in l_unique :
	j, k = 0, 0
	while j <= 1 and k < len(l):
		if i == l[k] :
			j += 1
			if j > 1:
				l_repeat2.append(i)
		k += 1

print('repeated_2 elements of the list : ', l_repeat2)
