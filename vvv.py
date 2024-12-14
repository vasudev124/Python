n=int(input("Enter weight"))
if n%2!=0:
    print("NO")
else:
    x=n//2
    if x%2==0:
        print(x,x)
    else:
        print(x-1,x+1)
