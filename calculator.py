num1 = int(input("Enter a Number: "))
num2 = int(input("Enter a Number: "))

operat  = input("Enter an operator(+,-,*,/,%): ")


if operat == "+" :
    print(num1+num2)
elif operat =="-":
    print(num1-num2)
elif operat == "*":
    print(num1*num2)
elif operat == "/":
    print(num1/num2)
elif operat == "%":
    print(num1%num2)
else:
    print("Enter an correct operator")   
