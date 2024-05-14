#Write a Python Program to calculate the sum of 3 given numbers,
# if the values are equal then return thrice of their sum.

n1=int(input("enter the 1st number"))
n2=int(input("enter the 2nd number"))
n3=int(input("enter the 3rd number"))

def sum_thrice(x,y,z):
    summation=x+y+z
    if x==y==z:
        summation=3*summation
        print(summation)
    else:
        print(summation)

sum_thrice(n1,n2,n3)