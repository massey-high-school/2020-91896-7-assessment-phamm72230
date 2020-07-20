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
    # calculates the semi-perimeter
    s = (a + b + c) / 2
    # calculates the area using Heron's formula
    areatriangle = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return areatriangle


def perimetertriangle(a, b, c):
    # Calculates the perimeter
    perimetertriangle = a + b + c
    return perimetertriangle


def maintriangle():
    # user input with number checking function
    a = num_check('Enter first side: ')
    b = num_check('Enter second side: ')
    c = num_check('Enter third side: ')
    # returns the area and perimeter
    print("Area of Triangle:", areatriangle (a, b, c), unit_chosen, "^2")
    print("Perimeter of Triangle:", perimetertriangle(a, b, c), unit_chosen)
    # Asks user input and adds to calculation history
    shape_list.append(['Triangle',areatriangle (a, b, c), perimetertriangle(a, b, c), unit_chosen ])


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
    # user input with number checking function
    a = num_check('Enter base no.1 of Trapezium: ')
    b = num_check('Enter base no.2 of Trapezium: ')
    c = num_check('Enter side no.1 of Trapezium: ')
    d = num_check('Enter side no.2 of Trapezium: ')
    h = num_check('Enter height of Trapezium: ')

    # returns the area and perimeter
    print("Area of Trapezium:",  areatrapezium(a, b, h), unit_chosen, "^2")
    print("Perimeter of Trapezium:", perimetertrapezium(a, b, c, d), unit_chosen)
    # Asks user input and adds to calculation history
    shape_list.append(['Trapezium', areatrapezium(a, b, h), perimetertrapezium(a, b, c, d), unit_chosen])

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
    # user input with number checking function
    b = num_check('Enter base of Parallelogram: ')
    h = num_check('Enter height of Parallelogram: ')

    # returns the area and perimeter
    print("Area of Parallelogram:", areaparallelogram(b, h), unit_chosen, "^2")
    print("Perimeter of Parallelogram:", perimeterparallelogram(b, h), unit_chosen)
    # Asks user input and adds to calculation history
    shape_list.append(['Parallelogram',  areaparallelogram(b, h), perimeterparallelogram(b, h), unit_chosen])

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
    # user input with number checking function
    w = num_check('Enter width of Rectangle: ')
    l = num_check('Enter length of Rectangle: ')

    # returns the area and perimeter
    print("Area of Rectangle:", arearectangle(w, l), unit_chosen, "^2")
    print("Perimeter of Rectangle:", perimeterrectangle(w, l), unit_chosen)
    # Asks user input and adds to calculation history
    shape_list.append(['Rectangle', arearectangle(w, l),perimeterrectangle(w, l), unit_chosen])

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
    # user input with number checking function
    l = num_check('Enter length of Square: ')

    # returns the area and perimeter
    print("Area of Square:", areasquare(l), unit_chosen, "^2")
    print("Perimeter of Square:", perimetersquare(l), unit_chosen)
    # Asks user input and adds to calculation history
    shape_list.append(['Square', areasquare(l), perimetersquare(l), unit_chosen])

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
    # user input with number checking function
    r = num_check('Enter radius of Circle: ')

    # returns the area and perimeter
    print("Area of Circle:", areacircle(p, r,),unit_chosen , "^2")
    print("Circumference of Circle:", circumference(p, r),unit_chosen )
    # Asks user input and adds to calculation history
    shape_list.append(['Circle', areacircle(p, r,), circumference(p, r), unit_chosen])

# String Checker
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

# Blank list for calculation history
shape_list = []

# *** Main Routine starts here ***
print("1.Circle",
      "2.Square",
      "3.Rectangle",
      "4.Parallelogram",
      "5.Trapezium",
      "6.Triangle")

# loops the program until user wants to stop it
keep_going = ""
while keep_going == "":

    # Get Shape
    shapes = ["1.Circle", "2.Square", "3.Rectangle", "4.Parallelogram", "5.Trapezium", "6.Triangle",]
    chosen_shapes = string_checker\
        ("Please enter the number representing the shape you want to calculate: ", shapes)
    print(chosen_shapes)

    # adds units
    print ("*** m, cm, mm ***")
    units = ['m', 'cm', 'mm']
    unit_chosen = string_checker\
        ("What unit do you want to use?", units)
    print(unit_chosen)

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

    # Calculation_History (loop within a loop)
    print("**** Calculation History ****")
    for item in shape_list:
        print("shape:{} ".format(item[0]))
        print("Area:{}{}^2 ".format( item[1],item[3]))
        print("Perimeter:{}{} ".format( item[2], item[3]))


    # allows user to stop the program whenever they choose to
    else:
        keep_going = input("Press <enter> to continue or any key to quit")
