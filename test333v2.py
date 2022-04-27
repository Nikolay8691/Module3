print(' Hello! It is test time ')
l = [3, 81, 5, 10, 1000]
s = ''
for i in l : s += str(i)
#s = int(str[7, 3, 2, 79])
print(l)
print(s)

parameters = [[] ,0 ,0 ,[]]
numbers = {'figure' : parameters}

len_max = 0
for i in l : 
	len_i = len(str(i))
	if len_i > len_max : len_max = len_i

for i in l :

	digits = []
	x = i
#	while not ( x = 0) :
	len_i = len(str(i))
#	if len_i > len_max : len_max = len_i

	for j in range(len_i) :
		digits.append( x % 10)
		x = x // 10
#	print(i, ' ', digits)
	digits.reverse()
	print(i, ' ', digits)

	print('1 digits ', digits)

#	d = digits
#	print('2 digits ', digits)
	d = []
	for j in range(len_max) :
		if j < len_i : 
			d.append(digits[j])
		else :
			d.append(digits[0])

	print('3 digits ', digits)
	print('2 digits ',d)

	numbers[str(i)] = [digits ,len_i ,len_max ,d]
del numbers['figure']

#numbers1 = {'digits_s' : [6, 9], 'length' : 0, 'digits_f' : [6, 9, 6, 6]}
print(numbers)
#print(numbers['2'])

l1 = []
#l2 = [[0 for i in range(2)] for j in range(len(l))]
#print(' list l2_0 : ', l2)

for i in l :
	s = str(i)
	list_1p = numbers.get(s)

#	print(k, numbers[s], list_1p)

	list_2p = list_1p[3]
	print(list_2p)
	figure_ext = ''
	for j in list_2p :
		figure_ext += str(j)
	print(figure_ext)
	
	l1.append(int(figure_ext))

print(' list0 : ', l)
print(' list1 : ', l1)

#for i in range(len(l)) :
#	l2[i] = [l[i], l1[i]] 

#print(' list2 : ', l2)

for i in range(len(l)-1) :
	for j in range(len(l)-1-i) :
		a = l1[j]
		b = l[j]
		if a > l1[j + 1] :
			l1[j] = l1[j + 1]
			l1[j + 1] = a 
			l[j] = l[j + 1]
			l[j + 1] = b

print('l1 after sorting ; ', l1)

print('l after sorting ; ', l)
l.reverse()
print('l after sorting and  reverse; ', l)

s = ""
for i in l : s += str(i)
print(s)
