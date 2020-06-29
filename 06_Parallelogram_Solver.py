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