n=int(input())
if n<2:
    print("NO")
elif n>=2:
    for i in range(2,n+1):
        if(n%i==0):
            print("NO")
            break
else:
    print("YES")
