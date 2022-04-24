print(' welcome to Module 3 Part 3 homework 2! ')

def s5 (s, n) :
	imax = len(s)
	znaki = ['.', ',', '!', '-', '\n', ' ']
	words = []

#	print(n, ' ',s)

	j = 0
	for i in range(imax) :

#		if s[i] == ' ' or s[i] in znaki :
		if s[i] in znaki :
			if 0 < j <= n :	words.append(s[(i - j):i])
			j = 0

		else: j += 1

	return words

#main program
print(' How many words which length is less than n letters are in the text? ')				
n = int(input(' how many letters check? '))
s = '''Было просто пасмурно, дуло с севера А к обеду насчитал сто градаций серого.
Так всегда первого ноль девятого То ли весь мир сошёл с ума, то ли я - того... На столе записка от неё смятая Недопитый виски допиваю с матами.
Посмотрю в окно, допишу главу Первое сентября, дворник жжёт листву.
Серым облакам наплевать на нас Если знаешь как жить - живи
Ты хотела плыть как все - так плыви!'''

print(s5(s,n))
