def fun(n,a):
    if n==a:
        print(n)
        return 0
    print(n)
    fun(n-1,a)
    print(n)
num=int(input())
fun(num,1)
