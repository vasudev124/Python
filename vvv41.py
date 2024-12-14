s=input()
n=len(s)
res=[]
for i in range(n):
    if i>2 or not(s[i]==s[i-1]==s[i-2]):
        res.append(i)
print("".join(res))
