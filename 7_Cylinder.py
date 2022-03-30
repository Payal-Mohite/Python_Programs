# calculate surface volume and area of a cylinder.
radius=float(input("Enter radius of cylinder:"))
height=float(input("Enter height of cylinder:"))

Area=2*3.14*radius*height+2*3.14*radius*radius
print("Area of cylinder:",Area)

Volume=3.14*radius*radius*height
print("Volume of cylinder:",Volume)
