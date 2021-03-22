n=int(input('Enter a number :'))
i=2
f=1
while i<n:
    if n%i==0:
        f=0
    i+=1
if f:
    print('Prime no')
else:
    print('Not prime')
