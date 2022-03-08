#functions go here

def num_check(question):
    valid = False
    while not valid:

        error = "just pick a number over 0, not that hard"

        try:

            response = float(input(question))

            if response > 0:
                return response

            else:
                print(error)
                print()

        except ValueError:
            print(error)
        




# main routine

keep_going = ""
while keep_going == "":

    width = num_check("width: ")
    height = num_check("height: ")
    area = width * height
    perimeter = 2 * (width * height)
    print("perimeter: {:.2f} units" .format(perimeter))
    print("area: {:.2f} square units" .format(area))

    keep_going = input ("press enter to restart or any key to exit")
print()
print("area / perimeter calculator ended")