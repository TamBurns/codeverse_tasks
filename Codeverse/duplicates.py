#This activity is independent of any programming language 
# - so just mention the algorithm - use pseudocode.

#There is a file containing one name in each line. 
#Write the pseudocode for a program that finds the non-duplicate names (names that occur exactly once) 
# and duplicate names (names that occur more than once) in the file

#Sample input file:

#Jack
#John
#Jeff
#Jonah
#Jack
#Jonah

#Output:

#Non-duplicates:
#John
#Jeff

#Duplicates:
#Jack
#Jonah


name_list = [Jack, John, Jeff, Jonah, Jack, Jonah]
non_duplicate_list = []
dulpicate_list = []

for i in name_list:
    if i not in non_duplicate_list:
        non_duplicate_list.append(i)
    else:
        duplicate_list.append(i)


##USE DICTIONARY

dict = {"Jack": 1, "John": 1, "Jeff": 1, "Jonah": 1, "Jack": 1, "Jonah": 1}




