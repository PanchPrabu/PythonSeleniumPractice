#sorting of 3 numbers using Min Max Functions

#Gettting the Inputs from the User
n1=int(input("Enter the 1st No:"))
n2=int(input("Enter the 2nd No:"))
n3=int(input("Enter the 3rd No:"))

#Using Min and Max Functions
mi=min(n1,n2,n3)
mx=max(n1,n2,n3)
md=n1+n2+n3-mi-mx

print("The Sorting of 3 Numbers are:")
print(mi)
print(md)
print(mx)