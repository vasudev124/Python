n=int(input())
rev=0
while(n!=0):
    d=n%10
    rev=rev+(d**3)
    n=n//10
print(rev)
    
