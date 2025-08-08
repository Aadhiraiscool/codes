try:
    num1, num2 = eval(input("Enter two numbers, seperated by a coma : "))
    result=num1 / num2
    print("Result is", result)


except ZeroDivisionError:
    print("Comma is missing. Enter numbers seperated by comma like this 1,2")

except SyntaxError :
    print("Comma is missing. Enter numbers seperated by comma like this 1,2")

except:
    print("Wrong input")


else:
    print("No exeptions")

finally:
    print("This will execute no matter what")
