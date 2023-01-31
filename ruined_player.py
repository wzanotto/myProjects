import random

def outcome(p,q):
	i = random.randint(1,q)
	if i <= p:
		return True

	return False


def game(a,c,p,q):
	while  a < c and a > 0:
		if outcome(p,q):
			a = a + 1
		else:
			a = a - 1
	if a == 0:
		#print("player A is ruined.")
		return 0
	if a == c:
		#print("player A achieved his goal.")
		return 1

# this is a game where a player with an initial capital a plays a game with a probability of winning equals to p/q. He plays until he is ruined
# or until he achieves his goal. The probability of a ruin equals to ((q/p)^a - (q/p)^c)/(1 - (q/p)^c). In theory the example below converges to 
# 0.99485 which can be verified by increasing the number of repetitions.

def q():
	a = 500
	c = 550
	p = 18
	q = 38
	n = 1000
	sum = 0
	for i in range(0,n):
		if game(a,c,p,q) == 0:
			sum  = sum + 1
	return sum/n

print(q())
