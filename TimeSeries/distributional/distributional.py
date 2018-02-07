#python 3
import os, time, gensim
from gensim.models import translation_matrix
from gensim.models import KeyedVectors
import matplotlib.pyplot as plt
from scipy import spatial

""" Distributional model for Linguistic shift time sereis construction
        For each time slot,
            [1] load in gensime word2vec modles generated wiht gensim_models.py 
            [2] align all vectors to the last vector
            [3] compute the distances between each vector and the first vector (just model["searchword"] vectors)
            *** NOT SURE ABOUT THREE, AM I LOOKING AT ALIGNING ENTIRE VECTOR OR VECTORS FOR THE WORDS ...
                I THINK JUST THE VECTORS FOR THE WORDS
            [3] plot a time series of the distances between vectors
"""

##
weeks = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
distances = []

for i in range(0, len(weeks)):
    model = gensim.models.Word2Vec.load("./models/" + str(i) + ".model")
    target = gensim.models.Word2Vec.load("./models/0.model")
    target_word = target.wv["slave"]
    current_word = model.wv["slave"]

    distances.append(spatial.distance.cosine(target_word, current_word))



plt.plot(weeks, distances, '--ro')
axes = plt.gca()
axes.set_ylim([0,1])
plt.xticks( range(0,10,1))
plt.savefig("result.png")
#plt.show()

## Plot the Stacked Area time series for part of speech distribution
# not sure, look up

