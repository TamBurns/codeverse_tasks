
n = int

def fib(n):
    for i in range(n):
        if (n <= 1):                      
            print(n)

        else:
            result = fib(n-1) + fib(n-2)
            return result


fib(5)

