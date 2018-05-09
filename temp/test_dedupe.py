import os
import signal
import time
import subprocess
d_file = open('./dedup_data.txt', 'w') 
check = ['haar0', 'haar1', 'haar5', 'haar10', 'haar15', 'haar20', 'haar_sine_1', 'haar_sine_6', 'haar_sine_9', 'haar_test', 'haar_test_org']
block_size = 64
d_file.write('Block Size\tFile\tNumber of Hashes\tNumber of Unique Hashes\n')
while block_size < 262145:
	for x in check:
		d_file.write(str(block_size)+'\t'+x+'\t')
		name_list = []
		hashes = []
		c = 0
		with open('../data/'+x+'.bin', 'rb') as file:
			while True:
				file1 = open('./'+x+'_'+str(c)+'.bin', 'wb')
				name_list.append(x+'_'+str(c)+'.bin')
				c += 1
				block = file.read(block_size)
				file1.write(block)
				if not block: break
		start = len(name_list)
		d_file.write(str(start)+'\t')
		print(len(name_list))
		while len(name_list)!= 0:
			p = subprocess.Popen(['ipfs', 'add', name_list[0]], stdout=subprocess.PIPE)
			line = str(p.stdout.readline())
			if len(line) > 20:
				line = line[8:]
				line = line[:line.index(' ')]
				# print(line)
				hashes.append(line)
				os.remove('./'+name_list[0])
				del name_list[0]
			else:
				print(name_list[0], len(name_list))
				time.sleep(.25)
			p.kill()
		d_file.write(str(len(set(hashes)))+'\n')
		print(start, len(set(hashes)))
	block_size = block_size*2