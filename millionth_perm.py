from sys import argv
from math import factorial

num=1000000
n=0
while factorial(n)<num:
	n+=1

s=[i for i in range(n)]

fact, perm=[None]*n, [None]*n
x, y=num, s[:]
for i in range(n):
	r, x=divmod(x, factorial(n-i-1))
	fact[i], perm[i]=r, y.pop(r)
print(str(perm))
