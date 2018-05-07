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
plt.plot(x,original,'b')
plt.plot(x,reconstructed,'g')
plt.show()