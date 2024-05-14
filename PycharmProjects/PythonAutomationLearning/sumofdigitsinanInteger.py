#sum of digits in an Integer
def sum_of_digits(n1):
    summation = 0
    while(n1>0):
        digits=n1%10
        summation+=digits
        n1=n1//10
   #print("The Sum of digits in an Integer is",summation)
    return(summation)
n=int(input("Enter the integer"))
print("The sum of digits in an Integer is",sum_of_digits(n))