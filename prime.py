n=eval(input('Enter a number :'))
for i in range(2,n):
    if n%i==0:
        print('Not a prime')
        break
else:
    if n!=1:
        print('Prime number')
    else:
        print('Not a prime')
