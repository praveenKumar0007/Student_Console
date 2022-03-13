import mysql.connector
from valid_input import get_valid_input
from marks import get_marks
from desc import item_list
myConn = mysql.connector.connect(host = "localhost",user = "root",passwd = "almightypunch",database = "pythondb")
while True:
    person_choice = get_valid_input("1.Student\n2.Faculty\n3.Exit\n")
    if person_choice == 1:
        print("You can only view marks")
        roll_no = input("Search by Roll_no\n")
        Count_Query = "select count(Roll_no) from student where Roll_no=%s"
        cursor2 = myConn.cursor()
        cursor2.execute(Count_Query,(roll_no,))
        res = cursor2.fetchone()
        if res[0] > 0:
            select_Query = "select * from student where Roll_no=%s"
            cursor2.execute(select_Query,(roll_no,))
            sturesult = cursor2.fetchall()
            for i in sturesult:
                for j in range(0,7):
                    print(item_list[j],i[j],end="\n")
            print("\n")
        else:
            print("Invalid Roll Number\n")
    elif person_choice == 2:
        while True:
            Decider_of_faculty_choice_input=get_valid_input("\n1.Insert a Student details\n2.Display Student Details\n3.Search Details of a Student\n4.Delete Details of Student\n5.Update Student Details\n6.Exit\n")
            if Decider_of_faculty_choice_input == 1:
                roll_no = input("Enter Roll Number of Student :")
                # To check if the entered roll number is already present in the database
                Count_Query = "select count(Roll_no) from student where Roll_no=%s"
                cursor2 = myConn.cursor()
                cursor2.execute(Count_Query,(roll_no,))
                res = cursor2.fetchone()
                if( res[0] == 0):
                    name = input("Enter the name of Student :")  
                    english = get_marks("English")
                    tamil = get_marks("Tamil")
                    maths = get_marks("Maths")
                    science = get_marks("Science")
                    social_science = get_marks("Social Science")
                    inpTuple=(roll_no,name,english,tamil,maths,science,social_science)
                    cursor=myConn.cursor()
                    cursor.execute("Insert into student values(%s,%s,%s,%s,%s,%s,%s)",inpTuple)
                    myConn.commit()
                else:
                    print("Entered Roll Number is already present in the database...Please try again with valid Roll Number\n")
            elif Decider_of_faculty_choice_input == 2:
                Count_Query="select count(roll_no) from student"
                cursor1=myConn.cursor()
                cursor1.execute(Count_Query)
                res=cursor1.fetchone()
                if res[0] > 0:
                    select_Query="select Roll_no, Name from student"
                    cursor1.execute(select_Query)
                    result=cursor1.fetchall()
                    for i in result:
                        for j in range(0,2):
                            print(item_list[j],i[j],end=" | ")
                        print("\n")
                else:
                    print("No Student Details are registered...Try inserting them into the database first")
            elif Decider_of_faculty_choice_input == 3:
                roll_no=input("Select by Roll_no\n")
                Count_Query="select count(roll_no) from student where roll_no=%s"
                cursor1=myConn.cursor()
                cursor1.execute(Count_Query,(roll_no,))
                res=cursor1.fetchone()
                if res[0] > 0:
                    select_Query="select * from student where roll_no=%s"
                    cursor1.execute(select_Query,(roll_no,))
                    result=cursor1.fetchall()
                    for i in result:
                        for j in range(0,7):
                            print(i[j],end=" ")
                else:
                    print("Invalid Roll_no")
            elif Decider_of_faculty_choice_input == 4:
                roll_no = input("Enter the Roll Number that has to be deleted : ")
                Count_Query = "select count(roll_no) from student where roll_no=%s"
                cursor1=myConn.cursor()
                cursor1.execute(Count_Query,(roll_no,))
                res=cursor1.fetchone()
                if res[0] > 0:
                    delete_Query = "delete from student where roll_no=%s"
                    cursor1.execute(delete_Query,(roll_no,))
                    print(f"Roll Number {roll_no} is deleted from the database")
                else:
                    print("Entered Roll Number does NOT exist in the database")
            elif Decider_of_faculty_choice_input == 5:
                cursor3 = myConn.cursor()
                roll_no = input("Enter the Roll Number which you want to update\n")
                Count_Query = "select count(roll_no) from student where roll_no=%s"
                cursor3.execute(Count_Query,(roll_no,))
                result = cursor3.fetchone()
                if result[0] > 0:
                    while True:
                        Decider_input_update=int(input("1.Name\n2.Roll_no\n3.English Mark\n4.Tamil mark\n5.Maths mark\n6.Science mark\n7.Social Science mark\n8.Exit from update\n"))
                        if Decider_input_update == 1:
                            
                            update_Name=input("Enter the Name\n")
                            update_Name_Query="update student set name=%s where roll_no=%s"
                            myConn.commit()
                            cursor3.execute(update_Name_Query,(update_Name,roll_no))
                        elif Decider_input_update == 2:
                            update_Roll_no=input("Enter the Roll_no\n")
                            update_Roll_no_Query="update student set roll_no=%s where roll_no=%s"
                            cursor3.execute(update_Roll_no_Query,(update_Roll_no,roll_no))
                            myConn.commit()
                        elif Decider_input_update == 3:
                            update_English=int(input("Enter the English mark\n"))
                            update_English_Query="update student set english=%s where roll_no=%s"
                            cursor3.execute(update_English_Query,(update_English,roll_no))
                            myConn.commit()
                        elif Decider_input_update == 4:
                            update_Tamil=int(input("Enter the Tamil mark\n"))
                            update_Tamil_Query="update student set tamil=%s where roll_no=%s"
                            cursor3.execute(update_Tamil_Query,(update_Tamil,roll_no))
                            myConn.commit()
                        elif Decider_input_update == 5:
                            update_Maths=int(input("Enter the Maths mark\n"))
                            update_Maths_Query="update student set maths=%s where roll_no=%s"
                            cursor3.execute(update_Maths_Query,(update_Maths,roll_no))
                            myConn.commit()
                        elif Decider_input_update == 6:
                            update_Science=int(input("Enter the Science mark\n"))
                            update_Science_Query="update student set science=%s where roll_no=%s"
                            cursor3.execute(update_Science_Query,(update_Science,roll_no))
                            myConn.commit()
                        elif Decider_input_update == 7:
                            update_Social=int(input("Enter the Social mark\n"))
                            update_Social_Query="update student set social_science=%s where roll_no=%s"
                            cursor3.execute(update_Social_Query,(update_Social,roll_no))
                            myConn.commit()
                        elif Decider_input_update == 8:
                            break
                        else:
                            print("Invalid Choice")
                else:
                    print("Invalid Roll_no")
            elif Decider_of_faculty_choice_input == 6:
                break
            else:
                  print("Invalid Choice")
    elif person_choice == 3:
        break
    else:
        print("Invalid Choice")
myConn.close()