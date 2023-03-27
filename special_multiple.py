#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER n as parameter.
#

def new_states(tab):
    states = []
    for i in range(0,len(tab)):
        states.append("0" + tab[i])
    for i in range(0,len(tab)):
        states.append("9" + tab[i])
    return states

def create_new_tab(states):
    new_tab = []
    for i in range(0,len(states)):
        new_tab.append("9"+states[i])
    return new_tab

def check(tab,n):
    for ind in range(0,len(tab)):
        if(int(tab[ind])%n==0):
            return tab[ind]
    return "-1"
        
def solve(n):
    tab = ["9"]
    states = ["0","9"]
    cond = "-1"
    while cond == "-1":
        cond = check(tab,n)
        tab = create_new_tab(states)
        states = new_states(states)
    return cond
    
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = solve(n)

        fptr.write(result + '\n')

    fptr.close()
