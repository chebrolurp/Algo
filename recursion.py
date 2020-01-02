#find the factorial and of a number and n th fibonacci
n = int(raw_input("enter the number", ))
def factorial(n):		
	if n == 2 or n == 1:
		return n
	elif n>2:
		return n*factorial(n-1)
	else:
		print "enter a positive number"
def fibonacci(n):
	if n <= 2 :
		return 1
	else:
		return (fibonacci(n-1) + fibonacci(n-2)) 
x = factorial(n)
y = fibonacci(n)
print("factorial = "+str(x))
print(str(n) + "th fibonacci number is "+ str(y))



