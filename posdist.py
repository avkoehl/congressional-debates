#python2
from nltk import sent_tokenize
from nltk import word_tokenize
from nltk import pos_tag
import math
import pickle
import matplotlib.pyplot as plt

# Please make it stop
import sys
reload(sys)
sys.setdefaultencoding('utf-8')



""" Distribution of Part of Speech for Keyword in each Snapshot (week)
    For each week of texts, 
        [1] find all the sentences containing keyword and store in new list (to reduce time of POS tagging entire text!)
        [2] use NLTK POS Tagger to Tag all the text in the list of sentences
        [3] For keyword, count the number of each tag it has
        [4] Plot the distribution of POS for that word for each week
"""


# read in the list of texts generated by readCorpus
with open('texts.pkl', 'rb') as f:
   texts = pickle.load(f)

# Coresponding Dates for weeks 0 - 9
dates = ["Dec 03 - Dec 09", "Dec 10 - Dec 16", "Dec 17 - Dec 23", 
        "Dec 24 - Dec 30", "Dec 31 - Jan 06", "Jan 07 - Jan 13", 
        "Jan 14 - Jan 20", "Jan 21 - Jan 27", "Jan 28 - Feb 03", 
        "Feb 10 - Feb 17"]

# Now in texts[0] is all the text up to 00250023 and texts[1] has 00250023 to 00970095 and so on
# need to tokenize each element in texts and then calculate word frequencies, will use nltk
searchword = "work" #work is a good word to see multiple parts of speech
all_sentences = []
sentences = []
parts_of_speech = [] #for all the texts, should have length 9 (one for each week)

for i in range (0, len(texts)):
    parts = [] #for each text, to be appended into parts_of_speech
    raw = texts[i].decode('utf8').lower()
    all_sentences = sent_tokenize(raw)
    for sent in all_sentences:
        if searchword in sent:
            sentences.append(sent)

    for s in sentences:
        pos = pos_tag(word_tokenize(s))
        for j in range (0, len(pos)):
            if str(pos[j][0]) == searchword:
                parts.append(pos[j][1])
    parts_of_speech.append(parts)


## given all the parts of speech for the word in each text (week), calculate distributions
## Calculate the Jensen Shannon Divergence for each text (week)
for i in range(0, len(parts_of_speech)):
    print "=================================================================="
    print "Week Number:", i
    print "=================================================================="
    unique = set(parts_of_speech[i])
    total = len(parts_of_speech[i])
    for pos in unique:
        count = parts_of_speech[i].count(pos)
        dist = float(count) / float(total)
        print pos, count, 100 * dist

   # formula for Jensen Shannon Divergence
   # JSD is list with 10 values, one for each week



## Plot the Jensen Shannon Divergence Time Series for each snapshot
#plt.plot([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], JSD, 'ro')
#plt.show()


## Plot the Stacked Area time series for part of speech distribution
# not sure, look up

