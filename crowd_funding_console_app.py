import json
import datetime
import re
def update_File(users):
    with open("data.json", 'w') as f:
        json.dump(users, f)
        f.close()
    return users

def read_file(fileName):
    with open(fileName, 'r') as f:
        data = json.load(f)
    f.close()
    return data

#store data
def store_data(user,fileName):
    users = read_file(fileName)
    users.append(user)
    with open(fileName, 'w') as f:
        json.dump(users, f)
        f.close()

def validate_email(email):
    regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
    if (re.search(regex, email)):
       return True
    else:
        return False

def register():
    flag=False
    firstName = input("Enter Your First Name ")
    lastName = input("Enter Your Last Name ")

    email = input("Enter Your Email ")
    while flag==False:
        if validate_email(email)== False:
            print("Email is unvalid")
            email = input("plz  Enter Your Email ")
        flag=True
        
    phoneNumber = input("Enter Your Phone Number ")
    password = input("Enter Your Password ")
    confirmPassword = input("Confrim Password ")

    while password != confirmPassword:
        print("your password is not identical")
        confirmPassword = input("Enter Your Password ")

    data = {
         "fName": firstName,
         "lName": lastName,
         "email": email,
         "password": password,
         "phoneNumber": phoneNumber,
         "projects": [

         ]
        }
    store_data(data,'data.json')
    print("***********************  WELCOME "+firstName+"  ***********************")
    login()

def menu():
    print("""
    \t\t\t\t\t\t\t\t\t\t\t <---------------WELCOME--------------> \t\t\t\t\t\t\t\t\t\t
    1.Register
    2.Login
    3.Exit/Quit
    """)
    choose = input("Enter your choice ")
    if choose == "1" :
       register()
    elif choose == "2":
       login()
    elif choose == "3":
       print("exit")
    else:
       print("Choose Correct Number")
       menu()

def CreateProject(author):
    title=input("Please Enter title ")
    details=input("Please Enter details ")
    target=input("Please enter total target ")
    startDate=input("Please enter start time for the campaign ")
    endDate=input("Please enter end time for the campaign ")
    date_format = '%Y-%m-%d'
    flag=False

    while flag==False:
        try:
            datetime.datetime.strptime(startDate, date_format)
            datetime.datetime.strptime(endDate, date_format)
            flag=True
            print("right")
        except ValueError:
            print("Incorrect data format, should be YYYY-MM-DD")
            startDate = input("Please enter start time for the campaign")
            endDate = input("Please enter end time for the campaign")

    data = {
         "title": title,
         "details": details,
         "target": target,
         "startDate": startDate,
         "endDate":  endDate,
        }
    users=read_file('data.json')
    for user in users:
        if user['email'] == author:
            user['projects'].append(data)
            with open("data.json", 'w') as f:
                json.dump(users, f)
                f.close()
            print("Project Created Successfully")
            break
    projectMenu(author)

def listProjects():
    users = read_file('data.json')
    for user in users:
        projects= user['projects']
        for project in projects:
            print(project['title'] +" " + project['details'] +" " + project['target'] +" " + project['startDate'] +" " + project['endDate']  )






def deleteproject(author):
     users = read_file('data.json')
     for user in users:
         if user['email'] == author:
            projectName=input("please enter project name ")
            projects = user['projects']
            for project in projects:
                if projectName == project['title']:
                    projects.remove(project)
                    with open("data.json", 'w') as f:
                        json.dump(users, f)
                        f.close()
                    print(projects)
                    break

def editProject(author):
    users = read_file('data.json')
    for user in users:
        if user['email'] == author:
            projectName = input("please enter project name ")
            projects = user['projects']
            for project in projects:
                if projectName == project['title']:
                    print(""" please choose element to edit 
                        1.Title
                        2.Details
                        3.Target
                        4.Start Date
                        5.End Date
                        """)
                    choose = input("Enter your choice ")
                    if choose == "1":
                        project['title']=input("enter new title ")
                        print(projects)
                        update_File(users)

                    elif choose == "2":
                        project['details']=input("enter new details ")
                        update_File(users)
                    elif choose == "3":
                        project['target']=input("enter new target ")
                        update_File(users)
                    elif choose == "4":
                        project['startDate']=input("enter new start date ")
                        update_File(users)
                    elif choose == "5":
                        project['endDate']=input("enter new end date ")
                        update_File(users)
                    else:
                        print("Choose Correct Number")
                        menu()











def projectMenu(author):
    print("""
       \t\t\t\t\t\t\t\t\t\t\t <---------------WELCOME--------------> \t\t\t\t\t\t\t\t\t\t
       1.Create Project
       2.List Projects
       3.Delete Project
       4.Edit Project
       """)
    choose = input("Enter your choice ")
    if choose == "1":
      CreateProject(author)

    elif choose == "2":
      listProjects()

    elif choose == "3":
      deleteproject(author)

    elif choose == "4":
      editProject(author)

    else:
        print("Choose Correct Number")
        projectMenu()

def login():
    email=input("Please Enter Your Email ")
    password=input("please Enter Your Password ")
    users=read_file('data.json')
    flag=False
    for user in users:
        if email == user['email'] and password == user['password']:
           flag=True
           print("Welcome " + user['fName'])
           projectMenu(user['email'])
           break

    if flag == False:
        print("Username Or Password is incorrect")
        login()



menu()