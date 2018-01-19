#python2
import pickle
import matplotlib.pyplot as plt


# read in the list of texts generated by readCorpus
with open('texts.pkl', 'rb') as f:
   texts = pickle.load(f)

# Now in texts[0] is all the text up to 00250023 and texts[1] has 00250023 to 00970095 and so on
# need to tokenize each element in texts and then calculate word frequencies, will use nltk
searchword = "union"
freqs = []
occs = []
totals = []
for i in range (0, len(texts)):
    raw = texts[i].decode('utf8').lower()
    words = word_tokenize(raw)
    occurances = words.count(searchword)
    total = len(words)
    frequency = float(occurances) / float(total)

    occs.append(occurances)
    totals.append(total)

    if (frequency > 0):
        freqs.append(math.log10(frequency))
    else:
        freqs.append(0)

print "searchword:", searchword
for i in range(0, len(freqs)):
    print dates[i], "|", freqs[i]
    

plt.plot([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], freqs, 'ro')
plt.show()
