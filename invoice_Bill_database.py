import mysql.connector
import random
from datetime import datetime

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_invoicebill2"
)

cursor = conn.cursor()

while True:
    print("\n1.Create New Invoice")
    print("2.Search Invoice")
    print("3.Update Invoice")
    print("4.Delete Invoice")
    print("5.Exit")

    choise=input("Enter your choice:")

    if choise=="1":
        num = input("Enter Invoice Number:")
        name = input("Enter Your Name:")

        while True:
            Phonen = input("Enter Phone Number:")
            if Phonen.isdigit() and len(Phonen) == 10 and Phonen[0] in ['7','8','9']:
                break
            else:
                print("Invalid Number")

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS customer (
            unique_id INT AUTO_INCREMENT PRIMARY KEY,
            invoice_number VARCHAR(10),
            customer_name VARCHAR(50),
            phone_number VARCHAR(10),
            grand_total DECIMAL(10,2),
            invoice_date DATE
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS product (
            id INT AUTO_INCREMENT PRIMARY KEY,
            unique_id INT,
            product_name VARCHAR(30),
            product_price DECIMAL(10,2),
            product_quantiti INT,
            total_price DECIMAL(10,2)
        
        )
        """)
        conn.commit()

        date = datetime.now().date()

        cursor.execute(
            "INSERT INTO customer (invoice_number, customer_name, phone_number, grand_total, invoice_date) VALUES (%s,%s,%s,%s,%s)",
            (num, name, Phonen, 0, date)
        )
        conn.commit()

        unique_id = cursor.lastrowid
        grandtotal = 0

        while True:

            productname = input("Enter Product Name:")

            productprice = input("Enter Product Price:")
            while not productprice.replace('.', '', 1).isdigit():
                print("Enter a valid number")
                productprice = input("Enter Product Price:")

            productquantiti = input("Enter Product Quantity:")
            while not productquantiti.isdigit():
                print("Enter a valid number")
                productquantiti = input("Enter Product Quantity:")

            totalprice = float(productprice) * int(productquantiti)
            grandtotal += totalprice

            cursor.execute(
                "INSERT INTO product(unique_id, product_name, product_price, product_quantiti, total_price) VALUES (%s,%s,%s,%s,%s)",
                (unique_id, productname, float(productprice), int(productquantiti), totalprice)
            )

            cursor.execute(
                "UPDATE customer SET grand_total=%s WHERE unique_id=%s",
                (grandtotal, unique_id)
            )
            conn.commit()

            while True:
                print("\n1.Add Another Product")
                print("2.Exit")

                choice = input("Enter your choice:")

                if choice == "1":
                    break
                elif choice == "2":
                    break

                else:
                    print("Invalid choice. Please try again.")

            if choice == "2":
                break

        conn.commit()

        print("\n========== DISPLAY CURRENT INVOICE ==========")

        cursor.execute(
            "SELECT * FROM customer WHERE unique_id=%s",
            (unique_id,)
        )

        customer = cursor.fetchone()

        if customer:
            print("\nCustomer Details:")
            print(f"Unique ID: {customer[0]}")
            print(f"Invoice Number: {customer[1]}")
            print(f"Customer Name: {customer[2]}")
            print(f"Phone Number: {customer[3]}")
            print(f"Grand Total: {customer[4]}")
            print(f"Invoice Date: {customer[5]}")

            cursor.execute(
                "SELECT * FROM product WHERE unique_id=%s",
                (unique_id,)
            )

            products = cursor.fetchall()

            if products:
                print("\nProduct Details:")
                for product in products:
                    print(f"Product Name: {product[2]}, Price: {product[3]}, Quantity: {product[4]}, Total Price: {product[5]}")
            else:
                print("No products found.")
        else:
            print("Invoice Not Found")

    elif choise=="2":
        search_id=input("Enter Invoice Number to Search: ")

        cursor.execute("SELECT * FROM customer WHERE invoice_number=%s", (search_id,))
        customer = cursor.fetchone()

        if customer:
            print("\nCustomer Details:")
            print(f"Unique ID: {customer[0]}")
            print(f"Invoice Number: {customer[1]}")
            print(f"Customer Name: {customer[2]}")
            print(f"Phone Number: {customer[3]}")
            print(f"Grand Total: {customer[4]}")
            print(f"Invoice Date: {customer[5]}")

            cursor.execute("SELECT * FROM product WHERE unique_id=%s", (customer[0],))
            products = cursor.fetchall()

            if products:
                print("\nProduct Details:")
                for product in products:
                    print(f"Product Name: {product[2]}, Price: {product[3]}, Quantity: {product[4]}, Total Price: {product[5]}")
            else:
                print("No products found.")
        else:
            print("Invoice Not Found")

    elif choise == "3":
        search_id = input("Enter Invoice Number to Update: ")

        cursor.execute("SELECT * FROM customer WHERE invoice_number=%s", (search_id,))
        customer = cursor.fetchone()

        if customer:
            new_name = input("Enter New Customer Name:")

            while True:
                new_phone = input("Enter New Phone Number:")
                if new_phone.isdigit() and len(new_phone) == 10 and new_phone[0] in ['7','8','9']:
                    break
                else:
                    print("Invalid Number")

            cursor.execute(
                "UPDATE customer SET customer_name=%s, phone_number=%s WHERE invoice_number=%s",
                (new_name, new_phone, search_id)
            )
            conn.commit()
            print("Customer Updated Successfully")
        else:
            print("Invoice Not Found")

    elif choise == "4":
        search_id = input("Enter Invoice Number to Delete: ")
        cursor.execute("SELECT * FROM customer WHERE invoice_number=%s", (search_id,))
        customer = cursor.fetchone()
        if customer:
            cursor.execute("DELETE FROM product WHERE unique_id=%s", (customer[0],))
            cursor.execute("DELETE FROM customer WHERE invoice_number=%s", (search_id,))
            conn.commit()
            print("Invoice Deleted Successfully")
        else:
            print("Invoice Not Found")

    elif choise == "5":
        print("Exiting....")
        break
cursor.close()
conn.close()

