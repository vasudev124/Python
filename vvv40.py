s =input()
n=len(s)-1
res=0
for i in s:
    res=res+(10**n)*ord(i)
    n-=1
print(res)
    
    
