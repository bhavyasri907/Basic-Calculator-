def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b==0:
        return "Cannot divided by Zero"
    return a/b
print("__MENU__")
print("1.Addition\t2.Subtraction\t3.Multiplication\t4.Division")
while True:
    try:
        ch=int(input("Enter your choice:"))
        if ch==5:
            print("Exiting the Calculator>>>Good Bye..!!!")
            break
        num1=float(input("Enter first number:"))
        num2=float(input("Enter second number:"))
        if ch==1:
            print("Addition=",add(num1,num2))
        elif ch==2:
            print("Subtraction=",subtract(num1,num2))
        elif ch==3:
            print("Multiplication=",multiply(num1,num2))
        elif ch==4:
            print("Division=",divide(num1,num2))
        else:
            print("Inavlid Input")
    except ValueError:
        print("Invalid Input.Please enter numeric values only")

