from art import logo
print(logo)

def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def mul(num1,num2):
    return num1*num2
def div(num1,num2):
    return num1/num2

output=0
times=1

while times>0:

    if times==1:
        first_number = float(input("Enter First Number : "))
    else:
        first_number=output
    times+=1

    print("+\n-\n*\n/")
    operator=input("Pick an Operation : ")
    second_number=float7(input("Enter Second Number : "))

    if operator=="+":
        output=add(first_number,second_number)
    elif operator=="-":
        output=sub(first_number,second_number)
    elif operator=="*":
        output=mul(first_number,second_number)
    elif operator=="/":
        output=div(first_number,second_number)
    else:
        print("Ops Wrong Input....")


    print(f"'{first_number}'{operator}'{second_number}'={output}")


    restart=input(f"Type 'y' to continue calculating with {output}, or type 'n' to start a new calculation or 'x' to exit\n")
    if restart=="y":
        continue
    elif restart=="n":
        times=1
        output=0
    elif restart=="x":
        break












