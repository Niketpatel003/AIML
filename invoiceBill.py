import mysql.connector
import random
from openpyxl.styles import Font, Alignment, Border, Side
from openpyxl import Workbook

def save_to_database():
    conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_invoicebill"
    )
    cursor=conn.cursor()

    cursor.execute(
        "INSERT INTO customer (invoice_number, customer_name, phone_number,grand_total) VALUES (%s, %s, %s,%s)",
        (num, name, Phonen, grandtotal)
    )

    for item in data:
        cursor.execute(
            "INSERT INTO product(product_name, product_price, product_quantiti, total_price) VALUES (%s, %s, %s, %s)",
            (item["Product Name"], item["Product Price"], item["Product Quantiti"], item["Total Price"])
        )
    conn.commit()
    cursor.close()
    conn.close()


def display():
    print("---------------Invoice Details----------------")
    print("Invoice Number:",num)
    print("Customer Name:",name)
    print("Phone Number:",Phonen)
    print("----------------------------------------------")
    print("\nProduct Name\tProduct Price\tProduct Quantiti\tTotal Price")
    for item in data:
        print(f"{item['Product Name']}\t\t{item['Product Price']}\t\t{item['Product Quantiti']}\t\t\t{item['Total Price']}")
    print("----------------------------------------------")
    print("Grand Total:",grandtotal)
    print("----------------------------------------------")

def save_to_excel():
    wb=Workbook()
    ws=wb.active
    ws.append(["Invoice Number",num])
    ws.append(["Customer Name",name])
    ws.append(["Phone Number",Phonen])
    ws.append([])
    ws.append(["Product Name","Product Price","Product Quantiti","Total Price"])
    for item in data:
        ws.append([item["Product Name"],item["Product Price"],item["Product Quantiti"],item["Total Price"]])
    ws.append([])
    ws.append(["Grand Total",grandtotal])
    wb.save("Invoice.xlsx")

    filename=f"Invoice_{num}.xlsx"
    wb.save(filename)
    print(f"Invoice saved as {filename}")

num=random.randint(0,9999)
# unique_id=input("Enter Unique ID:")
name=input("Enter Your Name:")
count=0
while count<1:
    Phonen=input("Enter Phone Number:")
    if Phonen.isdigit() and len(Phonen)==10 and Phonen[0] in ['7','8','9']:
        count+=1
    else:
        print("Invalid Number")
grandtotal=0
data=[]
while True:
        productname=input("Enter Product Name:")
        productprice=input("Enter Product Price:")
        while not productprice.isdigit():
            print("Enter a valid number")
            productprice=input("Enter Product Price:")
        productquantiti=input("Enter Product Quantiti:")
        while not productquantiti.isdigit():
            print("Enter a valid number")
            productquantiti=input("Enter Product Quantiti:")
        totalprice=int(productprice)*int(productquantiti)
        grandtotal+=totalprice
        
        data.append({
            "Product Name":productname,
            "Product Price":int(productprice),
            "Product Quantiti":int(productquantiti),
            "Total Price":totalprice
        })
        while True:
            print("1.Add Another Product")
            print("2.Remove Product")
            print("3.Update Product")
            print("4.Display Invoice")
            print("5.Exit")
            choice=input("Enter your choice:")

            if choice=="1":
                break
            elif choice=="2":
                remove_item=input("Enter the name of the product to remove:")
                for item in data:
                    if item["Product Name"].lower()==remove_item.lower():
                        grandtotal-=item["Total Price"]
                        data.remove(item)
                        print(f"{remove_item} has been removed successfully")
                        break
                else:
                    print(f"{remove_item} not found")
            elif choice=="3":
                update_item=input("Enter the name of the product to update:")
                for item in data:
                    if item["Product Name"].lower()==update_item.lower():
                        new_price=input("Enter the new price:")
                        while not new_price.isdigit():
                            print("Enter a valid number")
                            new_price=input("Enter the new price:")
                        new_quantiti=input("Enter the new quantiti:")
                        while not new_quantiti.isdigit():
                            print("Enter a valid number")
                            new_quantiti=input("Enter the new quantiti:")
                        grandtotal-=item["Total Price"]
                        item["Product Price"]=int(new_price)
                        item["Product Quantiti"]=int(new_quantiti)
                        item["Total Price"]=int(new_price)*int(new_quantiti)
                        grandtotal+=item["Total Price"]
                        print(f"{update_item} has been updated successfully")
                        break
            elif choice=="4":
                display()
            elif choice=="5":
                save_to_excel()
                save_to_database()
                break
            else:
                print("Invalid Choice")
        if choice=="5":
         break
display()
