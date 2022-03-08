#functions go here

def num_check(question):
    valid = False
    while not valid:

        error = "dont be a smartass, pick a positive number"

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
width = num_check("width: ")
height = num_check("height: ")
area = width * height
perimeter = 2 * (width * height)
print("perimeter: {} units" .format(perimeter))
print("area: {} square units" .format(area))

