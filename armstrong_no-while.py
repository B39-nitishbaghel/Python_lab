n= int(input("Enter a number"))
x=0
n1=n
while n!=0:
    c=n%10
    x+=pow(c,3)
    n=n//10
if n1==x:
    print('Armstrong number')
else :
    print('Not a Armstrong number')
