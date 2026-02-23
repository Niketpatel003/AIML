

name=input("Enter Your Name:")
count=0
while count<1:
    Phonen=input("Enter Phone Number:")
    if Phonen.isdigit() and len(Phonen)==10:
        count+=1
    else:
        print("Invalid Number")
Pname=input("Enter Product Name:")
Pquantiti=int(input("Enter Product Quantiti:"))
Pprice=int(input("Enter Product Price:"))
Tprice=Pquantiti*Pprice
print("Total Price is:",Tprice)

sellarstate=input("Enter the sellar state:")
buyerstate=input("Enter the buyer state:")
if sellarstate==buyerstate:
    cgst=0.09*Tprice
    sgst=0.09*Tprice
    print("CGST is:",cgst)
    print("SGST is:",sgst)
    Tprice=Tprice+cgst+sgst
    print("Total Price is:",Tprice)
else:
    igst=0.18*Tprice
    print("IGST is:",igst)
    Tprice=Tprice+igst
    print("Total Price is:",Tprice)
