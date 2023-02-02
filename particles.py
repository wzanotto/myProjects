import random

def outcome(p,q):
	i = random.randint(1,q)
	if i <= p:
		return True
	return False

# In this experiment we calculate the number of particles at time = n. A particle reproduces m times every step with a probability of p/q. 
def experiment(n):
	p = 12
	q = 11
	m = 2
	population = 1
	result = outcome(1,2)
	for t in range(1,n+1):
		#print("time = ",t)
		for i in range(1,population+1):
			if outcome(p,q):
				population = population + m
				#print("a particle reproduced")
			else:
				population = population - 1
				#print("a particle has died")
			if population == 0:
				return 0
	return population

# Expected population 
def expected(N,n):
	sum = 0
	N = 10
	for i in range(0,N):
		sum = sum + experiment(n)
	return sum/N
