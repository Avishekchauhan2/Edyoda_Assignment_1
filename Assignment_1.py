n=int(input("Enter the range from 0 of the Fibonacci series : "))
num1 = 0
num2 = 1
next_number = 0

while next_number <= n:
	print(next_number,)
	num1, num2 = num2, next_number
	next_number = num1 + num2
print()