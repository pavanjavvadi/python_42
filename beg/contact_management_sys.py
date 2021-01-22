import mysql.connector as sql

db = sql.Connect(host="localhost",user="admin_user",password="1997",database="Test_Database")
command_handler = db.cursor(buffered=True)

def main():
    while 1:
        print("\nWelccome to Contact Management System using Python Command Line Interface\n")
        print("Main Menu")
        print("1. Save\n2. Delete\n3. Update\n4. All Contacts\n5. Logout")
        option = str(input("Choose any one option: "))

        if option == "1":
            print("\nAdd Details to save the contact")
            name = str(input("Name: "))
            phone = str(input("Phone: "))
            email = str(input("email: "))
            saveto = str(input("Save To: "))
            query_vals = (name,phone,email,saveto)
            command_handler.execute("INSERT INTO contact_list (Name,Phone,Email,SaveTo) VALUES (%s,%s,%s,%s)",query_vals)
            db.commit()
            print("Saved Successfully.")    
        elif option == "2":
            print("\nDelete Contact")
            name = str(input("Name: "))
            query_vals = (name,)
            command_handler.execute("DELETE FROM contact_list WHERE (Name=%s)",query_vals)
            db.commit()
            if command_handler.rowcount < 1:
                print("Try Again")
            else:
                print("Contact deleted")
        elif option == "3":
            print("\nUpdate Contact")
            old_name = str(input("Search contact using name: "))
            name = str(input("Name: "))
            phone = str(input("Phone: "))
            email = str(input("email: "))
            saveto = str(input("Save To: "))
            query_vals = (name,phone,email,saveto,old_name)
            command_handler.execute("UPDATE contact_list SET Name= %s,Phone=%s,Email=%s,SaveTo=%s WHERE (Name = %s)",query_vals)
            db.commit()
            if command_handler.rowcount <= 0:
                print("Try Again")
            else:
                print("Contact updated")
        elif option == "4":
            print("\nView all contacts")
            command_handler.execute("SELECT Name,Phone FROM contact_list")
            records = command_handler.fetchall()
            for record in records:
                print(record)
        elif option == "5":
            break
        else:
            print("Invalid option") 
main()