#Build a map function that takes a list as input and a function as input 
# and returns a list of items where the function is applied to each item 
# in the input list. 
# Eg:

#list = [1, 2, 3]
#function square(number) {
#  return number * number;
#}
#map(list, square) -> Returns [1, 4, 9]


#define list

num_list = [1, 2, 3, 4, 5, 6]
print(num_list)



#define input function

def TimesThree(num_list):
    new_list = []
    for num in num_list:
        new_list.append(num * 3)
    print(new_list)


#call function

TimesThree(num_list)





