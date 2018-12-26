import pymysql
import sys
mydb = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='CRUD_PB', 
)


#add contact
def add_contact():
    FName = input("Please Enter first name: ")
    LName = input("Please Enter last name: ")
    Number = input("Please Enter a number:")

     
    try:
        with mydb.cursor() as cursor:
            sql = "INSERT INTO Contacts (`firstname`,`lastname`,`number`) VALUES (%s, %s,%s)"
            try:
                cursor.execute(sql, (FName, LName, Number))
                print("Contact added successfully")
            except:
                print("Oops! Something wrong")
     
        mydb.commit()
    finally:
        return

#Display Contact
def display_contact():
    try:
        with mydb.cursor() as cursor:
            sql = "SELECT * FROM `Contacts`;"
            try:
                cursor.execute(sql)
                result = cursor.fetchall()

                print("Id\t\t First_Name \t Last_Name\t\t Number")
                print("---------------------------------------------------------------------------")
                for row in result:
                    print('%s\t\t%s\t\t%s\t\t\t%s'%(str(row[0]),row[1],row[2],row[3]))

            except:
                print("Oops! Something wrong")

        mydb.commit()
    finally:
        return

#updating the contact
def update_contact():
    display_contact()
    print("")
    contact_id = input("Enter id: ")
    Fname = input("Enter new first name: ")
    Lname = input("Enter new last name: ")
    number = input("Enter new number: ")
    try:
        with mydb.cursor() as cursor:
            sql = "UPDATE Contacts SET `firstname`=%s,`lastname`=%s,`number`=%s WHERE `contact_id`=%s;" 
            try:
                cursor.execute(sql,(Fname,Lname,number,contact_id))

                print("Successfully Updated...")

            except:
                print("Oops Somethings wrong")
           
 
        mydb.commit()
    finally:
        print ("")
        return

#deleting the contact
def delete_contact():
    display_contact()
    contact_id = input("Please Enter the ID you want to Delete:")
    try:
        with mydb.cursor() as cursor:
            sql = "DELETE FROM Contacts WHERE contact_id = " + contact_id
            try:
                cursor.execute(sql)
                print ("Deleted Successfully")

            except:
                print("Oops! Something wrong")

        mydb.commit()
    finally:
        return

#exit
def exit():
    sys.exit(0)        


#main code for choices
while True:
    print (" \tPhone_Book")
    print ("C ---> Create Product") 
    print ("R ---> Read Product")
    print ("U ---> Update Product")
    print ("D ---> Delete Product")
    print ("E ---> Exit")
    

    choices = input("Please Enter the letter of your choices: ")

    if choices in ('Cc'):
        add_contact()
    elif choices in ('Rr'):
        display_contact()
    elif choices in ("Uu"):
        update_contact()
    elif choices in ("Dd"):
        delete_contact()
    elif choices in ("Ee"):
        exit()

    else:
        print ("Invalid Input!\n")
        choices = 1
