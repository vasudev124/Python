n=int(input())
flag=0
d=0
val=0
while(n):
    d=n%10
    val+=d
    n=n//10
for i in range(2,int(val**0.5)+1):
    if val%i==0:
        flag=1
        break
if flag==1:
    print("NOT GOOGLY")
else:
    print("GOOGLY")
