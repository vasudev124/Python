def fib(num):
    f0=0
    f1=1
    if(num==0):
        return 0
    elif(num==1):
        return 1
    else:
        x=fib(num-1)+fib(num-2)
        print(x)
        return x
n=int(input())
print(fib(n))
