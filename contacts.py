import sqlite3
        
# Connect Program to a database
con = sqlite3.connect('contacts.db')
dat = con.cursor() 

# Creating a templete to insert contacts
# ------ try to check if files exists or not then do this
# dat.execute("""CREATE TABLE contacts (
#         firstName DATATYPE,
#         lastName DATATYPE,
#         phoneNumber DATATYPE,
#         altNumber DATATYPE,
#         emailId DATATYPE,
#         relation DATATYPE
#     )""")

# Letting the user to choose b/w different options
print("My Contacts\n")
print("1. Add Contacts\n2. Edit Contacts\n3. Delete Contacts\n4. Display Contacts\n(choose one from above)\n")
option = int(input())
if option==1:
    # Taking inputs
    fName = input("First Name: ")
    lName = input("Last Name: ")
    phone = int(input("Phone Number: "))
    altPhone = int(input("Alternative Number: "))
    email = input("Email Id: ")
    relat = input("Relation: ")

    # Insert contact info to templetes
    dat.execute(f"""INSERT INTO contacts (firstName, lastName, phoneNumber, altNumber, emailId, relation) VALUES ({fName}, {lName}, {phone}, {altPhone}, {email}, {relat})""")
            
    print("Contact Saved Successfully...")
elif option==2:
    pass
elif option==3:
    pass
elif option==4:
    dat.execute("SELECT rowid, * FROM contacts")
    items = dat.fetchall()
    print("Sno.\tName\t\tPhone\tAlt. Number\tEmail\tRelation\n")
    for item in items:
        print(f"{insert[0]}.\t{insert[1]} {insert[2]}\t{insert[3]}\t{insert[4]}\t{insert[5]}\t{insert[6]}")
else:
    pass

con.commit()
con.close()