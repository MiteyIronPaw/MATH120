from math import *
import time
import sys
import itertools


def prime_check(t, ps):
	for p in ps:
		if t % p == 0:
			return False
		if p >= sqrt(t):
			break
	return True


def find_primes(x):
	'''Hayden's technique'''
	start_time = time.time()
	x = sqrt(x)

	primes = [2,3]
	t = 5
	while x > t:
				
		if prime_check(t, primes):
			primes.append(t)
		
		t += 2
	
	end_time = time.time()
	print("Took {} seconds to find primes for {}".format(round(end_time - start_time, 2), x))
	return primes





def find_primes2(number):
	'''Tom's atemp at using a Sieve it sieves out ~80% of the numbers then uses Hayden's technique'''
	start_time = time.time()
	x = round(sqrt(number))
	
	#Make list of all the numbers
	all_nums = list(range(2,x))
	
	#
	# Sieve
	#
	orgin_len = len(all_nums)
	primes = []
	while len(all_nums)/orgin_len > 0.2:
		primes.append(all_nums[0])
		
		#Make a set of all the multiples of the prime
		clash = {a*primes[-1] for a in range(1,x//primes[-1]+1)}
		
		#Remove any nums from all nums that clash
		all_nums = [y for y in all_nums if y not in clash]
	#
	# Normal method
	#
	all_nums = all_nums[::-1]
	
	t = all_nums.pop()
	
	while len(all_nums) > 0:
	
		if prime_check(t, primes):
			primes.append(t)
		
		t = all_nums.pop()
	
	#
	#Finish
	#
	end_time = time.time()
	print("Took {} seconds to find primes for {}".format(round(end_time - start_time, 2), number))
	return primes






def find_primes3(num):
	'''Method found online 10X faster than the others'''
	start_time = time.time()
	x = sqrt(num)
	
	primes = []
	for i in erat2():
		primes.append(i)
		if i > x:
			break

	end_time = time.time()
	print("Took {} seconds to find primes for {}".format(round(end_time - start_time, 2), num))
	return primes

def erat2():
    D = {}
    yield 2
    for q in itertools.islice(itertools.count(3), 0, None, 2):
        p = D.pop(q, None)
        if p is None:
            D[q*q] = q
            yield q
        else:
            x = p + q
            while x in D or not (x&1):
                x += p
            D[x] = p
    return D




def prime_fact(number, primes):
	orig_num = number
	factorisation = []
	if number in primes or number == 1 or number == 0:
		return number	
	for prime in primes:
		while number % prime == 0:
			factorisation.append(prime)
			number = number // prime
		if prime > sqrt(orig_num):
			break
	if number != 1:
		factorisation.append(number)
	result = str(factorisation[0])
	for fact in factorisation[1:]:
		result += " x " + str(fact)
	return result





NUM = 999999999999
print(prime_fact(NUM,find_primes3(NUM)))
