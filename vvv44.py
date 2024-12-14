def fun(n):
    if n==0:
        print(n)
        return 0
    print(n)
    fun(n-1)
    print(n)
num=int(input())
fun(num)
