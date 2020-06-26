# Number checking function (must be a float and more than 0)
def num_check(question):
    error = "Please enter a number that is more than zero"

    valid = False
    while not valid:
        try:
            response = float(input(question))

            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# Triangle
def areatriangle(a, b, c):
    # calculate the semi-perimeter
    s = (a + b + c) / 2
    # calculate the area using Heron's formula
    areatriangle = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return areatriangle


def perimetertriangle(a, b, c):
    # Calculate the perimeter
    perimetertriangle = a + b + c
    return perimetertriangle


def maintriangle():
    a = num_check('Enter first side: ')
    b = num_check('Enter second side: ')
    c = num_check('Enter third side: ')

    print("Area of Triangle:", areatriangle(a, b, c))
    print("Perimeter of Triangle:", perimetertriangle(a, b, c))


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
    a = num_check('Enter base no.1 of Trapezium: ')
    b = num_check('Enter base no.2 of Trapezium: ')
    c = num_check('Enter side no.1 of Trapezium: ')
    d = num_check('Enter side no.2 of Trapezium: ')

    h = num_check('Enter height of Trapezium: ')

    print("Area of Trapezium:", areatrapezium(a, b, h))
    print("Perimeter of Trapezium:", perimetertrapezium(a, b, c, d))


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
    b = num_check('Enter base of Parallelogram: ')
    h = num_check('Enter height of Parallelogram: ')

    print("Area of Parallelogram:", areaparallelogram(b, h))
    print("Perimeter of Parallelogram:", perimeterparallelogram(b, h))


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
    w = num_check('Enter width of Rectangle: ')
    l = num_check('Enter length of Rectangle: ')

    print("Area of Rectangle:", arearectangle(w, l))
    print("Perimeter of Rectangle:", perimeterrectangle(w, l))

# Square
def areasquare(l):
    # Calculate the area
    areasquare = l ** 2
    return areasquare


def perimetersquare(l):
    # Calculate the perimeter
    perimetersquare = 4 * l
    return perimetersquare


def mainsquare():
    l = num_check('Enter length of Square: ')

    print("Area of Square:", areasquare(l))
    print("Perimeter of Square:", perimetersquare(l))

# Circle
def areacircle(p, r):
    # Calculate the area
    areacircle = p * r * r
    return areacircle


def circumference(p, r):
    # Calculate the perimeter
    circumference = 2 * p * r
    return circumference


def maincircle():
    r = num_check('Enter radius of Circle: ')

    print("Area of Circle:", areacircle(p, r))
    print("Circumference of Circle:", circumference(p, r))

# Get Shape
def string_checker(question, to_check):
    valid = False
    while not valid:

        response = input(question).lower()

        for item in to_check:
            if response == item:
                return response
            elif response == item[0]:
                return item

        print("sorry that is not a valid response")


# *** Main Routine starts here ***
print("1.Circle",
      "2.Square",
      "3.Rectangle",
      "4.Parallelogram",
      "5.Trapezium",
      "6.Triangle")

shapes = ["1.Circle", "2.Square", "3.Rectangle", "4.Parallelogram", "5.Trapezium", "6.Triangle",]


chosen_shapes = string_checker\
    ("Please enter the number representing the shape you want to calculate: ", shapes)
print(chosen_shapes)


if chosen_shapes in [ '1.Circle'] :
    # Circle
    p = 3.14159265359
    maincircle()

if chosen_shapes in [ '2.Square'] :
    # Square
    mainsquare()

if chosen_shapes in [ '3.Rectangle'] :
    # Rectangle
    mainrectangle()

if chosen_shapes in [ '4.Parallelogram'] :
    # Parallelogram
    mainparallelogram()

if chosen_shapes in [ '5.Trapezium'] :
    # Trapezium
    maintrapezium()

if chosen_shapes in [ '6.Triangle'] :
    # Triangle
    maintriangle()
