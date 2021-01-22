import mysql.connector as mysql
import uuid

db = mysql.connect(host="localhost",user="admin_user",password="1997",database="Test_Database")
command_handler = db.cursor(buffered=True)

def admin_work():
    while 1:
        print("\nAdmin Dashboard\n")
        print("1.Register new Teacher")
        print("2.Register new student")
        print("3.Delete existing Teacher details")
        print("4.Delete existing Student details")
        print("5.Update Teacher details")
        print("6.Update Student details")
        print("7.Logout")

        opt = str(input("\nChoose Option : "))
        if opt == "1":
            print("\nRegister New Teacher")
            username = str(input("Teacher Username : "))
            password = str(input("Password : "))
            query_vals = (username,password)
            command_handler.execute("INSERT INTO Users (username,passwd,previlage) VALUES (%s,%s,'Teacher')",query_vals)
            db.commit()
            print(username+" has successfully created")
        elif opt == "2":
            print("\nRegister New Student")
            username = str(input("Student Username : "))
            password = str(input("Password : "))
            query_vals = (username,password)
            command_handler.execute("INSERT INTO Users (username,passwd,previlage) VALUES (%s,%s,'Student')",query_vals)
            db.commit()
            print("\nUser "+username+" has been successfully created")    
        elif opt== "3":
            print("\nDelete Existing Teacher details")
            username = str(input("Teacher username: "))
            query_vals = (username,"teacher")
            command_handler.execute("DELETE FROM Users WHERE (username=%s) AND (previlage=%s)",query_vals)
            db.commit()
            if command_handler.rowcount < 1:
                print("Teacher with username :" + username +" not found.")
            else:
                print("Account deleted successfully.")    
        elif opt== "4":
            print("\nDelete Existing Student details")
            username = str(input("Student username: "))
            query_vals = (username,"Student")
            command_handler.execute("DELETE FROM Users WHERE (username=%s) AND (previlage=%s)",query_vals)
            db.commit()
            if command_handler.rowcount < 1:
                print("Teacher with username :" + username +" not found.")
            else:
                print("Account deleted successfully.")        
        elif opt=="5":
            print("\nUpdate existing teacher details")
            username = str(input("Enter Teacher username: "))
            new_username = str(input("New Username: "))
            new_password = str(input("New password: "))
            query_vals=(new_username,new_password,username,"teacher")
            command_handler.execute("UPDATE Users SET username = %s, passwd = %s WHERE (username=%s) and (previlage=%s)",query_vals)
            db.commit()
            if command_handler.rowcount <= 0:
                print("Username not found") 
            else:
                print("Details Updated successfully")
        elif opt=="6":
            print("\nUpdate Existing Student Details")
            username = str(input("Enter Student username: "))
            new_username = str(input("New Username: "))
            new_password = str(input("New password: "))
            query_vals=(new_username,new_password,username,"Student")
            command_handler.execute("UPDATE Users SET username = %s, passwd = %s WHERE (username=%s) and (previlage=%s)",query_vals)
            db.commit()
            if command_handler.rowcount <= 0:
                print("Username not found") 
            else:
                print("Details Updated successfully")    
        elif opt=="7":
            break
        else:
            print("Invalid option") 

def auth_admin():
    print("\nAdmin Login\n")
    username = str(input("Username : "))
    password = str(input("Passsword: "))
    if username == "username":
        if password == "password":
            admin_work()
        else:
            print("Incorrect password")
    else:
        print("Incorrect Username or Password.")

def teacher_work():
    while 1:
        print("\nWelcome to Teacher Dashboard.\n")
        print("1. Mark Student Attendence")
        print("2. View Student Attendence")
        print("3. Logout")

        opt = str(input("Choose an option: "))
        if opt == "1":
            print("\nMark student Attendence")
            command_handler.execute("SELECT username FROM Users WHERE (previlage='student')")
            records = command_handler.fetchall()
            date = str(input("Date - DD/MM/YYYY: "))
            for record in records:
                #return only student names without any others chars
                record = str(record).replace("'","")
                record = str(record).replace(",","")
                record = str(record).replace("(","")
                record = str(record).replace(")","")
                status = str(input("Status for "+str(record)+ " P/A/L : ")).upper()
                query_vals = (str(record),date,status)
                command_handler.execute("INSERT INTO Attendence (username,date,status) VALUES (%s,%s,%s)",query_vals)
                db.commit()
                print(str(record)+ " marked as " + status)
        elif opt == "2":
            print("\nStudent Attendence")
            date = str(input("enter date DD/MM/YYYY: "))
            query_vals = (date,)
            command_handler.execute("SELECT username,date,status FROM Attendence WHERE (date=%s)",query_vals)
            records = command_handler.fetchall()
            print("attendence list:\n")
            for record in records:
                print(record)
        elif opt == "3":
            break
        else:
            print("Invalid option")

def auth_teacher():
    print("\nTeacher Login\n")
    username = str(input("Teacher Username: "))
    password = str(input("Password: "))
    query_vals = (username,password)
    command_handler.execute("SELECT * FROM Users WHERE (username=%s) and (passwd=%s) AND (previlage='teacher')",query_vals)
    if command_handler.rowcount <= 0:
        print("User not Found.")
    else:
        teacher_work() 

def student_work(username):
    while 1:
        print("\nStudent Dashboard")
        print("1. view Attendence")
        print("2. Download Attendence")
        print("3. Logout")

        opt = str(input("Choose an option: "))
        if opt == "1":
            print("\nView Attendence")
            username = (str(username))
            query_vals = (username,)
            command_handler.execute("SELECT date,username,status FROM Attendence WHERE (username=%s)",query_vals)
            records = command_handler.fetchall()
            for record in records:
                print(record)
        elif opt == "2":
            print("\nView Attendence")
            username = (str(username))
            query_vals = (username,)
            command_handler.execute("SELECT date,username,status FROM Attendence WHERE (username=%s)",query_vals)
            records = command_handler.fetchall()
            for record in records:
                with open(str(uuid.uuid4()).replace("-","")+".doc","w") as file:
                    file.write(str(record)+ "\n")
                file.close()
            print("Downloaded successfully!!!!!!!")        
        elif opt == "3":
            break
        else:
            print("Invalid option")

def auth_student():
    print("\nStudent Login\n")
    username = str(input("Username: "))
    password = str(input("password: "))
    query_vals = (username,password)
    command_handler.execute("SELECT username FROM Users WHERE (previlage='student') AND (username=%s) AND (passwd=%s)",query_vals)
    if command_handler.rowcount <= 0:
        print("Invalid login details")
    else:
        student_work(username)    

def main():
    while 1:
        print("Welcome to the college management system\n")
        print("1. Login as Admin")
        print("2. Login as Teacher")
        print("3. Login as Student")
        print("4. Exit")
        option = str(input("\nChoose option: "))
        if option == "1":
            auth_admin()
        elif option == "2":
            auth_teacher()
        elif option == "3":
            auth_student()    
        elif option=="4":
            print("\nThank you!!!!!!!!")
            break    
        else:
            print("Invalid option selected")
main()