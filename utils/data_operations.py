import math 

import numpy as np

def euclidean_distance(x1, x2):
    ''' Euclidean distance between two poinst.'''

    return(sum([(a - b) ** 2 for a, b in zip(x1, x2)]))


x = [1, 2, 3]
y = [4, 5, 6]

print(euclidean_distance)
     

