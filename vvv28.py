n=int(input())
vote=list(map(int,input().split()))
age=list(map(int,input().split()))
l1=[0]*max(vote)
for i in range(n):
    if(age[i]>=18):
        l1[vote[i]-1]+=1
m=max(l1)
c = len(l1)
l=[]
for i in range (c):
    if(l1[i]>= max(l1)):
        l.append(l1[i])
if len(l)>1 :
    print("-1")
else:
    print(l1.index(m)+1)
       


        
