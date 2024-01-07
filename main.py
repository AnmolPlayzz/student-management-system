import mysql.connector as sql
db = sql.connect(
    host="localhost",
    user="root",
    password="root",
    database="student_management")
cur=db.cursor()

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
    phone VARCHAR(20),
    email VARCHAR(40),
    fees int
    );"""
    cur.execute(sql)
    print("'Students' table created!")
if 'attendance' not in myres:
    sql="""CREATE TABLE Attendance (
    attendance_id INT PRIMARY KEY,
    student_id INT,
    date DATE,
    status VARCHAR(10)
    );
    """
    cur.execute(sql)
    print("'Attendance' table created!")

def manage_student():
    print(f"""
+-----------------------------------------------------+
|                                                     |
|                >  Manage Student  <                 |
|                                                     | 
+-----------------------------------------------------+
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
+-----------------------------------------------------+

↓ Enter your choice and press Enter""")
    c=int(input(""))
    if c==1:
        print("-------[    Adding new Student    ]-------")
        s_id=int(input("Enter Student ID: "))
        f_na=input("Enter First Name: ")
        l_na=input("Enter Last Name: ")
        s_p=input("Enter Phone Number: ")
        s_e=input("Enter E-Mail: ")
        s_f=int(input("Enter Fees: "))
        data=(s_id,f_na,l_na,s_p,s_e,s_f)
        sql="INSERT INTO Students VALUES (%s,%s,%s,%s,%s,%s)"
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
        s_id=int(input("   >> Enter Student ID: "))
        s_id_t=(s_id,)
        chk="SELECT * FROM Students WHERE Student_id=%s"
        cur.execute(chk,s_id_t)
        res=cur.fetchall()
        print("\nSTUDENT ID\tFIRST NAME\tLAST NAME\tPHONE")
        for i in res:
            for j in i:
                print(j,end="\t\t")
            print()

        print("""
    >> What do you want to update?
    [1] First Name
    [2] Last Name
    [3] Phone Number
    [4] Email
    [5] Fees
    
    ↓ Enter your choice and press Enter""")
        mde=int(input("    "))
        col=""
        val=""
        if mde==1:
            col="first_name"
            val="'"+input("    Enter new First Name: ")+"'"
        elif mde==2:
            col="last_name"
            val="'"+input("    Enter new Last Name: ")+"'"
        elif mde==3:
            col="phone"
            val="'"+input("    Enter new Phone Number: ")+"'"
        elif mde==4:
            val="'"+input("    Enter new E-Mail: ")+"'"
        elif mde==5:
            col="fees"
            val=input("    Enter new Fees: ")
        sql="UPDATE Students SET {0}={1} WHERE student_id={2}".format(col,val,s_id)
        cur.execute(sql)
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
+-----------------------------------------------------+
|                                                     |
|               >  Manage Attendance  <               |
|                                                     | 
+-----------------------------------------------------+
|                                                     |
|                        MENU                         |
|                        -  -                         |
|               [1] - Mark Attendance                 | 
|               [2] - Retrieve Attendance             |
|               [3] - List all Records                |
|               [0] - Main Menu                       |
|                                                     |
+-----------------------------------------------------+

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
+-----------------------------------------------------+
|                                                     |
|               > Student Management <                |
|                      System                         |
|                                                     |
+-----------------------------------------------------+
|                                                     |
|                     MAIN MENU                       |
|                      -  -  -                        |
|               [1] - Manage Students                 | 
|               [2] - Manage Attendance               |
|               [0] - Exit                            |
|                                                     |
+-----------------------------------------------------+

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