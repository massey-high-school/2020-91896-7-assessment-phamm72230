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

