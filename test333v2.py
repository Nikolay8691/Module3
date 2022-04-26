print(' Hello! It is test time ')
l = [2, 69]
s = ''
for i in l : s += str(i)
#s = int(str[7, 3, 2, 79])
print(l)
print(s)

parameters = [[] ,0 ,0 ,[]]
numbers = {'figure' : parameters}
len_max = 0

for i in l :

	digits = []
	x = i
#	while not ( x = 0) :
	len_i = len(str(i))
	if len_i > len_max : len_max = len_i

	for j in range(len_i) :
		digits.append( x % 10)
		x = x // 10
#	print(i, ' ', digits)
	digits.reverse()
	print(i, ' ', digits)
	d = digits

	numbers[i] = [digits ,len_i ,len_max ,d]
del numbers['figure']

#numbers1 = {'digits_s' : [6, 9], 'length' : 0, 'digits_f' : [6, 9, 6, 6]}
print(numbers)