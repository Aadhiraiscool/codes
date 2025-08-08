try:
    number=int(input("Enter a number"))
    print("number entered is", number)
except ValueError as ex:
    print("Exception: ", ex)