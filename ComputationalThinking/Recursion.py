
# 階層
def factorial(i):
    if i == 1:
        return 1
    else:
        return i * factorial(i-1)

# 費伯納序列
def fib(n):
    if n == 0:
        return 0
    elif n==1 or n==2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

# 盒內塔
def hanoi(n, p1, p2, p3):
    if n==1:
        print("套環從 %d 移到 %d"%(p1, p2))
    else:
        hanoi(n-1, p1, p3, p2)
        print("套環從 %d 移到 %d"%(p1, p2))
        hanoi(n-1, p2, p1, p3)

if __name__ == "__main__":
    print(factorial(5))
    print(fib(5))
    hanoi(4, 1, 2, 3) #怪怪的
