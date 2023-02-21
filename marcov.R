P = c(c(1/3,1/3,1/3,0),c(1/2,1/2,0,0),c(1/4,1/4,0,1/2),c(0,1/2,0,1/2))
P = matrix(P,nrow=4,ncol=4,byrow=TRUE)

next_state <- function(state,P){
q <- runif(1,0,1)
return(findInterval(q,cumsum(P[state:]))+1)
}

next_state_rec <- function(X,P,n){
	if(n==0) return(X)
	else return(next_state_rec(next_state(X,P),P,n-1))
}

# execute an exemplary trajectory of a marcov process

x <- seq(1,10000,100)
state <- sample(states,1)
trajectory <- numeric(0)

for(x_i in x){
	trajectory <- append(trajectory,state)
	state <- next_state_rec(state,P,1)
}

plot(x,trajectory,type="l")

# stationary distribution

n <-1000
states <- 1:nrow(P)
s <- sample(states,n,replace=TRUE)
res <- numeric(0)

for(i in s){
	res <- append(res,next_state_rec(i,P,100))
}

for(state in states){
	print(length(which(res==state))/n)
}
