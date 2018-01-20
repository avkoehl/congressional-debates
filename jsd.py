# python2 
# test script to calculate Jensen Shannon Divergence
import math



# TO TEST AGAINST!!!
import numpy as np
# @author: jonathanfriedman
def jsd(x,y): #Jensen-shannon divergence
    import warnings
    warnings.filterwarnings("ignore", category = RuntimeWarning)
    x = np.array(x)
    y = np.array(y)
    d1 = x*np.log2(2*x/(x+y))
    d2 = y*np.log2(2*y/(x+y))
    d1[np.isnan(d1)] = 0
    d2[np.isnan(d2)] = 0
    d = 0.5*np.sum(d1+d2)
    return d



# all distribution matrices must have the same number of elements!
def calc_entropy( dist ):
    entropy = 0
    for d in dist:
        if d != 0:
            entropy = entropy + d * math.log(d,2)
    return -entropy

def calc_jsd ( dists ):
    weight = float(1) / len(dists)
    A = [0] * len(dists[0]) 
    B = 0
    for dist in dists:
        for i in range (len(dist)):
            A[i] = A[i] + dist[i] * weight
        B = B + weight * calc_entropy(dist)

    return calc_entropy(A) - B



dists = []
dists.append ( [.5, .5, 0])
dists.append ( [0, 0.1,.9])
c = calc_jsd(dists)

print c

d =jsd(np.array([.5 ,0.5,0]),np.array([0,0.1,0.9]))
print d

