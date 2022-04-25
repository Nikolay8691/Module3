print(' welcome to Module 3 Part 3 homework 1! ')

from math import sqrt

def sq(a,b,c) :
	p = (a + b + c) / 2
	s = sqrt(p * (p - a) * (p - b) * (p - c))
	return s

#main program

a = int(input(' input length of side a '))
b = int(input(' input length of side a '))
c = int(input(' input length of side a '))

print(' Square of this triangle = ', sq(a, b, c))