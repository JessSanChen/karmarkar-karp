import random
import numpy as np
import math

MAX_ITER = 25000

def generate_input(n): # creates random input
    return [random.randint(1, pow(10,12)) for i in range(n)]

def random_s (n): # creates random solution set
    return [random.choice([-1,1]) for i in range(n)]

def residue (s, a): # calculates residue
    return np.dot(np.array(s), np.array(a)).tolist()

def t_iter(iter): # cooling function
    return pow(10,10)*pow(0.8, math.floor(iter/300))

def random_move(s, n): # changes input s to a neighbor s 
    res = s
    i = random.randint(1, pow(10,12))
    j = i
    while j == i: # makes sure j != i
        j = random.randint(1,pow(10,12))
    s_i = res[i]
    res[i] = -s_i
    if random.random() < 0.5:
        s_j = res[j]
        res[j] = -s_j
    return res


def repeated_random(n): 
    s = random_s(n)
    for i in range(1, MAX_ITER):
        s_prime = random_s(n)
        if residue(s_prime) < residue(s):
            s = s_prime
    return s

def hill_climbing(n):
    s = random_s(n)
    for i in range(1, MAX_ITER):
        s_prime = random_move(s,n) # random neighbor
        if residue(s_prime) < residue(s):
            s = s_prime
    return s

def simulated_annealing(n):
    s = random_s(n)
    s2 = s
    for i in range(1, MAX_ITER):
        s1 = random_move(s,n)
        res = residue(s)
        res1 = residue(s1)
        if res1 < res:
            s = s1
        else:
            if random.random() < math.exp(-((res1-res)/t_iter(i))):
                s = s1
        res2 = residue(s2)
        if res < res2: 
            s2 = s
    return s2
