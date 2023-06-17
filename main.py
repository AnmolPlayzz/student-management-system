import mysql.connector as sql
db = sql.connect(
    host="localhost",
    user="root",
    password="root",
    database="student_management")
cur=db.cursor()

for j in range(5):
    cur.execute('SHOW tables;')
    res = cur.fetchall()
    myres=[]
    for i in res:
        myres+=[i[0]]
    if 'students' not in myres:
        sql="""CREATE TABLE Students (
        student_id INT PRIMARY KEY,
        first_name VARCHAR(50),
        last_name VARCHAR(50),
        phone VARCHAR(20)
        );"""
        cur.execute(sql)
    elif 'attendance' not in myres:
        sql="""CREATE TABLE Attendance (
        attendance_id INT PRIMARY KEY,
        student_id INT,
        date DATE,
        status VARCHAR(10)
        );
        """
        cur.execute(sql)
def manage_student():
    print(f"""
 _____________________________________________________
|                                                     |
|                >  Manage Student  <                 |
|                                                     | 
|-----------------------------------------------------|
|                                                     |
|                        MENU                         |
|                        -  -                         |
|               [1] - Add Student                     | 
|               [2] - Remove Student                  |
|               [3] - Update Student                  |
|               [4] - Search Student                  |
|               [5] - List Students                   |
|               [0] - Main Menu                       |
|                                                     |
 ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾

↓ Enter your choice and press Enter""")
    c=int(input(""))
    if c==1:
        print("-------[    Adding new Student    ]-------")
        s_id=int(input("Enter Student ID: "))
        f_na=input("Enter First Name: ")
        l_na=input("Enter Last Name: ")
        s_p=input("Enter Phone Number: ")
        data=(s_id,f_na,l_na,s_p)
        sql="INSERT INTO Students VALUES (%s,%s,%s,%s)"
        cur.execute(sql, data)
        db.commit()
        print("-------[    ✅ Student Added     ]-------")
    elif c==2:
        print("-------[    Removing a Student    ]-------")
        s_id=(int(input("Enter Student ID: ")),)
        sql="DELETE FROM Students WHERE Student_ID = %s"
        cur.execute(sql,s_id)
        db.commit()
        print("-------[   ✅ Student Deleted     ]-------")
    elif c==3:
        print("-------[    Updating a Student    ]-------")
        s_id=int(input("Enter Student ID: "))
        f_na=input("Enter First Name: ")
        l_na=input("Enter Last Name: ")
        s_p=input("Enter Phone Number: ")
        v=(f_na,l_na,s_p,s_id)
        sql="UPDATE Students SET First_Name = %s, Last_Name = %s, Phone = %s WHERE Student_ID=%s"
        cur.execute(sql,v)
        db.commit()
        print("-------[    ✅ Student Updated    ]-------")
    elif c==4:
        data=(int(input("Enter Student ID: ")),)
        sql="SELECT * FROM Students WHERE Student_id=%s"
        cur.execute(sql,data)
        res=cur.fetchall()
        print("STUDENT ID\tFIRST NAME\tLAST NAME\tPHONE")
        for i in res:
            for j in i:
                print(j,end="\t\t")
            print()
    elif c==5:
        sql="SELECT * FROM Students"
        cur.execute(sql)
        res=cur.fetchall()
        print("STUDENT ID\tFIRST NAME\tLAST NAME\tPHONE")
        for i in res:
            for j in i:
                print(j,end="\t\t")
            print()
    elif c==0:
        main()
    else:
        print("-------[  ❌ Invalid Input  ]--------")
    manage_student()
def manage_attendance():
    print(f"""
 _____________________________________________________
|                                                     |
|               >  Manage Attendance  <               |
|                                                     | 
|-----------------------------------------------------|
|                                                     |
|                        MENU                         |
|                        -  -                         |
|               [1] - Mark Attendance                 | 
|               [2] - Retrieve Attendance             |
|               [3] - List all Records                |
|               [0] - Main Menu                       |
|                                                     |
 ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾

↓ Enter your choice and press Enter""")
    c=int(input(""))
    if c==1:
        print("-------[    Adding new Attendance Record    ]-------")
        a_id=int(input("Enter Attendance ID: "))
        s_id=int(input("Enter Student ID: "))
        date=input("Enter Date [yyyy-mm-dd]: ")
        st=input("Enter Status: ")
        data=(a_id,s_id,date,st)
        sql="INSERT INTO Attendance VALUES (%s,%s,%s,%s)"
        cur.execute(sql,data)
        db.commit()
        print("-------[    ✅ Attendance Record Added    ]-------")
    if c==2:
        print("-------[    Retrieving Attendance Records    ]-------")
        print("""You can use 2 methods to fetch the records:
[1] - by Student ID
[2] - by Date
        """)
        me=int(input("What data would you like to use to retireve record?\n->"))
        if me==1:
            s_id=(int(input("Enter Student ID: ")),)
            sql="SELECT * FROM Attendance WHERE Student_id=%s"
            cur.execute(sql,s_id)
            res=cur.fetchall()
            print("ATTENDACE ID\tSTUDENT ID\tDATE\t\t\tSTATUS")
            for i in res:
                for j in i:
                    print(j,end="\t\t")
                print()
        elif me==2:
            date=(input("Enter Date: "),)
            sql="SELECT * FROM Attendance WHERE Date=%s"
            cur.execute(sql,date)
            res=cur.fetchall()
            print("ATTENDACE ID\tSTUDENT ID\tDATE\t\t\tSTATUS")
            for i in res:
                for j in i:
                    print(j,end="\t\t")
                print()
    elif c==3:
        sql="SELECT * FROM Attendance"
        cur.execute(sql)
        res=cur.fetchall()
        print("ATTENDACE ID\tSTUDENT ID\tDATE\t\t\tSTATUS")
        for i in res:
            for j in i:
                print(j,end="\t\t")
            print()
    elif c==0:
        main()
    else:
        print("-------[  ❌ Invalid Input  ]--------")
    manage_attendance()
def main():
    print("""
 _____________________________________________________
|                                                     |
|               > Student Management <                |
|                      System                         |
|                                                     |
|-----------------------------------------------------|
|                                                     |
|                     MAIN MENU                       |
|                      -  -  -                        |
|               [1] - Manage Students                 | 
|               [2] - Manage Attendance               |
|               [0] - Exit                            |
|                                                     |
 ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾

↓ Enter your choice and press Enter""")
    c=int(input(""))
    if c==1:
        manage_student()
    elif c==2:
        manage_attendance()
    elif c==0:
        exit()
    else:
        print("-------[  ❌ Invalid Input  ]--------")
    main()
main()
db.close()