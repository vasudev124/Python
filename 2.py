n=int(input())
for _ in range(n):
    k=int(input())
    i=1
    count=0
    while(i):
        if(i%3!=0 and i%10!=3):
            count=count+1
            if count==k:
                print(i)
                break
        i+=1



