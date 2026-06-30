num1 = float(input("enter the first number: "))
num2 = float(input("enter the second number: "))
operator = input("enter the operator (+,-,*,/):")

if operator == "+":
    result = num1 + num2
    print ("The result is: ", result)

elif operator == "-":
    result = num1 - num2
    print ("The result is: ", result)

elif operator == "*":
    result = num1 * num2
    print ("The result is: ", result)

elif operator == "/":
    result = num1 / num2
    print ("The result is: ", result)

else:
    print ("Invalid operator")