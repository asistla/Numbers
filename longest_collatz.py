#Finds the longest collatz sequence length for one million. Quite obviously, if you want to, change it to any number you want. The larger the number, the bigger your cup of coffee should be. 
#For this, a teaspoon will do.
def findcol():
	t=[]
	for i in range (1, 1000000):
		x=i
		count=1
		while x!=1:
			if x%2==0:
				x=int(x/2)
			else:
				x=3*x+1
			if x<len(t):
				if t[x-1]>=1:
					count+=t[x-1]
					break
			count+=1
		t.append(count)
	print(max(t))

findcol()
		
			
