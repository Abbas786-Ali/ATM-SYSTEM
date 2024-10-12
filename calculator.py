def add(a,b):
   return a+b
def subtract(a,b):
   return a-b
def multiply(a,b):
   return a*b
def division(a,b):
   return a/b
def modulas(a,b):
    return(a%b)
operation={'+':add,'-':subtract,'*':multiply,'/':division,'%':modulas}
def calculation_function():
    number1=int(input("enter the first number = "))
    for i in operation:
        print(i)
    calculation=True
    while calculation:
        operation_perform=input("enter the operation you want to perform = ")
        number2=int(input("enter the second number = "))
        calculator_function=operation[operation_perform]
        output=calculator_function(number1,number2)
        print(f"{number1} {operation_perform} {number2} = {output}")
        continue_operation=input({"press'y'to continue the operation with the output of first oprtaton'x'to exit the operation 'n'to perform new operation from first "})
        if continue_operation=='y':
            number1=output
        elif continue_operation=='n':
            calculation=False
            calculation_function()
        else:
            calculation=False
            print("good bye")
calculation_function()