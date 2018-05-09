import math
check = ['haar0', 'haar1', 'haar5', 'haar10', 'haar15', 'haar20', 'haar_sine_1', 'haar_sine_6', 'haar_sine_9', 'haar_test']
for x in check:
	file = open('./data/'+x+'.bin', 'rb')
	l = file.readlines()[:-2]
	l = l[1:]
	l = [i.strip('\n\t') for i in l]
	l = [i.split('\t') for i in l]
	original = []
	reconstructed = []
	diff = []
	for i in l:
		original.append(float(i[0]))
		reconstructed.append(float(i[1]))
		if len(i) == 3:
			diff.append(float(i[2]) ** 2)
	e_list.append((name,len(diff),(len(diff)/len(l))*100,math.sqrt(sum(diff)/len(l))))
print(*e_list,sep='\n')