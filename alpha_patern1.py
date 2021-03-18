n=eval(input("enter the number of lines of pattern"))
for i in range(1,n+1):
	ch=65
	for j in range(1,i+1):
		print(chr(ch+(j-1)),end=" ")
		
	print()
	
