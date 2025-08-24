angle1 = int(input("Enter first angle: "))
angle2 = int(input("Enter second angle: ")) 
angle3 = int(input("Enter third angle: "))
if angle1 + angle2 + angle3 != 180:
    print("this is not a triangle.")
elif angle1 == 90 or angle2 == 90 or angle3 == 90:
    print("This is a right triangle.")
elif angle1 > 90 or angle2 > 90 or angle3 > 90:
    print("This is an obtuse triangle.")
else:
    print("This is an acute triangle.")
