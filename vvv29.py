n=int(input())
vote=list(map(int,input().split()))
age=list(map(int,input().split()))
l1=[0]*max(vote)
for i in range(n):
    if(age[i]>=18):
        l1[vote[i]-1]+=1
temp=sorted(c,reverse=True)
if temp[0]==temp[1]:
    print("1")
else:
    print(c.index(temp[0])+1)
