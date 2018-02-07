#python 3
import os, re, math
from nltk import pos_tag
from nltk import word_tokenize
import matplotlib.pyplot as plt

""" Distribution of Part of Speech for Keyword in each Snapshot (week)
    For each week of texts, 
        [1] find all the sentences containing keyword and store in new list (to reduce time of POS tagging entire text!)
        [2] use NLTK POS Tagger to Tag all the text in the list of sentences #update to Spacy for performance
        [3] For keyword, count the number of each tag it has
        [4] Plot the distribution of POS for that word for each week
"""
##
path = '../Corpus/weeks/'
filelist = sorted(os.listdir(path))
weeks = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


###############################################################################
### JSD CALCULATION FUNCTIONS
###############################################################################
def calc_entropy( dist ):
    entropy = 0
    for d in dist:
        if d != 0:
            entropy = entropy + d * math.log(d,2)
    return -entropy

# all distribution matrices must have the same number of elements!
def calc_jsd ( dists ):
    weight = float(1) / len(dists)
    A = [0] * len(dists[0]) 
    B = 0
    for dist in dists:
        for i in range (len(dist)):
            A[i] = A[i] + dist[i] * weight
        B = B + weight * calc_entropy(dist)

    return calc_entropy(A) - B


###############################################################################
### GET THE DISTRIBUTION FOR EACH PART OF SPEECH IN EACH TEXT
###############################################################################
searchword = "work" #work is a good word to see multiple parts of speech
distributions = []
parts_dictionary = []
for i in range (0, len(weeks)):
    with open (path + str(i) + ".txt", "r") as myfile:
        parts = [] #for each text, to be appended into parts_of_speech
        for line in myfile:
            if searchword in line:
                pos = pos_tag(word_tokenize(line))
                for j in range (0, len(pos)):
                    if str(pos[j][0]) == searchword:
                        parts.append(pos[j][1])
        
        d = []
        for pos in sorted(set(parts)):
            d.append ( round( float(parts.count(pos)) / len(parts) , 3) )
        distributions.append(d)
        parts_dictionary = set(parts)

###############################################################################
### COMPUTE THE JSDs (RELATIVE TO ORIGINAL DISTRIBUTION FROM WEEK 0)
###############################################################################
jsds = []
for i in range(0, len(distributions)):
    dists = []
    dists.append( distributions[0])
    dists.append( distributions[i])
    jsds.append(calc_jsd(dists))

###############################################################################
### PLOT THE RESULTS
###############################################################################

## Plot the Jensen Shannon Divergence Time Series for each snapshot
plt.plot(weeks, jsds, '--ro')
axes = plt.gca()
axes.set_ylim([0,.5])
plt.xticks( range(0,10,1))
plt.show()

## Plot the Stacked Area time series for part of speech distribution
# not sure, look up

