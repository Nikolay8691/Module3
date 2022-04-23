print(' welcome to Module 3 Part 2 homework 3! ')

d = {'name1' : 'id1', 'name2' : 'id2', 'name3' : 'id3'}
print('Input dictionary : ', d)

d1 = {}
for s in d.keys() :
	new_id = d[s]
	new_value = s
	d1[new_id] = new_value

d = d1
print('Final dictionary : ', d)