def reduce_haar(list_to_reduce, diff_list):
	first = []
	second = []
	c = 0
	for i in range(0,len(list_to_reduce),2):
		ave = (list_to_reduce[i]+list_to_reduce[i+1])/2
		first.append(ave)
		c += 1
		if (list_to_reduce[i] - ave) == (ave -list_to_reduce[i+1]):
			second.append((ave -list_to_reduce[i+1]))
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
		return new_list, diff_list
	else:
		return (restore_haar(new_list, diff_list))

test_list = [7,1,6,6,3,-5,4,2]
test = reduce_haar(test_list, [])
print('Result of reduction:', test)
if test[0][0] == sum(test_list)/len(test_list):
	print('Result of restoration:',restore_haar(test[0],test[1]))
else:
	print('Reduced list and average not the same.')