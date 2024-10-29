import numpy as np
from matplotlib import pyplot as plt
def circ_shift(x,m):
	N=len(x)
	y=[]
	for n in range(0,N):
		if((n-m)>=0):
			idx=(n-m)%N
		else:
			idx=N+(n-m)
		y.append(x[idx])
	return y
def circ_conv(x1,x2):
	z=[]
	a=x2[1:]
	x2r=[x2[0]]+a[::-1]
	for n in range(len(x1)):
		y=circ_shift(x2r,n)
		z.append(np.dot(x1,y))
	return z
X1=[1,2,3,4]
X2=[-1,0,5,3]
print(circ_conv(X1,X2))
	
