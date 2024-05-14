#Concatenationof2StringValues

str1=str(input("Enter the 1st String:"))
str2=str(input("Enter the 2nd String:"))



#Concatenate2StringusingFunctions

def concatenate(s1,s2):
    print("The 1st String is:",s1)
    print("The 2nd String is:",s2)
    print("After concatenating the Strings are:", (str1 + str2))

concatenate(str1,str2)