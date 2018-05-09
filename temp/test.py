import struct
import os
import signal
import time
import subprocess

# # p = subprocess.Popen(['ipfs', 'add', 'test.py'], stdout=subprocess.PIPE)
# while True:
# 	p = subprocess.Popen(['ipfs', 'add', 'test.py'], stdout=subprocess.PIPE)
# 	time.sleep(.5)
# 	line = str(p.stdout.readline())[8:]
# 	line = line[:line.index(' ')]

# 	print(line, sep='')
# 	# break
# 	p.kill()



t = 1048577 #bits
c = 2
while c < 262144:
	print(c)
	c = c*2