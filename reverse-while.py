n=int(input("Enter a number :"))
x=0
while n!=0:
    c=n%10
    x=(x+c)*10
    n=n//10
print(x//10)
