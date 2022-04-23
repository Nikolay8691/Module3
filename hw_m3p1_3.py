print(' Hello! Let us calculate (Sum of figures) ')
x = int(input(' What is the number-mamba? '))

sum = 0
while x > 0:
	sum += x % 10
	x = x // 10

print('sum = ', sum)