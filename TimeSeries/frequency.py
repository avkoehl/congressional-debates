#python 3
import math, os, re
import matplotlib.pyplot as plt

##
path = '../Corpus/weeks/'
filelist = sorted(os.listdir(path))

weeks = ["Dec 03", "Dec 10", "Dec 17", "Dec 24", "Dec 31", "Jan 07", "Jan 14", "Jan 21", "Jan 28", "Feb 04"]
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

plt.plot(weeks, freqs, '--ro')
axes = plt.gca()
axes.set_ylim([-5,0])
plt.xticks(range(0,10,1), weeks)
plt.show()

