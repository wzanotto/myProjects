import random

class Dice:
	def roll(self):
		i = random.randint(1,6)
		return i

def X(A):
	return len(A)

def outcome():
	A=[]
	R=[]
	dice = Dice()
	while len(R) != 6:
		result = dice.roll()
		A.append(result)
		if result not in R:
			R.append(result)
	return A

# In this experiment we roll the dice until we get all numbers. X is a random variable returning the number of rolls. 
# Approximation of the Expected value of X.
def experiment(n):
	sum=0
	for i in range(0,n):
		A = outcome()
		print("{}. outcome: {}  rolls: {} \n".format(i,A,X(A)))
		sum = sum + X(A)
	print("rolls mean: ",sum/n)

experiment(5)


