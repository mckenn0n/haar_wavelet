import random
from tqdm import tqdm
import struct

cof_removed = 0
cof_number = 0
diff = 0

def reduce_haar(list_to_reduce, diff_list):
	first = []
	second = []
	c = 0
	for i in range(0,len(list_to_reduce),2):
		if i == len(list_to_reduce)-1:
			first.append(list_to_reduce[i]/2)
			# print('made it', len(list_to_reduce)-1)
			c += 1
			second.append(list_to_reduce[i]-(list_to_reduce[i]/2))
		else:
			ave = (list_to_reduce[i]+list_to_reduce[i+1])/2
			first.append(ave)
			c += 1
			# print(len(list_to_reduce), i)
			if (list_to_reduce[i] - ave) == (ave -list_to_reduce[i+1]):
				second.append((ave - list_to_reduce[i+1]))
			else:
				print('Broke')
	if c == 1:
		return first , second + diff_list
	else:
		return reduce_haar(first , second + diff_list)

def restore_haar(list_to_restore, diff_list):
	new_list = []
	for i in range(len(list_to_restore)):
		new_list.append(list_to_restore[i]+diff_list[0])
		new_list.append(list_to_restore[i]-diff_list[0])
		del diff_list[0]
		if len(diff_list) == 0:
			break
	if len(diff_list) == 0:
		return new_list, diff_list
	else:
		return (restore_haar(new_list, diff_list))

def remove_cof(diff_list, t):
	global cof_removed
	global cof_number
	cof_number = len(diff_list)
	thresh = t
	for i in range(round(len(diff_list)/2),len(diff_list)):
		if diff_list[i] <= thresh and diff_list[i] >= -thresh:
			diff_list[i] = 0.0
			cof_removed += 1
	return diff_list

for t in tqdm(range(0, 11)):
	file1 = open('./data/haar_sine_'+str(t)+'.bin', 'wb') 
	file2 = open('./data/haar_sine_'+str(t)+'.txt', 'w') 
	test_list = []
	value = 0.0
	c = 0
	up = True
	m = (262144/4)
	inc = 1
	while c != 262144:
		if up:
			test_list.append(round(value,5))
			if value >= m-inc:
				up = False
				value -= inc
			else:
				value += inc
		else:
			test_list.append(round(value,5))
			if value <= -m+inc:
				up = True
				value += inc
			else:
				value -= inc
		c += 1
	# print(test_list)
	test = reduce_haar(test_list, [])
	test = list(test)
	test[1] = remove_cof(test[1], t) 
	for x in range(len(test[1])):
		file1.write(bytearray(struct.pack('f',test[1][x])))
	print('Result of reduction:', test[1])
	val = restore_haar(test[0],test[1])
	file2.write('Original\tReconstructed\tDifference\n')
	for i in range(len(test_list)):
		file2.write(str(test_list[i])+'\t'+str(val[0][i])+'\t')
		if test_list[i] != val[0][i]:
			diff += 1
			file2.write(str(abs(abs(test_list[i])-abs(val[0][i]))))
		file2.write('\n')
	diff_ave = (diff/len(test_list)) * 100
	cof_ave = ((cof_removed/cof_number)) * 100
	file2.write(str(cof_removed) +' out of ' + str(cof_number) + ' coefficients were removed -- '+str(cof_ave)+'%\nPercent error is '+str(diff_ave)+'%')
	print('Result of restoration:', cof_removed,'\n%'+str(diff_ave)+' differnt\n% of cof diff =', cof_ave)
	cof_removed = 0
	cof_number = 0
	diff = 0