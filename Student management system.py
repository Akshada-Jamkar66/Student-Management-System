db={101:{"Name":"Akshada","City":"Nashik","Per":85,"Course":"Python"}}
print("-"*140)
print("Student Management System".center(130))
print("-"*140)
while True:
    print("""
            Dashboard
    1.Add student details
    2.display student details
    3.update student details
    4.delete student details"
    5.filter student details

""")
    ch=int(input("Enter Your choice:" ))
    if ch==1:
        Reg_No=eval(input("Enter Reg_no:"))
        Name=input("Enter name:")
        City=input("Enter City:")
        Per=eval(input("Enter per:"))
        Course=input(input("Enter Course:"))
        db[Reg_No]={"Name":Name,"city":City,"Per":Per,"Course":Course}
        print("Added successfully...")
    elif ch==2:
        print("-"*105)
        print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format("Reg_No","Name","City","Percentag","Course"))
        print("-"*105)
        for i in db:
            print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format(i,db[i]["Name"],db[i]["City"],db[i]["Per"],db[i],db["Course"]))
            print("-"*105)
    elif ch==3:
            Reg_No=eval(input("Reg_no:"))
            print("""
            1.Name
            2.City
            3.Per 
            4.Course
            """)
            ch=eval(input("Enter your choice:"))
            if ch==1:
                #var[key]=value
                uname=input("Enter name:")
                db[Reg_No]["Name"]=uname
                print("updated successfully...")
            elif ch==2:
                ucity=input("Enter city:")
                db[Reg_No]["City"]=ucity
                print("updated successfully...")
            elif ch==3:    
                uper=input("Enter per:")
                db[Reg_No]["Per"]=uper
                print("updated successfully...")
            elif ch==4:
                ucourse=input("Enter course:")
                db[Reg_No]["Course"]=ucourse
                print("updated successfully...")
            else:
                print("invalid input")
    elif ch==4:
        reg=eval(input("Enter Reg_no:"))
        del db[reg]
        print("delete successfully...")
            
    elif ch==5:
        print("""
            1.Name
            2.City
            3.Per
            4.Course
              """)
        print("-"*105)
        print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format("Reg_No","Name","City","Percentag","Course"))
        print("-"*105)
        for i in db:
            if db[i]["city"]==ucity:
                 print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format(i,db[i]["Name"],db[i]["City"],db[i]["Per"],db[i],["Course"]))
                 print("-"*105)


            elif ch==1:
                db[i]["Course"]==Course
                print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format(i,db[i]["Name"],db[i]["City"],db[i]["Per"],db[i],["Course"]))
                print("-"*105)

            elif ch==3:
                db[i]["Per"]==Per
                print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format(i,db[i]["Name"],db[i]["City"],db[i]["Per"],db[i],["Course"]))
                print("-"*105)
            else:
                 print("invalid input")    

else:
    print("invalid choice:")






