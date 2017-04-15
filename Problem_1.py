max=int(input("Enter upper limit of range"))
t=[]
product=0
i=1
while product<max:
	t.append(product)
	product=3*i
	i+=1
	
product=0
i=1
while product<max:
	t.append(product)
	product=5*i
	i+=1
t=set(t)
print(sum(t))
