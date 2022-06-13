# codeverse session2

# i = int(input("enter number:"))

#   if i < 5:
#        print("less than 5")
#  elif i == 5:
#       print("equal to 5")
#   else:
#       print("greaterthan 5")
#   print ("Done!")


#   if i < 10:
#       print("less than 10")
#       if i % 3 == 0:
#           print("divisible by 3")
#   else:
#       print("not less than 10")

# while loops

#   i = 0
#       while i < 3:
#       j = 0
                            #nested loop
#       while j < 3:            
#           print(i + j)
#           j = j + 1
#           i = i + 1
#   print("done!")

# Homework: Print numbers up to 200, where numbers divisible by 3, print "Free"
# and where numbers divisble by 7, print 'Heaven'. If both, print "Free Heaven".

#   i = 0

#   while i < 30:
#       print(i)
#       i = i + 1
  
#       if i % 3 == 0 and i % 7 == 0:
#           print("Free Heaven")
#       elif i % 3 == 0:
#           print("Free")
#       elif i % 7 == 0:
#           print("Heaven")

#   print("END")

# This printed 0, 1, 2, Free, 3, 4, 5, Free, 6, Heaven, 7, ....
# This is because the intruction to print i is before the if statements (consitionals)


i = 0

while i <= 30:
    i = i + 1
  
    if i % 3 == 0 and i % 7 == 0:
        print("Free Heaven")
    elif i % 3 == 0:
        print("Free")
    elif i % 7 == 0:
        print("Heaven")
    else:
        print(i)

print("END")





