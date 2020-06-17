# Rectangle
def arearectangle(w, l):
    # Calculate the area
    arearectangle = w * l
    return arearectangle

def perimeterrectangle(w, l):
    # Calculate the perimeter
    perimeterrectangle = 2 * (w + l)
    return perimeterrectangle

def mainrectangle():
    w = float(input('Enter width of Rectangle: '))
    l = float(input('Enter length of Rectangle: '))

    print("Area of Rectangle:", arearectangle(w, l))
    print("Perimeter of Rectangle:", perimeterrectangle(w, l))

mainrectangle()

# Square
def areasquare(w, l):
    # Calculate the area
    areasquare= w * l
    return areasquare

def perimetersquare(w, l):
    # Calculate the perimeter
    perimetersquare = 2 * (w + l)
    return perimetersquare

def mainsquare():
    w = float(input('Enter width of Square: '))
    l = float(input('Enter length of Square: '))

    print("Area of Square:", areasquare(w, l))
    print("Perimeter of Square:", perimetersquare(w, l))

mainsquare()

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

# Circle
p = 3.14159265359

def areacircle(p, r):
    # Calculate the area
    areacircle = p * r * r
    return areacircle

def circumference(p, r):
    # Calculate the perimeter
    circumference = 2 * p * r
    return circumference

def maincircle():
    r = float(input('Enter radius of Circle: '))

    print("Area of Circle:", areacircle(p, r))
    print("Circumference of Circle:", circumference(p, r))

maincircle()

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

# Parallelogram

def areaparallelogram(b, h):
    # Calculate the area
    areaparallelogram = b * h
    return areaparallelogram

def perimeterparallelogram(b, h):
    # Calculate the perimeter
    perimeterparallelogram = 2 * (b + h)
    return perimeterparallelogram

def mainparallelogram():
    b = float(input('Enter base of Parallelogram: '))
    h = float(input('Enter height of Parallelogram: '))

    print("Area of Parallelogram:", areaparallelogram(b, h))
    print("Perimeter of Parallelogram:", perimeterparallelogram(b, h))

mainparallelogram()









