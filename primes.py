#script to keep generating primes. How large the primes get depends on how much coffee you have.
#Apart from sieve methods, this performs better than the usual brute force methods that check divisors upto sqrt(n).
#This is because you don't really need to check for every number upto sqrt(n), you only need to check if the prime numbers upto sqrt(n) are a divisor.
#This means a powerful improvement. If you're finding primes upto one million for instance, you don't need to perform a thousand divisions, you only need to perform 168, as there are only 168 primes upto a thousand.

import math


def check(c, primes):
    x=int(math.sqrt(c))+1
    for i in primes:
        if c%i==0:
            return primes
        elif i>x:
            break
        else:
            continue
    primes.append(c)
    return primes





primes=[2, 3, 5]
inp=int(input("Enter upper limit for primes:"))
for i in range(7, inp, 2):
    primes=check(i, primes)
print("There are ", len(primes), "primes under ", inp)
