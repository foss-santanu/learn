inValue = input("Enter n to calculate n!: ")
factorialOf = int(inValue) if inValue != "" else -1
factorial = 1
if factorialOf > 0:
    for x in range(factorialOf):
        factorial *= (x+1)
elif factorialOf < 0:
    factorial = None
if inValue != "":
    print("{}! = {}".format(factorialOf,factorial))
else:
    print("No number to calculate n!")