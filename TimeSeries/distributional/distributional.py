#python 3
import os, time, gensim

""" Distributional model for Linguistic shift time sereis construction
        For each time slot,
            [1] load in gensime word2vec modles generated wiht gensim_models.py 
            [2] align all vectors to the last vector
            [3] plot a time series of the distances between vectors
"""

##
path = '../Corpus/weeks/'
filelist = sorted(os.listdir(path))
weeks = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

