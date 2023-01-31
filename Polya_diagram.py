import math

def V(c,d,n):
	prod=1
	for i in range(0,n):
		prod = prod*(c+i*d)
	return prod

def p(k,n,d):
	return(math.comb(n,k)*(V(c,d,k)*V(b,d,n-k))/V(b+c,d,n))

b = 1
c = 1
n = 5
# after pulling out a ball we throw it back to the urn and add d balls of the same color.
d = 100
for i in range(0,n+1):
	print("probability of pulling out {} black balls in {} draws is {}".format(i,n,p(i,n,d)))
