#Build a filter function that takes a list as input and a function as input 
# and returns a list of only those items which pass the condition specified 
# in the function.


#define list
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#define function

def DividesByThree(num_list):
    for num in num_list:
        if (num % 3 == 0):
            return True
        else:
            return False


#apply function to list to give list of true and false values
#then print the numbers that correspond to the true values    
       
DividesByThree(num_list)
#print(Numbers divisible by three are', numbers_list(result = True))
    




##NEEDS BETTER DEFINITION!!!


