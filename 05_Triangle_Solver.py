# Triangle
def areatriangle(a, b, c):
    # calculate the semi-perimeter
    s = (a + b + c) / 2
    # calculate the area using Heron's formula
    areatriangle = (s*(s-a)*(s-b)*(s-c)) ** 0.5
    return areatriangle

def perimetertriangle(a, b, c):
    # Calculate the perimeter
    perimetertriangle = a + b + c
    return perimetertriangle

def maintriangle():
    a = float(input('Enter first side: '))
    b = float(input('Enter second side: '))
    c = float(input('Enter third side: '))

    print("Area of Triangle:", areatriangle(a, b, c))
    print("Perimeter of Triangle:", perimetertriangle(a, b, c))

maintriangle()