#python 3
import os, time, gensim

""" Generate the word2vec models for each time slot using gensim skip grams model
        For each time slot,
            [1] use gensim to computer the word2vec model (skip grams sg=1)
"""

##
path = '../Corpus/weeks/'
filelist = sorted(os.listdir(path))
weeks = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


## loop through the texts for each week and compute word2vec model
##  Store the model under 0_model.txt, 1_model.txt ...

for i in range (0, len(weeks)):
    with open (path + str(i) + ".txt", "r") as myfile:
        print ("Training Model ", i, " ...")
        start = time.time()
        model = gensim.models.Word2Vec(myfile.readlines(), sg=1)
        model.save("./models/" + str(i)+".model")
        end = time.time()
        print ("time elapsed: ", end - start)
