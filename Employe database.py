import sqlite3
con = sqlite3.connect("e://Employe.db")
cur = con.cursor()


def create_table():
    cur.execute("""
    CREATE TABLE IF NOT EXISTS Emp (
        Empid INTEGER,
        name TEXT,
        designation TEXT,
        salary INTEGER
    )
    """)

    con.commit()
    print("Table created successfully")


def insert_record():
    Eid = int(input("Enter Id: "))
    Ename = input("Enter Name: ")
    Edesig = input("Enter Designation: ")
    Esalary = int(input("Enter salary: "))

    cur.execute("INSERT INTO Emp VALUES (?, ?, ?, ?)",
        (Eid,Ename,Edesig,Esalary)
    )
    con.commit()
    print("Record inserted successfully")


def update_record():
    Eid = int(input("Enter Eid to update: "))
    Esalary = int(input("Enter new salary: "))

    cur.execute(
        "UPDATE Emp SET salary = ? WHERE Empid= ?",
        (Esalary, Eid)
    )

    con.commit()
    print("Record updated successfully")


def delete_record():
    Eid = int(input("Enter Roll No to delete: "))

    cur.execute(
        "DELETE FROM Emp WHERE Empid = ?",
        (Eid,)
    )

    con.commit()
    print("Record deleted successfully")






def select_records():
    cur.execute("SELECT * FROM Emp")

    records = cur.fetchall()
    print("-"* 60)
    print(f"\n{'Empid':<10}{'Name':<20}{'Designation':<20}{'Mark1':<10}")
    print("-" * 60)

    for r in records:
        print(f"{r[0]:<10}{r[1]:<20}{r[2]:<20}{r[3]:<10}")

while True:
    print("\n===== EMPLOYEE DATABASE =====")
    print("1. Create Table")
    print("2. Insert")
    print("3. Update")
    print("4. Delete")
    print("5. Select")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        create_table()

    elif choice == 2:
        insert_record()

    elif choice == 3:
        update_record()

    elif choice == 4:
        delete_record()

    elif choice == 5:
        select_records()

    elif choice == 6:
        break

    else:
        print("Invalid choice")

con.close()
print("Program terminated..........")
