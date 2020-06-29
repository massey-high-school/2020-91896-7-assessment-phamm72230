# Trapezium

def areatrapezium(a, b, h):
    # Calculate the area
    areatrapezium = ((a + b) / 2) * h
    return areatrapezium

def perimetertrapezium(a, b, c, d):
    # Calculate the perimeter
    perimetertrapezium = a + b + c + d
    return perimetertrapezium

def maintrapezium():
    a = float(input('Enter base no.1 of Trapezium: '))
    b = float(input('Enter base no.2 of Trapezium: '))
    c = float(input('Enter side no.1 of Trapezium: '))
    d = float(input('Enter side no.2 of Trapezium: '))

    h = float(input('Enter height of Trapezium: '))

    print("Area of Trapezium:", areatrapezium(a, b, h))
    print("Perimeter of Trapezium:", perimetertrapezium(a, b, c, d))

maintrapezium()