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
    shape_list.append(['*** Triangle ***', "Area: {:.2f} {}^2".format(areatriangle (a, b, c), unit_chosen),
                       "Perimeter: {:.2f} {}".format( perimetertriangle(a, b, c), unit_chosen)])


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
    shape_list.append(['*** Triangle ***', "Area: {:.2f} {}^2".format(areatriangle2 (b,h) ,unit_chosen)])

# Trapezium
# Area of Trapezium
def areatrapezium():
    print()
    a = num_check('Enter base no.1 of Trapezium: ')
    b = num_check('Enter base no.2 of Trapezium: ')
    h = num_check('Enter height of Trapezium: ')
    print()
    # Calculate the area
    area_trapezium = ((a + b) / 2) * h
    # returns area
    print("Area of Trapezium:", area_trapezium, unit_chosen, "^2")
    # items in list for calculation history
    shape_list.append(['*** Trapezium ***',
                       "Area: {:.2f} {}^2".format(area_trapezium, unit_chosen)])
    return area_trapezium

# Perimeter of Trapezium
def perimetertrapezium():
    print()
    a = num_check('Enter base no.1 of Trapezium: ')
    b = num_check('Enter base no.2 of Trapezium: ')
    c = num_check('Enter side no.1 of Trapezium: ')
    d = num_check('Enter side no.2 of Trapezium: ')
    print()
    # Calculate the perimeter
    perimeter_trapezium = a + b + c + d
    # returns perimeter
    print("Perimeter of Trapezium:", perimeter_trapezium, unit_chosen)
    # items in list for calculation history
    shape_list.append(['*** Trapezium ***',
                       "Perimeter: {:.2f} {}".format(perimeter_trapezium, unit_chosen)])
    return perimeter_trapezium

# Parallelogram
# Area
def areaparallelogram():
    print()
    b = num_check('Enter base of Parallelogram: ')
    h = num_check('Enter height of Parallelogram: ')
    print()
    # Calculate the area
    area_parallelogram = b * h
    print("Area of Parallelogram:", area_parallelogram, unit_chosen, "^2")
    shape_list.append(['*** Parallelogram ***',
                       "Area: {:.2f} {}^2".format(area_parallelogram, unit_chosen),])

    return area_parallelogram

# Perimeter
def perimeterparallelogram():
    print()
    a = num_check('Enter side of Parallelogram: ')
    b = num_check('Enter base of Parallelogram: ')
    print()
    # Calculate the perimeter
    perimeter_parallelogram = 2 * (b + a)
    print("Perimeter of Parallelogram:", perimeter_parallelogram, unit_chosen)
    shape_list.append(['*** Parallelogram ***',
                       "Perimeter: {:.2f} {}".format(perimeter_parallelogram, unit_chosen)])

    return perimeter_parallelogram

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
    shape_list.append(['*** Rectangle ***', "Area: {:.2f} {}^2".format( arearectangle(w, l),unit_chosen),
                       "Perimeter: {:.2f} {}".format(perimeterrectangle(w, l),unit_chosen)])

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
    shape_list.append(['*** Square ***', "Area: {:.2f} {}^2".format(areasquare(l),unit_chosen),
                       "Perimeter: {:.2f} {}".format(perimetersquare(l),unit_chosen)])

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
    shape_list.append(['*** Circle ***', "Area: {:.2f} {}^2".format(areacircle(p, r),unit_chosen) ,
                       "Perimeter: {:.2f} {}".format(circumference(p, r),unit_chosen)])

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
    # List of shapes
    shapes = ["1.Circle", "2.Square", "3.Rectangle", "4.Parallelogram", "5.Trapezium", "6.Triangle",]
    print()
    # Ask user to choose a shape they want to calculate
    chosen_shapes = string_checker\
        ("Please enter the number representing the shape you want to calculate: ", shapes)
    print(chosen_shapes)

    # adds units
    print()
    print ("*** m, cm, mm ***")
    units = ['m', 'cm', 'mm']
    # Asks user which unit they want to use
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
        # Asks user if they want to calculate area or perimeter
        print("Do you want to calculate the Area or Perimeter?")
        aorppara = ['area', 'perimeter']
        aorppara_chosen = string_checker \
            ("Area or Perimeter?", aorppara)
        print(aorppara_chosen)
        if aorppara_chosen == 'area':
            # Area of Parallelogram
            areaparallelogram()
        else:
            # Perimeter of Parallelogram
            perimeterparallelogram()

    if chosen_shapes in [ '5.Trapezium'] :
        #Asks user if they want to calculate area or perimeter
        print("Do you want to calculate the Area or Perimeter?")
        aorptrap = ['area', 'perimeter']
        aorptrap_chosen = string_checker \
            ("Area or Perimeter?", aorptrap)
        print(aorptrap_chosen)
        if aorptrap_chosen == 'area':
            # Area of Trapezium
            areatrapezium()
        else:
            # Perimeter of Trapezium
            perimetertrapezium()


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

 # Calculation_History (list within a list)
print()
print("**** Calculation History ****")
print()
for item in shape_list:
    for x in item:
        print()
        print(x)
print()
