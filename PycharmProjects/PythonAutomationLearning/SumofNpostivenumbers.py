#Program to find the sum of N postive numbers

N=int(input("Enter the postive number to find the sum of it"))
summation=int(N*(N+1)/2)
print(summation)

#Program to find the sum of N postive numbers-using functions

def summation():
    N=int(input("Enter the positive number to find the sum of it"))
    summation=int(N*(N+1)/2)
    print(summation)

summation()

#Program to find the sum of N postive numbers-using Parameterized  functionsandreturnthevalues

def sum1(N):
   #N=int(input("Enterthepositivenumbertofindthesumofit"))
    sum2=int(N*(N+1)/2)
    return sum2

sum1(10)
print(sum1(10))