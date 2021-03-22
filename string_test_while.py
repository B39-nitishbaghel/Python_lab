stri=input('enter the string')
v=c=d=s=i=0
x=len(stri)
while i<x:
    if stri[i]=='a' or stri[i]=='e' or stri[i]=='i' or stri[i]=='o' or stri[i]=='u':
        v+=1
    elif stri[i]=='A' or stri[i]=='E' or stri[i]=='I' or stri[i]=='O' or stri[i]=='U' :
        v+=1
    elif stri[i]>='A' and stri[i]<='Z' or stri[i]>='a' and stri[i]<='z':
        c+=1
    elif stri[i]>='0' and stri[i]<='9':
        d+=1
    else:
        s+=1
    i+=1
print(f'Number of vovel :{v}\nNumber of constraint :{c}\nNumber of digits :{d}\nNumber of special charater :{s}')
    
