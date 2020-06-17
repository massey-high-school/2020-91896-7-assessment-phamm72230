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

shapes = ["circle", "square", "rectangle", "parallelogram", "triangle", "trapezium",]

chosen_shapes = string_checker("Please choose the shape you want to calculate: ", shapes)
print(chosen_shapes)
