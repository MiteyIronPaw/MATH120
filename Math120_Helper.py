from math import *

def gcd(a, b):
	if b > a:
		a, b = b, a
	
	out = []
	r = 1
	
	while r != 0:
		r = a % b
		c = (a - r)//b
		
		out.append((c,b,r))
		a = b
		b = r
		
	return out


def print_gcd_working(steps):
	for step in steps:
		x = step[0] * step[1] + step[2]
		print("{} = {}({})+{}".format(x, step[0], step[1], step[2]))


def lcm(steps):
	s = steps[0]
	return (s[0] * s[1] + s[2]) * steps[0][1] // steps[-1][1]


def lcom(steps):
	i = len(steps)-1
	while i > 0:
		print(steps[i])
		i -= 1


def prime_factorise(number):
    '''Finds the prime factorisation of a number'''
    orig_num = number
    primes_under_100 = [2,3,5,7,11,13,17,19,23,27,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
    factorisation = []
    for i in primes_under_100:
        while number % i == 0:
            factorisation.append(i)
            number = number / i
        if i > sqrt(orig_num):
            break
    return factorisation 

   # make function stop if the number is too large.


steps = gcd(5460, 1148)

print_gcd_working(steps)
print("lcm " + str(lcm(steps)))
lcom(steps)
