import mysql.connector
myConn = mysql.connector.connect(host="localhost",user="root",passwd="almightypunch",database="pythondb")
while True:
    Decider_of_person_input=int(input("1.Student\n2.Faculty\n3.Exit\n"))
    if Decider_of_person_input == 1:
        print("You can only view marks")
        Roll_no=input("Search by Roll_no\n")
        Count_Query="select count(roll_no) from student where roll_no=%s"
        cursor2=myConn.cursor()
        cursor2.execute(Count_Query,(Roll_no,))
        res=cursor2.fetchone()
        if res[0] > 0:
            select_Query="select * from student where roll_no=%s"
            cursor2.execute(select_Query,(Roll_no,))
            sturesult=cursor2.fetchall()
            for i in sturesult:
                for j in range(0,7):
                    if j == 6:
                        print(i[j],end="\n")
                    else:
                        print(i[j],end=" ")
        else:
            print("Invalid Roll_no")
    elif Decider_of_person_input == 2:
        while True:
            Decider_of_faculty_choice_input=int(input("\n1.Insert a Student details\n2.Display Student Details\n3.Search Details of a Student\n4.Delete Details of Student\n5.Update Student Details\n6.Exit\n"))
            if Decider_of_faculty_choice_input == 1:
                Name=input("Enter the name\n")  
                Roll_no=input("Enter the Roll_no\n")
                print("Enter the marks")
                English=int(input("English "))
                Tamil=int(input("Tamil "))
                Maths=int(input("Maths "))
                Science=int(input("Science "))
                Social=int(input("Social science "))
                inpTuple=(Name,Roll_no,English,Tamil,Maths,Science,Social)
                cursor=myConn.cursor()
                cursor.execute("Insert into student values(%s,%s,%s,%s,%s,%s,%s)",inpTuple)
                myConn.commit()
            elif Decider_of_faculty_choice_input == 2:
                Roll_no=input("Select by Roll_no\n")
                Count_Query="select count(roll_no) from student where roll_no=%s"
                cursor1=myConn.cursor()
                cursor1.execute(Count_Query,(Roll_no,))
                res=cursor1.fetchone()
                if res[0] > 0:
                    select_Query="select * from student where roll_no=%s"
                    cursor1.execute(select_Query,(Roll_no,))
                    result=cursor1.fetchall()
                    for i in result:
                        for j in range(0,7):
                            print(i[j],end=" ")
                else:
                    print("Invalid Roll_no")
            elif Decider_of_faculty_choice_input == 3:
                Roll_no=input("Select by Roll_no\n")
                Count_Query="select count(roll_no) from student where roll_no=%s"
                cursor1=myConn.cursor()
                cursor1.execute(Count_Query,(Roll_no,))
                res=cursor1.fetchone()
                if res[0] > 0:
                    select_Query="select * from student where roll_no=%s"
                    cursor1.execute(select_Query,(Roll_no,))
                    result=cursor1.fetchall()
                    for i in result:
                        for j in range(0,7):
                            print(i[j],end=" ")
                else:
                    print("Invalid Roll_no")
            elif Decider_of_faculty_choice_input == 4:
                Roll_no=input("Search by Roll_no\n")
                Count_Query="select count(roll_no) from student where roll_no=%s"
                cursor1=myConn.cursor()
                cursor1.execute(Count_Query)
                res=cursor1.fetchone()
                if res[0] > 0:
                    delete_Query="delete from student where roll_no=%s"
                    cursor1.execute(delete_Query,(Roll_no,))
                else:
                    print("Invalid Input")
            elif Decider_of_faculty_choice_input == 5:
                cursor3=myConn.cursor()
                Roll_no=input("Enter the Roll_no you want to update\n")
                print("Which part do you want to update")
                Count_Query="select count(roll_no) from student where roll_no=%s"
                cursor3.execute(Count_Query,(Roll_no,))
                result=cursor3.fetchone()
                if result[0] > 0:
                    while True:
                        Decider_input_update=int(input("1.Name\n2.Roll_no\n3.English Mark\n4.Tamil mark\n5.Maths mark\n6.Science mark\n7.Social Science mark\n8.Exit from update\n"))
                        if Decider_input_update == 1:
                            
                            update_Name=input("Enter the Name\n")
                            update_Name_Query="update student set name=%s where roll_no=%s"
                            myConn.commit()
                            cursor3.execute(update_Name_Query,(update_Name,Roll_no))
                        elif Decider_input_update == 2:
                            update_Roll_no=input("Enter the Roll_no\n")
                            update_Roll_no_Query="update student set roll_no=%s where roll_no=%s"
                            cursor3.execute(update_Roll_no_Query,(update_Roll_no,Roll_no))
                            myConn.commit()
                        elif Decider_input_update == 3:
                            update_English=int(input("Enter the English mark\n"))
                            update_English_Query="update student set english=%s where roll_no=%s"
                            cursor3.execute(update_English_Query,(update_English,Roll_no))
                            myConn.commit()
                        elif Decider_input_update == 4:
                            update_Tamil=int(input("Enter the Tamil mark\n"))
                            update_Tamil_Query="update student set tamil=%s where roll_no=%s"
                            cursor3.execute(update_Tamil_Query,(update_Tamil,Roll_no))
                            myConn.commit()
                        elif Decider_input_update == 5:
                            update_Maths=int(input("Enter the Maths mark\n"))
                            update_Maths_Query="update student set maths=%s where roll_no=%s"
                            cursor3.execute(update_Maths_Query,(update_Maths,Roll_no))
                            myConn.commit()
                        elif Decider_input_update == 6:
                            update_Science=int(input("Enter the Science mark\n"))
                            update_Science_Query="update student set science=%s where roll_no=%s"
                            cursor3.execute(update_Science_Query,(update_Science,Roll_no))
                            myConn.commit()
                        elif Decider_input_update == 7:
                            update_Social=int(input("Enter the Social mark\n"))
                            update_Social_Query="update student set social_science=%s where roll_no=%s"
                            cursor3.execute(update_Social_Query,(update_Social,Roll_no))
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
    elif Decider_of_person_input == 3:
        break
    else:
        print("Invalid Choice")
myConn.close()