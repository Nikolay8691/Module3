print(' welcome to Module 3 Part 3 homework 3 version 3! ')

def lmax(l) :

	parameters = [[] ,0 ,0 ,[]]
	numbers = {'figure' : parameters}

	len_max = 0
	for i in l : 
		len_i = len(str(i))
		if len_i > len_max : len_max = len_i

	for i in l :

		digits = []
		x = i
		len_i = len(str(i))

		for j in range(len_i) :
			digits.append( x % 10)
			x = x // 10
#1		print(i, ' ', digits)
		digits.reverse()
#1		print(i, ' ', digits)

#1		print('1 digits ', digits)

#		d = digits
#		print('2 digits ', digits)
		d = []
		for j in range(len_max) :
			if j < len_i : 
				d.append(digits[j])
			else :
				d.append(digits[0])

#1		print('3 digits ', digits)
#1		print('2 digits ',d)

		numbers[str(i)] = [digits ,len_i ,len_max ,d]
	del numbers['figure']

#	numbers1 = {'digits_s' : [6, 9], 'length' : 0, 'digits_f' : [6, 9, 6, 6]}
#1	print(numbers)
#	print(numbers['2'])

	l1 = []
#	l2 = [[0 for i in range(2)] for j in range(len(l))]
#	print(' list l2_0 : ', l2)

	for i in l :
		s = str(i)
		list_1p = numbers.get(s)

#		print(k, numbers[s], list_1p)

		list_2p = list_1p[3]
#1		print(list_2p)
		figure_ext = ''
		for j in list_2p :
			figure_ext += str(j)
#1		print(figure_ext)
		
		l1.append(int(figure_ext))

#1	print(' list0 : ', l)
#1	print(' list1 : ', l1)

#	for i in range(len(l)) :
#		l2[i] = [l[i], l1[i]] 

#	print(' list2 : ', l2)

	for i in range(len(l)-1) :
		for j in range(len(l)-1) :
			a = l1[j]
			b = l[j]
			if a > l1[j + 1] :
				l1[j] = l1[j + 1]
				l1[j + 1] = a 
				l[j] = l[j + 1]
				l[j + 1] = b

#1	print('l1 after sorting ; ', l1)

#1	print('l after sorting ; ', l)
	l.reverse()
#1	print('l after sorting and  reverse; ', l)

	s = ""
	for i in l : s += str(i)
#1	print(s)

	return s


#main program
l1 = [56, 9, 11, 2]
l2 = [3, 81, 5]
print(' 1st series of numbers (l1) : ', l1)
print(' Maximum composed from l1 = ', lmax(l1))
print(' 2nd series of numbers (l2) ', l2)
print(' Maximum composed from l2 = ', lmax(l2))