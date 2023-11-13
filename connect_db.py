from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
from tkinter import  messagebox
import pymysql


class Connect_database:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        self.hostval = StringVar()
        self.userval = StringVar()
        self.passwordval = StringVar()

        title_1b1=Label(self.root,text="Face Recognition Attendance System DataBase Connection",font=("Times new roman",35,"bold"),bg="black",fg="white")
        title_1b1.place(x=0,y=0,width=1400,height=60)
        title_1b1=Label(self.root,text="If you First Time in Use this Software then you fill this interface All required information",font=("Times new roman",25,"bold"),bg="white",fg="blue")
        title_1b1.place(x=0,y=61,width=1400,height=45)
        title_1b1=Label(self.root,text="Otherwise you Skip this Interface.",font=("Times new roman",25,"bold"),bg="white",fg="blue")
        title_1b1.place(x=0,y=105,width=1400,height=45)

        #background Image
        img3=Image.open(r"image/face_detect1.jpg")
        img3=img3.resize((1530,500),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=150,width=1530,height=500)


        #=====================================Entry Label===========================
        #connect_database_frame=LabelFrame(bg_img,bd=2,relief=RIDGE,font=("Times new roman",12,"bold"))
        #connect_database_frame.place(x=500,y=200,width=330,height=150)

        # Host
        studentId_label = Label(bg_img, text="Host Name :", font=("Times new roman", 20, "bold"))
        studentId_label.place(x=250,y=160)
        
        #Host Entry Box
        studentId_entry=ttk.Entry(bg_img,width=20,textvariable=self.hostval, font=("Times new roman",20, "bold"))
        studentId_entry.place(x=450,y=160)


        # Username
        studentId_label = Label(bg_img, text="User Name :", font=("Times new roman", 20, "bold"))
        studentId_label.place(x=250,y=220)
        
        #Username Entry Box
        studentId_entry=ttk.Entry(bg_img,width=20,textvariable=self.userval, font=("Times new roman", 20, "bold"))
        studentId_entry.place(x=450,y=220)


        # Password
        studentId_label = Label(bg_img, text="Password :", font=("Times new roman", 20, "bold"))
        studentId_label.place(x=250,y=280)
        
        #Password Entry Box
        studentId_entry=ttk.Entry(bg_img,width=20,textvariable=self.passwordval, font=("Times new roman", 20, "bold"))
        studentId_entry.place(x=450,y=280)

        submit_btn=Button(bg_img,text="Submit",command=self.submitdb, cursor="hand2",font=("Times new roman",25,"bold"),bg="blue",fg="white")
        submit_btn.place(x=350,y=350,width=300,height=50)

    def submitdb(self):
        global con, mycursor

        host=self.hostval.get()
        user=self.userval.get()
        password=self.passwordval.get()

        # host = 'localhost'
        # user = 'root'
        # password = ''
        try:
            conn = pymysql.connect(host=host, user=user, password=password)
            my_cursor = conn.cursor()
            messagebox.showinfo('Notification', 'Connection Sucessfull',parent=self.root)

        except:
            messagebox.showerror('Notification', 'Data is incorrect please try again',parent=self.root)
            return
        try:
            strr = 'create database face'
            my_cursor.execute(strr)
            strr = 'use face'
            my_cursor.execute(strr)
            strr = 'create table student(Department varchar(100),Course varchar(100),Year varchar(20),Semester varchar(20),Student_id varchar(20) not null,Name varchar(255),Section varchar(20),Roll bigint(20) not null primary key,Gender varchar(20),Dob varchar(20),Email varchar(255),Phone varchar(20),Address varchar(100),Teacher varchar(50),PhotoSamplesStatus varchar(45))'
            my_cursor.execute(strr)
            messagebox.showinfo('Notification', 'Database created successfully and you are connected to the database',
                                parent=self.root)
        except:
            strr = 'use face'
            my_cursor.execute(strr)

            messagebox.showinfo('Notification', 'Now face database is active.', parent=self.root)
        self.root.destroy()


if __name__ == "__main__":
    root=Tk()
    obj=Connect_database(root)
    root.mainloop()
