#python 3
import math, os, re
import matplotlib.pyplot as plt

##
path = '../Corpus/weeks/'
filelist = sorted(os.listdir(path))

weeks = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
searchword = "state"
freqs = [] 

for i in range (0, len(weeks)):
    with open(path + str(i) + ".txt", "r") as myfile:
        doc = myfile.read()
        words = doc.split(" ")
        frequency = float(words.count(searchword)) / len(words)

        if (frequency > 0):
            freqs.append(math.log10(frequency))
        else:
            freqs.append(0)

plt.plot(weeks, freqs, 'ro')
axes = plt.gca()
axes.set_ylim([-5,0])
plt.xticks( range(0,10,1))
plt.show()

