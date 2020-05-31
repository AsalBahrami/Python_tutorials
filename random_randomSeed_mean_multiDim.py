import numpy as np
import random
np.random.seed(0)
# with random seed function (here specified as a numpy function)
# every time we execute the program it is not going to give us
# a different random number from the last time.
# after the first execution and generation, the array remains unchangeable.
print(np.zeros((4,3),dtype=int),'\n')
print(np.ones((6,1),dtype=int),'\n')
mean_it=np.random.normal(0,1,(3,3))

# when we pass axis argument(=0) it calculates mean of each row
# when we pass axis argument(=1) it calculates mean of each column
# if we dont pass any axis argument, mean will be calculated
# using all the elements.
print(np.mean(mean_it,axis=0),'\n')

#--------------multi dimensional array
x1=np.random.randint(1,10,size=6)
x2=np.random.randint(1,10,size=(2,3))

# the 3 dimensional array has 2 layer, 3 rows and 5 columns
x3=np.random.randint(1,10,size=(2,3,5))

# the 4 dimensional array has 2 rows of layer 3 column of layer,
# 5 rows and 9 columns.(to the best of my knowledge).
x4=np.random.randint(1,10,size=(2,3,5,9))
# and so on and so forth...

#---------------dim,size,shape
print('x3: ',x3.ndim)
# size represents the number of all elements in the list
print('x3: ',x3.size)
# how many rows and columns it has
print('x3: ',x3.shape,'\n')

# itemsize shows the size of each element in byte(here=4)
print(x3.itemsize)
# nbyetes shows the size of array in bye(here=120, because 30 elements
# each of them 4 byte).
print(x3.nbytes,'\n')
