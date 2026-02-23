def electricityBill():
    Name=input("Enter Your Name:")
    count=0
    while count<1:
        Phonen=input("Enter Phone Number:")
        if Phonen.isdigit() and len(Phonen)==10 and Phonen[0] in ['7','8','9']:
            count+=1
        else:
            print("Invalid Number")
    Unitcoutn=input("Enter Unit Count:")
    while not Unitcoutn.isdigit():
        print("Enter a valid number")
        Unitcoutn=input("Enter Unit Count:")
    Unitcoutn=int(Unitcoutn)
    if Unitcoutn<=100:
        UnitPrice=1.5
    elif Unitcoutn>100 and Unitcoutn<=200:
        UnitPrice=2.5
    elif Unitcoutn>200 and Unitcoutn<=300:
        UnitPrice=4
    else:
        UnitPrice=6
    Fixcharge=50
    TotalPrice=Unitcoutn*UnitPrice+Fixcharge

    print("----Customer Ditails-----")
    print("Customer Name:",Name)
    print("Phone Number:",Phonen)
    print("Unit Count:",Unitcoutn)
    print("Unit Price:",UnitPrice)
    print("Fixed Charge:",Fixcharge)
    print("Total Price:",TotalPrice)

electricityBill()