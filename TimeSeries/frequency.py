#python 3
import math
import os
import re
import matplotlib.pyplot as plt

##
path = '../Corpus/weeks/'

##
filelist = sorted(os.listdir(path))

weeks = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
searchword = "state"
freqs = []
occs = []
totals = []


for i in range (0, len(weeks)):
    with open(path + str(i) + ".txt", "r") as myfile:
        doc = myfile.read()
        words = doc.split(" ")
        occurances = words.count(searchword)
        total = len(words)
        frequency = float(occurances) / float(total)

        occs.append(occurances)
        totals.append(total)

        if (frequency > 0):
            freqs.append(math.log10(frequency))
        else:
            freqs.append(0)

plt.plot([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], freqs, 'ro')
plt.show()

