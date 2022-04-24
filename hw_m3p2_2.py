from random import randint

n = 5
m = [[randint(0,100) for i in range(n)] for j in range(n)]

m_unique = set()
for i in range(n) : m_unique |= set(m[i])
mmax = 0
for i in m_unique :
	if i > mmax : mmax = i

print(m_unique)
print(' Maximum number in matrix m(n,n) = ', mmax)


m1 = [[9, 70, 20, 67, 33], 
      [60, 20, 94, 14,77],
      [27, 58, 45, 0, 13],
      [39, 47, 25, 97,69],
      [83, 13, 100, 1, 85]]

print(m1)

lmax = 0
for i in range(n) :
	l = m1[i]
	for j in range(n):
		if l[j] > lmax : lmax = l[j]

print(' Maximum number in matrix m1(n,n) = ', lmax)
