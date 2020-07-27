# Number checking function (must be a float and more than 0)
def num_check(question):
    error = "!!!Please enter a number that is more than zero!!!"
    valid = False
    while not valid:
        try:
            response = float(input(question))

            if response <= 0:
                print()
                print(error)
                print()
            else:
                return response

        except ValueError:
            print()
            print(error)
            print()


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
    print()
    a = num_check('Enter first side: ')
    b = num_check('Enter second side: ')
    c = num_check('Enter third side: ')
    print()

    # returns the area and perimeter
    print("Area of Triangle:", areatriangle (a, b, c), unit_chosen, "^2")
    print("Perimeter of Triangle:", perimetertriangle(a, b, c), unit_chosen)
    # Asks user input and adds to calculation history
    shape_list.append(['Shape: Triangle', "Area: {} {}^2".format(areatriangle (a, b, c), unit_chosen),
                       "Perimeter: {} {}".format( perimetertriangle(a, b, c), unit_chosen)])


# Triangle area finder 2
def areatriangle2( b,h ):
    # calculates the area using base and height

    areatriangle2= (h * b) /2
    return areatriangle2

def maintriangle2():
    # user input with number checking function
    print()
    b = num_check('Enter base of Triangle : ')
    h = num_check('Enter height of Triangle : ')
    print()

    # returns the area
    print("Area of Triangle:", areatriangle2 (b,h), unit_chosen, "^2")
    # Asks user input and adds to calculation history
    shape_list.append(['Shape: Triangle', "Area: {} {}^2".format(areatriangle2 (b,h) ,unit_chosen)])

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
    print()
    a = num_check('Enter base no.1 of Trapezium: ')
    b = num_check('Enter base no.2 of Trapezium: ')
    c = num_check('Enter side no.1 of Trapezium: ')
    d = num_check('Enter side no.2 of Trapezium: ')
    h = num_check('Enter height of Trapezium: ')
    print()

    # returns the area and perimeter
    print("Area of Trapezium:",  areatrapezium(a, b, h), unit_chosen, "^2")
    print("Perimeter of Trapezium:", perimetertrapezium(a, b, c, d), unit_chosen)
    # Asks user input and adds to calculation history
    shape_list.append(['Shape: Trapezium',"Area: {} {}^2".format( areatrapezium(a, b, h), unit_chosen),
                       "Perimeter: {} {}".format( perimetertrapezium(a, b, c, d), unit_chosen)])

# Parallelogram
def areaparallelogram(b, h):
    # Calculate the area
    areaparallelogram = b * h
    return areaparallelogram


def perimeterparallelogram(b, a):
    # Calculate the perimeter
    perimeterparallelogram = 2 * (b + a)
    return perimeterparallelogram


def mainparallelogram():
    # user input with number checking function
    print()
    a = num_check('Enter side of Parallelogram: ')
    b = num_check('Enter base of Parallelogram: ')
    h = num_check('Enter height of Parallelogram: ')
    print()

    # returns the area and perimeter
    print("Area of Parallelogram:", areaparallelogram(b, h), unit_chosen, "^2")
    print("Perimeter of Parallelogram:", perimeterparallelogram(b, a), unit_chosen)
    # Asks user input and adds to calculation history
    shape_list.append(['Shape: Parallelogram', "Area: {} {}^2".format( areaparallelogram(b, h),unit_chosen),
                       "Perimeter: {} {}".format( perimeterparallelogram(b, a), unit_chosen)])

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
    print()
    w = num_check('Enter width of Rectangle: ')
    l = num_check('Enter length of Rectangle: ')
    print()

    # returns the area and perimeter
    print("Area of Rectangle:", arearectangle(w, l), unit_chosen, "^2")
    print("Perimeter of Rectangle:", perimeterrectangle(w, l), unit_chosen)
    # Asks user input and adds to calculation history
    shape_list.append(['Shape: Rectangle', "Area: {} {}^2".format( arearectangle(w, l),unit_chosen),
                       "Perimeter: {} {}".format(perimeterrectangle(w, l),unit_chosen)])

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
    print()
    l = num_check('Enter length of Square: ')
    print()

    # returns the area and perimeter
    print("Area of Square:", areasquare(l), unit_chosen, "^2")
    print("Perimeter of Square:", perimetersquare(l), unit_chosen)
    # Asks user input and adds to calculation history
    shape_list.append(['Shape: Square', "Area: {} {}^2".format(areasquare(l),unit_chosen),
                       "Perimeter: {} {}".format(perimetersquare(l),unit_chosen)])

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
    print()
    r = num_check('Enter radius of Circle: ')
    print()

    # returns the area and perimeter
    print("Area of Circle:", areacircle(p,r),unit_chosen , "^2")
    print("Circumference of Circle:", circumference(p, r),unit_chosen )
    # Asks user input and adds to calculation history
    shape_list.append(['Shape: Circle', "Area: {} {}^2".format(areacircle(p, r),unit_chosen) ,
                       "Perimeter: {} {}".format(circumference(p, r),unit_chosen)])

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
        print()
        print("!!!sorry that is not a valid response!!!")
        print()
# Blank list for calculation history
shape_list = []

# loops the program until user wants to stop it
keep_going = ""
while keep_going == "":

    # *** Main Routine starts here ***
    print()
    print("1.Circle",
          "2.Square",
          "3.Rectangle",
          "4.Parallelogram",
          "5.Trapezium",
          "6.Triangle")
    print()

    # Get Shape
    shapes = ["1.Circle", "2.Square", "3.Rectangle", "4.Parallelogram", "5.Trapezium", "6.Triangle",]
    print()
    chosen_shapes = string_checker\
        ("Please enter the number representing the shape you want to calculate: ", shapes)
    print(chosen_shapes)

    # adds units
    print()
    print ("*** m, cm, mm ***")
    units = ['m', 'cm', 'mm']
    unit_chosen = string_checker\
        ("What unit do you want to use?", units)
    print(unit_chosen)
    print()


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
        # When user chooses triangle asks user if they have values to all 3 sides
        print("Do you have values to all 3 sides of the Triangle?")
        answer = ['yes', 'no']
        answer_chosen = string_checker \
            ("Yes or no?", answer)
        print(answer_chosen)
        if answer_chosen == 'yes':
            # Triangle
            maintriangle()
        else:
            # Triangle area finder 2
            maintriangle2()


# allows user to stop the program whenever they choose to
    print()
    keep_going = input("Press <enter> to continue or any key to quit")
    print()

 # Calculation_History (loop within a loop)
print()
print("**** Calculation History ****")
print()
for item in shape_list:
    for x in item:
        print()
        print(x)
print()
