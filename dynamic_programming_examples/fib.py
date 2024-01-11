
print("Run Normal fibonacci")

def fibonacci(n):
	if(n == 0):
		return(0)
	elif(n == 1):
		return(1)
	else:
		return(fibonacci(n-1) + fibonacci(n-2))

print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(4))
print(fibonacci(5))
print(fibonacci(6))
print(fibonacci(7))
print(fibonacci(8))


print("Run Dynamic Programming Fibonacci")

def dfibonacci(n):
	
	#Create your table for DP
	dtable = list()
	
	for x in range(n+1):
		if(x == 0):
			dtable.append(0)
		elif(x == 1):
			dtable.append(1)
		else:		
			number = dtable[x-1] + dtable[x-2]
			dtable.append(number)				


	return dtable[n]

		
print("hello world")
print(dfibonacci(0))
print(dfibonacci(1))
print(dfibonacci(2))
print(dfibonacci(3))
print(dfibonacci(4))
print(dfibonacci(5))
print(dfibonacci(6))
print(dfibonacci(7))
print(dfibonacci(8))
print(dfibonacci(50))
print(dfibonacci(100))

