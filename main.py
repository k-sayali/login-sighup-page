from tkinter import *
import tkinter as tk
from tkinter import messagebox
import json
from tkinter import ttk
import re

class Person:
    def __init__(self,email,password,name):
        self.name = name
        self.password= password
        self.email = email


class Teacher(Person):
    def __init__(self, email, password, name):
        super().__init__(email,password,name)
        self.type = "Teacher"
        self.counter=0


class Student(Person):
    def __init__(self,email, password, name):
        super().__init__(email, password, name)
      


class UGStudent(Student):
    def __init__(self, email, password, name, dept):
        super().__init__(email, password, name)
        self.dept = dept
        self.type = "UGStudent"
        self.counter=0

class PGStudent(Student):
    def __init__(self, email, password, name,  course):
        super().__init__(email, password, name)
        self.course = course
        self.type = "PGStudent"
        self.counter=0



def write_json(data, fname="data.json"):
    with open(fname, "w") as f:
        json.dump(data, f, indent=5)

# Reading the JSON file
try:
    with open("data.json") as f:
        data = json.load(f)
except FileNotFoundError:
    data = {"Teacher": [], "UGStudent": [], "PGStudent": []}

# Extracting lists
Teacher_List = data.get("Teacher", [])
UGStudent_List = data.get("UGStudent", [])
PGStudent_List = data.get("PGStudent", [])



def user_registration(user, type):
    if type == "Teacher":
        Teacher_List.append(user)
    elif type == "PGStudent":
        PGStudent_List.append(user)
    elif type == "UGStudent":
        UGStudent_List.append(user)
    write_json(data)


def Sign_into_System(email, password):
    for user in Teacher_List:
        if user["email"] == email and user["password"] == password:
            return user
    for user in PGStudent_List:
        if user["email"] == email and user["password"] == password:
            return user
    for user in UGStudent_List:
        if user["email"] == email and user["password"] == password:
            return user
    return None


def Teacher_Update(email, password, new_email, new_password, name):
    for user in Teacher_List:
        if user["email"] == email and user["password"] == password:
            user["email"] = ""
            user["password"] = ""
            user["name"] = ""
            user["counter"]=0
    
            user["email"] = new_email
            user["password"] = new_password
            user["name"] = name
            write_json(data)
            messagebox.showinfo("Sucess","Information updated successfully")
            return
    messagebox.showerror("Error", "User Not Found")

def UGStudent_Update(email, password, new_email, new_password, name, dept):
    for user in UGStudent_List:
        if user["email"] == email and user["password"] == password:
            user["email"] = ""
            user["password"] = ""
            user["name"] = ""
            user["email"] = new_email
            user["password"] = new_password
            user["name"] = name
            user["dept"] = dept
            write_json(data)
            messagebox.showinfo("Sucess","Information updated successfully")
            return
    messagebox.showerror("Error", "User Not Found")

def PGStudent_Update(email, password, new_email, new_password, name, course):
    for user in PGStudent_List:
        if user["email"] == email and user["password"] == password:
            user["email"] = ""
            user["password"] = ""
            user["name"] = ""
            user["email"] = new_email
            user["password"] = new_password
            user["name"] = name
            user["course"] = course
            write_json(data)
            messagebox.showinfo("Sucess","Information updated successfully")
            return
    messagebox.showerror("Error", "User Not Found")



def is_user(email, password):
    for user in Teacher_List:
        if user["email"] == email and user["password"] == password:
            return True
    for user in PGStudent_List:
        if user["email"] == email and user["password"] == password:
            return True
    for user in UGStudent_List:
        if user["email"] == email and user["password"] == password:
            return True
    return False


def Deactivate_User_Account(email, password, type):
    if type == "Teacher":
        for user in Teacher_List:
            if user["email"] == email and user["password"] == password:
                Teacher_List.remove(user)
                write_json(data)
                messagebox.showinfo("Sucess","user degestisterd")
                return
    elif type == "PGStudent":
        for user in PGStudent_List:
            if user["email"] == email and user["password"] == password:
                PGStudent_List.remove(user)
                write_json(data)
                messagebox.showinfo("Sucess","user degestisterd")
                return
    elif type == "UGStudent":
        for user in UGStudent_List:
            if user["email"] == email and user["password"] == password:
                UGStudent_List.remove(user)
                write_json(data)
                messagebox.showinfo("Sucess","user degestisterd")
                return
    messagebox.showerror("Error", "User Not Found")

def deactivate_by_email(email):
        for user in Teacher_List:
            if user["email"] == email:
                Teacher_List.remove(user)
                write_json(data)
        for user in PGStudent_List:
            if user["email"] == email:
                PGStudent_List.remove(user)
                write_json(data)
        for user in UGStudent_List:
            if user["email"] == email:
                UGStudent_List.remove(user)
                write_json(data)



def is_strong_password(password):
        if (
            8 <= len(password) <= 12
            and any(char.isupper() for char in password)
            and any(char.isdigit() for char in password)
            and any(char.islower() for char in password)
            and any(char in "!@#$%&*" for char in password)
            and ' ' not in password
        ):
            return True
        else : messagebox.showerror("error","Password is not strong Error")
        return False

def Register(frame, type):
    frame.destroy()
    frame = ttk.Frame(root)
    frame.pack(expand=True, fill="both", padx=10, pady=10)
    label_user_id = tk.Label(frame, text="User ID:")
    label_user_id.pack()
    entry_user_id = tk.Entry(frame,text="enter user id")
    entry_user_id.pack()

    label_password = tk.Label(frame, text="Password:")
    label_password.pack()

    entry_password = tk.Entry(frame, show="*") 
    entry_password.pack()

    def register_users():
        if not is_strong_password(entry_password.get()):
            return
        elif is_user(entry_user_id.get(), entry_password.get()) == True:
            messagebox.showerror("Error", "This Account already is_users")
        else:
            if type == "Teacher":
                user = {
                    "email": entry_user_id.get(),
                    "password": entry_password.get(),
                    "type": "Teacher",
                    "name" : "",
                    "counter":0,
                }
           
            elif type == "UGStudent":
                user = {
                    "email": entry_user_id.get(),
                    "password": entry_password.get(),
                    "type": "UGStudent",
                    "name" : "",
                    "counter":0,
                }
            elif type == "PGStudent":
                user = {
                    "email": entry_user_id.get(),
                    "password": entry_password.get(),
                    "type": "PGStudent",
                    "name" : "",
                    "counter":0,
                }
            user_registration(user, type)
            messagebox.showinfo("Success", "User registered successfully")
            if type == "Teacher":
                register_button.destroy()
                label_name = tk.Label(frame, text="Name:")
                label_name.pack()

                entry_name = tk.Entry(frame)
                entry_name.pack()

                update_button = tk.Button(
                    frame,
                    text="Update Details",
                    command=lambda: Teacher_Update(
                        user["email"],
                        user["password"],
                        entry_user_id.get(),
                        entry_password.get(),
                        entry_name.get(),
                    ),
                )
                update_button.pack(pady=10)

                deactivate_button = tk.Button(
                    frame,
                    text="Deactivate User",
                    command=lambda: Deactivate_User_Account(
                        entry_user_id.get(), entry_password.get(), type
                    ),
                )
                deactivate_button.pack(pady=10)

                sign_button = tk.Button(
                    frame, text="Sign In Page", command=lambda: Sign_window(frame)
                )
                sign_button.pack(pady=10)

            elif type == "PGStudent":
                register_button.destroy()
                label_name = tk.Label(frame, text="Name:")
                label_name.pack()

                entry_name = tk.Entry(frame)
                entry_name.pack()

                label_course = tk.Label(frame, text="course:")
                label_course.pack()

                entry_course = tk.Entry(frame)
                entry_course.pack()

                update_button = tk.Button(
                    frame,
                    text="Update Details",
                    command=lambda: PGStudent_Update(
                        user["email"],
                        user["password"],
                        entry_user_id.get(),
                        entry_password.get(),
                        entry_name.get(),
                        entry_course.get(),
                    ),
                )
                update_button.pack(pady=10)

                deactivate_button = tk.Button(
                    frame,
                    text="Deactivate User",
                    command=lambda: Deactivate_User_Account(
                        entry_user_id.get(), entry_password.get(), type
                    ),
                )
                deactivate_button.pack(pady=10)

                sign_button = tk.Button(
                    frame, text="Sign In Page", command=lambda: Sign_window(frame)
                )
                sign_button.pack(pady=10)

            elif type == "UGStudent":
                register_button.destroy()
                label_name = tk.Label(frame, text="Name:")
                label_name.pack()

                entry_name = tk.Entry(frame)
                entry_name.pack()

                label_dept = tk.Label(frame, text="Department:")
                label_dept.pack()

                entry_dept = tk.Entry(frame)
                entry_dept.pack()

                update_button = tk.Button(
                    frame,
                    text="Update Details",
                    command=lambda: UGStudent_Update(
                        user["email"],
                        user["password"],
                        entry_user_id.get(),
                        entry_password.get(),
                        entry_name.get(),
                        entry_dept.get(),
                    ),
                )
                update_button.pack(pady=10)

                deactivate_button = tk.Button(
                    frame,
                    text="Deactivate User",
                    command=lambda: Deactivate_User_Account(
                        entry_user_id.get(), entry_password.get(), type
                    ),
                )
                deactivate_button.pack(pady=10)

                sign_button = tk.Button(
                    frame, text="Sign In Page", command=lambda: Sign_window(frame)
                )
                sign_button.pack(pady=10)

                
                

    register_button = tk.Button(frame, text="Register", command=register_users)
    register_button.pack(pady=10)


def User_Register_window(frame):
    frame.destroy()
    frame = ttk.Frame(root)
    frame.pack(expand=True, fill="both", padx=10, pady=10)
    
    label_type = tk.Label(frame, text="Register As: ")
    label_type.pack()

    button1 = tk.Button(
        frame, text="Teacher", command=lambda: Register(frame, "Teacher")
    )
    button1.pack(pady=10)

    button2 = tk.Button(
        frame, text="PG-Student", command=lambda: Register(frame, "PGStudent")
    )
    button2.pack(pady=10)

    button3 = tk.Button(
        frame, text="UG-Student", command=lambda: Register(frame, "UGStudent")
    )
    button3.pack(pady=10)


def Sign_window(frame):
    frame.destroy()
    frame = ttk.Frame(root)
    frame.pack(expand=True, fill="both", padx=10, pady=30)
    heading=Label(root,text='USER SIGHIN')
    heading.place(x=160,y=10)
  
    label_user_id = tk.Label(frame, text="User ID:")
    label_user_id.pack()

    entry_user_id = tk.Entry(frame)
    entry_user_id.pack()

    label_password = tk.Label(frame, text="Password:")
    label_password.pack()

    entry_password = tk.Entry(frame, show="*")  # Show '*' for password
    entry_password.pack()

    def submit_form():
       
        user_id = entry_user_id.get()
        password = entry_password.get()
       
        if Sign_into_System(user_id, password) == None:
            messagebox.showerror(
                "Error", "User ID or Password is incorrect. Please try again."
            )
            for user in Teacher_List:
             if(user["email"]==user_id):
              user["counter"]+=1
              if(user["counter"]==3):
                  deactivate_by_email(user["email"])
                  messagebox.showerror(
                "Error", "User ID is deactivated. "
            )
             write_json(data)
            for user in UGStudent_List:
             if(user["email"]==user_id):
              user["counter"]+=1
              if(user["counter"]==3):
                  deactivate_by_email(user["email"])
                  messagebox.showerror(
                "Error", "User ID is deactivated."
            )
             write_json(data)
            for user in PGStudent_List:
             if(user["email"]==user_id):
              user["counter"]+=1
              if(user["counter"]==3):
                  deactivate_by_email(user["email"])
                  messagebox.showerror(
                "Error", "User ID is deactivated."
            )
             write_json(data)

            return
        else: 
            messagebox.showinfo("Success", "Login Successful!")
            for user in Teacher_List:
             if(user["email"]==user_id):
              user["counter"]=0
            for user in UGStudent_List:
             if(user["email"]==user_id):
              user["counter"]=0
            for user in PGStudent_List:
             if(user["email"]==user_id):
              user["counter"]=0

            write_json(data)
            user = Sign_into_System(user_id, password)
            if user["type"] == "Teacher":
                submit_button.destroy()
                label_name = tk.Label(frame, text="Name:")
                label_name.pack()
                entry_name = tk.Entry(frame, textvariable="Enter New Name")
                entry_name.pack()

                update_button = tk.Button(
                    frame,
                    text="Update Details",
                    command=lambda: Teacher_Update(
                        user["email"],
                        user["password"],
                        entry_user_id.get(),
                        entry_password.get(),
                        entry_name.get(),
                    ),
                )
                update_button.pack(pady=10)

                deactivate_button = tk.Button(
                    frame,
                    text="Deactivate User",
                    command=lambda: Deactivate_User_Account(
                        entry_user_id.get(), entry_password.get(), "Teacher"
                    ),
                )
                deactivate_button.pack(pady=10)

                sign_button = tk.Button(
                    frame, text="Sign In Page", command=lambda: Sign_window(frame)
                )
                sign_button.pack(pady=10)

            elif user["type"] == "PGStudent":
                submit_button.destroy()
                label_name = tk.Label(frame, text="Name:")
                label_name.pack()

                entry_name = tk.Entry(frame, textvariable="Enter New Name")
                entry_name.pack()

                label_course = tk.Label(frame, text="course:")
                label_course.pack()

                entry_course = tk.Entry(frame)
                entry_course.pack()

                update_button = tk.Button(
                    frame,
                    text="Update Details",
                    command=lambda: PGStudent_Update(
                        user.id,
                        user["password"],
                        entry_user_id.get(),
                        entry_password.get(),
                        entry_name.get(),
                        entry_course.get(),
                    ),
                )
                update_button.pack(pady=10)

                deactivate_button = tk.Button(
                    frame,
                    text="Deactivate User",
                    command=lambda: Deactivate_User_Account(
                        entry_user_id.get(), entry_password.get(), "PGStudent"
                    ),
                )
                deactivate_button.pack(pady=10)

                sign_button = tk.Button(
                    frame, text="Sign In Page", command=lambda: Sign_window(frame)
                )
                sign_button.pack(pady=10)

            elif user["type"] == "UGStudent":
                submit_button.destroy()
                label_name = tk.Label(frame, text="Name:")
                label_name.pack()

                entry_name = tk.Entry(frame, textvariable="Enter New Name")
                entry_name.pack()

                label_dept = tk.Label(frame, text="Department:")
                label_dept.pack()

                entry_dept = tk.Entry(frame)
                entry_dept.pack()

                update_button = tk.Button(
                    frame,
                    text="Update Details",
                    command=lambda: UGStudent_Update(
                        user.id,
                        user["password"],
                        entry_user_id.get(),
                        entry_password.get(),
                        entry_name.get(),
                        entry_dept.get(),
                    ),
                )
                update_button.pack(pady=10)

                deactivate_button = tk.Button(
                    frame,
                    text="Deactivate User",
                    command=lambda: Deactivate_User_Account(
                        entry_user_id.get(), entry_password.get(), "UGStudent"
                    ),
                )
                deactivate_button.pack(pady=10)

                sign_button = tk.Button(
                    frame, text="Sign In Page", command=lambda: Sign_window(frame)
                )
                sign_button.pack(pady=10)

    submit_button = tk.Button(frame, text="Submit", command=submit_form)
    submit_button.pack(pady=10)


# Main window
root = tk.Tk()
root.title("Teacher-student info")
root.geometry("400x450")

main_frame = ttk.Frame(root)
main_frame.pack(expand=True, fill="both", padx=10, pady=10)
heading=Label(root,text='WELCOME USER')
heading.place(x=160,y=10)

button1 = tk.Button(
    main_frame, text="Register User", command=lambda: User_Register_window(main_frame)
)
button1.pack(pady=30)

button2 = tk.Button(main_frame, text="Sign In User", command=lambda: Sign_window(main_frame))
button2.pack(pady=0)

root.mainloop()