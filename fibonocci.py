def Fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

list1 = [x for x in range(39)]
list2 = [i for i in list1 if Fibonacci(i) % 2 == 0]
