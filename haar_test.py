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

test_list = []
value = 0.0
c = 0
up = True
m = (262144/4)
print(m)
inc = 1
file2 = open('haar_test.txt', 'w')
file2.write(str(round(value,5))+'\n')
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
	file2.write(str(round(value,5))+'\n')
	c += 1
print(len(test_list))