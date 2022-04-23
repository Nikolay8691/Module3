print('Hello! Welcome to our BY bank')
x = int(input('How much is your 1st deposit? '))
p = int(input('How much is interest rate per year? '))
y = int(input('How much money you want to make? '))
n = 0

while x < y:
	x += int(x * (p / 100))
	n = n + 1

print('You are to wait for ', n, ' years. Your sum is ', x)