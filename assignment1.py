s=input("Enter your desired string:")
i=0
s1=""

for x in s:
    if s.index(x)==i:
        s1+=x
    i+=1
print(s1)