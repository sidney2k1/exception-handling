try:
    num1,num2=eval(input("Enter two number separated by a comma:"))
    result=num1/num2
    print("Result is",result)
except ZeroDivisionError:
    print("Division by zero is not defined")
except SyntaxError:
    print("Comma is missing. Please enter number with a comma in between like 1,2")
except:
    print("wrong input")
else:
    print("no exceptions")
finally:
    print("The code will execute no matter what")