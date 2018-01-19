# PYTHON 2
import os
from nltk import word_tokenize
import math


##
path = './texts/36th/'

## sort the files into filelist
filelist = os.listdir(path)
filelist = sorted(filelist)

# page breaks weeks: 0 - 9
pages = ["00250023", "00970095", "01830181", "02120210", "02650263", "03530351", "04850483", "05870585", "07210719", "09930991"]
dates = ["Dec 03 - Dec 09", "Dec 10 - Dec 16", "Dec 17 - Dec 23", 
        "Dec 24 - Dec 30", "Dec 31 - Jan 06", "Jan 07 - Jan 13", 
        "Jan 14 - Jan 20", "Jan 21 - Jan 27", "Jan 28 - Feb 03", 
        "Feb 10 - Feb 17"]

files = []


pb = 0
fnames = []
texts = []
text = []

for i in range(0, len(filelist)):

    full = filelist[i]
    num = full.split('.')[0]
    fnames.append(full)



    with open(path + full, 'r') as myfile:
        text.append(myfile.read().replace('\n', '').replace('\r', ''))

    if (num == pages[pb]):
        files.append(" ".join(fnames))
        texts.append(" ".join(text))
        pb = pb + 1
        fnames = []
        text = []

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
    

import matplotlib.pyplot as plt
plt.plot([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], freqs, 'ro')
plt.show()
