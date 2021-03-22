n=int(input("Enter the no. of fibonacci no :"))
i=0
f1=0
f2=1
print('0')
while i<n-1:
    x=f1+f2
    f1=f2
    f2=x
    print(f1)
    i+=1
        
