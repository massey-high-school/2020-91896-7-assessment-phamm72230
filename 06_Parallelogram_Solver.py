# Parallelogram

def areaparallelogram(b, h):
    # Calculate the area
    areaparallelogram = b * h
    return areaparallelogram

def perimeterparallelogram(a , b ):
    # Calculate the perimeter
    perimeterparallelogram = 2 * (a + b)
    return perimeterparallelogram

def mainparallelogram():
    a = float(input('Enter side of Parallelogram: '))
    b = float(input('Enter base of Parallelogram: '))
    h = float(input('Enter height of Parallelogram: '))

    print("Area of Parallelogram:", areaparallelogram(b, h))
    print("Perimeter of Parallelogram:", perimeterparallelogram(a, b))

mainparallelogram()

