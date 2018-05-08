import matplotlib.pyplot as plt

file = open('./data/haar18.txt', 'r')
l = file.readlines()[:-261149-800]
l = l[1:]
l = [i.strip('\n\t') for i in l]
l = [i.split('\t') for i in l]
x = list(range(0, len(l)))
original = []
reconstructed = []
for i in l:
	original.append(float(i[0]))
	reconstructed.append(float(i[1]))
if len(original) != len(x):
	print("Wrong")
f, axarr = plt.subplots(2, sharex=True)
axarr[0].set_title('Random Signal 18')
axarr[0].plot(x,original,'b')
axarr[1].plot(x,reconstructed,'g')
plt.show()