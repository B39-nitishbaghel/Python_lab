n=eval(input("enter the number of line"))
for i in range(1,n+1):
	for j  in range((n-i)+1,1,-1):
		print(" ",end=" ")
	for k in range(0,2*i-1):
		if i==n:
			print("*",end=" ")
		elif k==0 or k==(2*i-1)-1:
			print("*",end=" ")
		else:
			print(" ",end=" ")
	print()
