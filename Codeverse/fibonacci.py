#This activity is independent of any programming language - so just mention the algorithm -
#use pseudocode.

#Write the pseudocode to compute the Fibonacci series using recursion.

#Sample input:  n = 5
#Sample output: 
#0
#1
#1
#2
#3

#n = 5

#define function
#def fib(n):

 #   if (n <= 1):                      
  #      return n

   # return fib(n-1) + fib(n-2)    
    
#create list of results
#fib_seq = [fib(n) for n in range(n)]


n = int

def fib(n):
    a = 0
    b = 1
    for i in range(n):
        if (i == 0):
            print(a)
        elif (i == 1):
            print(b)
        else:
            c = a + b
            print(c)

            a = b
            b = c

fib(10)





        

