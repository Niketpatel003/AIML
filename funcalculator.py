def calculator():
    a=int(input("Enter the number:"))
    b=int(input("Enter the number:"))

    while True:
        print("1.Addition")
        print("2.Subtraction")
        print("3.Multiplication")
        print("4.Division")
        print("5.Exit")

        choice=int(input("Enter your choice:"))

        if choice==1:
            print("Addition is:",a+b)
        elif choice==2:
            print("Subtraction is:",a-b)
        elif choice==3:
            print("Multiplication is:",a*b)
        elif choice==4:
            if b!=0:
                print("Division is:",a/b)
            else:
                print("Cannot divide by zero")
        elif choice==5:
            break
        else:
            print("Invalid Choice")
calculator()