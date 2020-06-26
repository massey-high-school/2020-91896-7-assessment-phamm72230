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

if chosen_shapes in [ '3.Rectangle'] :
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





