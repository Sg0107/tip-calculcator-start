import numpy as np

# Code to generate n datapoints, returns an np array of n numbers ranging from 0
# to 10000
def data(n):
	x = np.random.randint(10001, size = n)
	print (x)
	return x	
