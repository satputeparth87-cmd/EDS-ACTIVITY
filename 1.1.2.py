#write your code here...
import math
n=int(input())
digits=len(str(abs(n)))

if digits == 1:
	print(n*n)
elif digits == 2:
	result=n ** (1/2)
	print(f"{result:.2f}")
elif digits == 3:
	result=n**(1/3)
	print(f"{result:.2f}")
else:
	print("Invalid")