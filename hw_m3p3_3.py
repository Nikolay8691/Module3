print(' welcome to Module 3 Part 3 homework 3! ')

def lmax(l) :
	l_plus = {}
	l_1max = 0
	j_lmax = 1

	n = len(l)
	for j in range(n) : 
		x = l[j]
		while not (x < 10): x = x // 10
#		l_1fig[j] = x 
		l_plus[str(j)] = [l[j], x]

#	print(l_plus)

	for i in range(n - 1) :
		for j in range(n - 1):
			m = l_plus[str(j)]
			m_next = l_plus[str(j + 1)]
			if m[1] > m_next[1] :
				l_plus[str(j)] = m_next
				l_plus[str(j + 1)] = m 

#	print(l_plus)
	
	m = l_plus[str(n - 1)]
	max_figure = str(m[0])
	for j in range(2, n + 1):
		m = l_plus[str(n - j)]
		max_figure += str(m[0]) 		

	return max_figure


#main program
l1 = [56, 9, 11, 2]
l2 = [3, 81, 5]
print(' 1st series of numbers (l1) : ', l1)
print(' Maximum composed from l1 = ', lmax(l1))
print(' 2nd series of numbers (l2) ', l2)
print(' Maximum composed from l2 = ', lmax(l2))