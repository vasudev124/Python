def fun(n):
    if n==1:
        print(n)
        return 0
    print(n)
    fun(n-2)
    
    print(n)
num=int(input())
fun(num)
