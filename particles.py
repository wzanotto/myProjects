import random

def outcome(p,q):
	i = random.randint(1,q)
	if i <= p:
		return True
	return False

# In this experiment we calculate the number of particles at time = n. A particle transforms into new m particles every step with a probability of p/q or it disappears. 
def experiment(n):
	p = 1
	q = 2
	m = 2
	population_start = 1
	for t in range(2,n+1):
		population = 0
		print("time = ",t)
		for i in range(0,population_start):
			if outcome(p,q):
				population = population + m
				print("a particle reproduced")
		if population == 0:
			return 0
		print("number of particles at time {}: {}".format(t,population))
		population_start = population
	return population

# Expected population 
def expected(N,n):
	sum = 0
	for i in range(0,N):
		sum = sum + experiment(n)
	return sum/N
