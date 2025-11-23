# print("******AREA CALCULATOR******")
# print("PRESS 1 TO GET A AGER OF SQUARE")
# print("PRESS 2 TO GET A AGER OF RECTANGLE")
# print("PRESS 3 TO GET A AGER OF CIRCLE")
# print("PRESS 4 TO GET A AGER OF TRIANGLE")

# Choice = int(input("Enter a number in between 1 to 4: "))

# if Choice == 1:
#     side = float(input("Enter the length of one side: "))
#     area = side**2
#     print("The area of square is",area)

# elif Choice == 2:
#     length = float(input("Enter the length: "))
#     Widh = float(input("Enter the Widh: "))

#     area = length*Widh
#     print("The area of RECTANGLE",area)

# elif Choice == 3:
#     radius = float(input("Enter the radius of the Circle: "))
#     area = ((22%7)*(radius))
#     print = ("The area of Circle", area)

# elif Choice == 4:
#     base = float(input("Enter the radius of the TRIANGLE"))
#     height = float(input("Enter the height of the TRIANGLE"))
#     area = 0.5*base*height
#     print = ("The area of TRIANGLE", area)

# else:
#     print("invalid input")


# Buy ChatGPT

print("****** AREA CALCULATOR ******")
print("PRESS 1 TO GET AREA OF SQUARE")
print("PRESS 2 TO GET AREA OF RECTANGLE")
print("PRESS 3 TO GET AREA OF CIRCLE")
print("PRESS 4 TO GET AREA OF TRIANGLE")

choice = int(input("Enter a number between 1 to 4: "))

if choice == 1:
    side = float(input("Enter the length of one side: "))
    area = side ** 2
    print("The area of the square is", area)

elif choice == 2:
    length = float(input("Enter the length: "))
    width = float(input("Enter the width: "))  # Fixed spelling of "width"
    area = length * width
    print("The area of the rectangle is", area)

elif choice == 3:
    radius = float(input("Enter the radius of the circle: "))
    area = (22 / 7) * radius ** 2  # Use division, not modulus (%)
    print("The area of the circle is", area)

elif choice == 4:
    base = float(input("Enter the base of the triangle: "))  # Fixed label
    height = float(input("Enter the height of the triangle: "))
    area = 0.5 * base * height
    print("The area of the triangle is", area)

else:
    print("Invalid input")
