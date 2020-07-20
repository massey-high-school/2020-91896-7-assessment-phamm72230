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

print ("*** m, cm, mm ***")
units = ['m', 'cm', 'mm']
unit_chosen = string_checker("What unit do you want to use?", units )
print(unit_chosen)