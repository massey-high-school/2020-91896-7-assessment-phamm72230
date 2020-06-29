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
