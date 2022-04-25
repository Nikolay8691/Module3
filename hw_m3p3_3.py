print(' welcome to Module 3 Part 3 homework 3! ')

def lmax(l) :
	l_1max = 0
	j_lmax = 1

	n = len(l)
	l_plus = [[0 for i in range(2)] for j in range(n)]

#	print(l_plus)

	for j in range(n) : 
		x = l[j]
		while not (x < 10): x = x // 10
		l_plus[j] = [l[j], x]

#	print(l_plus)

	for i in range(n - 1) :
		for j in range(n - 1):
			m = l_plus[j]
			m_next = l_plus[j + 1]
			if m[1] > m_next[1] :
				l_plus[j] = m_next
				l_plus[j + 1] = m 

#	print(l_plus)
	
	m = l_plus[n - 1]
	max_figure = str(m[0])

	for j in range(2, n + 1):
		m = l_plus[n - j]
		max_figure += str(m[0])	

	return max_figure


#main program
l1 = [56, 9, 11, 2]
l2 = [3, 81, 5]
print(' 1st series of numbers (l1) : ', l1)
print(' Maximum composed from l1 = ', lmax(l1))
print(' 2nd series of numbers (l2) ', l2)
print(' Maximum composed from l2 = ', lmax(l2))