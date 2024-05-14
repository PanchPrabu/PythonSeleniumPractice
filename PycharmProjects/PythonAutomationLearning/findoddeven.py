#to find the number is odd or even

num=int(input("enter the number to be checked"))

def oddeven(x):
   #print("Using If-Else")
    if x%2==0:
        print("The Number is EVEN")
    else:
        print("The Number is ODD")

oddeven(num)
