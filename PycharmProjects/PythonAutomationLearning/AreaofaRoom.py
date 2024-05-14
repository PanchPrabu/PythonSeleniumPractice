#Area of a room- simple way

length=float(input("Enter the length of the room"))
breadth=float(input("Enter the breadth of the room"))
area=length*breadth
print("Area of the room is",area,"Square Feets")

#Area of a room- using functions

def area():
    l=float(input("Enter the length of the room"))
    b=float(input("Enter the breadth of the room"))
    Area=l*b
    Area=print("Area of the room is",Area,"Sq.fts")

area()

#Area of a room- using paramaterized functions and return the values

def area(l,b):
   # l=float(input("Enter the length of the room"))
   # b=float(input("Enter the breadth of the room"))
    Area=l*b
 #  Area=print("Area of the room is",Area,"Sq.fts")
    return (Area)

area(5.5,10.5)
print(area(5.5,10.5))
