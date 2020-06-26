# Square
def areasquare( l ):
    # Calculate the area
    areasquare= l**2
    return areasquare

def perimetersquare( l ):
    # Calculate the perimeter
    perimetersquare = 4* l
    return perimetersquare

def mainsquare():
    l = float(input('Enter length of Square: '))

    print("Area of Square:", areasquare( l ))
    print("Perimeter of Square:", perimetersquare( l ))

mainsquare()



chosen_shapes = string_checker\
    ("Please enter the number representing the shape you want to calculate: ", shapes)
print(chosen_shapes)