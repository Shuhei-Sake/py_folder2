inum_t = []
for i in range(1,101):
	inum = ''
	if i % 3 == 0:
		inum += 'fizz'
	if i % 5 == 0:
		inum += 'buzz'
	if (i % 3 != 0) and (i % 5 != 0):
		inum += str(i)
	inum_t.append(inum)
print(inum_t)

inum_t2 = []
for i in range(1, 101):
    if i % 15 == 0:
        inum_t2.append('fizzbuzz')
    elif i % 3 == 0:
        inum_t2.append('fizz')
    elif i % 5 == 0:
        inum_t2.append('buzz')
    else:
        inum_t2.append(str(i))
print(inum_t2)
