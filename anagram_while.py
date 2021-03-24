str1=input("Enter frist sring")
str2=input("Enter second string")
str1=sorted(str1)
str2=sorted(str2)
if len(str1)==len(str2):
    f=1
    i=0
    while i<len(str1):
        if str1[i]!=str2[i]:
            f=0
        i+=1
    if f:
        print("stings are anagram")
    else:
        print("string is not anagram")
else:
    print("string of different lenght")
