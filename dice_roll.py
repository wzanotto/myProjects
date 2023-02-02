import random

# Object of type 6 is a dice. Object of type 2 is a coin.

class Object():
	type = 6
	def __init__(self,t):
		self.type = t
	def throw(self):
		i = random.randint(1,self.type)
		return i

# A random variable returning experiment time.
def X(A):
	return len(A)

# A random outcome of an experiment.
def outcome():
	A=[]
	R=[]
	object = Object(6)
	while len(R) != object.type:
		result = object.throw()
		A.append(result)
		if result not in R:
			R.append(result)
	return A

# In this experiment we roll the dice until we get all numbers. X is a random variable returning the number of rolls. 
# We repeat the experiment n times.

def experiment(n):
	sum=0
	for i in range(0,n):
		A = outcome()
		print("{}. outcome: {}  rolls: {} \n".format(i,A,X(A)))
		sum = sum + X(A)
	print("rolls mean: ",sum/n)
	
# EX = E(X_1 + ... + X_6) = sum_i=0^{6}E(X_i) where X_i denotes the number of rolls until we roll a number different from the previous (i-1) numbers.
# X_1, ..., X_6 have geometric distribiution with probabilities (7-i)/6 thus their expected value is E(X_i) = 6/(7-i)
# By computing EX we get 6 + 3 + 2 + 1.5 + 1.2 + 1 = 14.7 which is the limit of our empirical Expected value.

experiment(1000)


