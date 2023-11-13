from tkinter import*
import tkinter
from tkinter import messagebox
from tkinter import ttk
from PIL import Image,ImageTk
from time import strftime
from student import Student
from train import Train
from developer import Developer
from face_recognition import Face_Recognition
from attendance import Attendance
from connect_db import Connect_database
import os

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1521x820+0+0")
        self.root.title("Face Recognition Attendance System")

        #background Image
        img3= Image.open(r"image/Black.png")
        img3=img3.resize((1530,760),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1521,height=760)

        title_1b1=Label(bg_img,text="Attendance Management System",font=("Times new roman",25,"bold"),bg="black",fg="white")
        title_1b1.place(x=0,y=0,width=1400,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=50,width=1500,height=625)
        
        # Clock
        def time():
            string=strftime("%H:%M:%S %p")
            lbl.config(text=string)
            lbl.after(1000, time)

        lbl=Label(title_1b1,font=("times new roman",10,"bold"),background='black',foreground='white')
        lbl.place(x=20,y=0,width=120,height=50)
        time()


        b1_9=Button(title_1b1,text="Logout",command=self.root, cursor="hand2",font=("Times new roman",12,"bold"),bg="black",fg="white")
        b1_9.place(x=1250,y=10,width=90,height=25)


        # Left Frame
        Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,font=("Times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=200,height=600)

        img_left= Image.open(r"image/SU_2.jpg")
        img_left= img_left.resize((100, 100), Image.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_1bl=Label(self.root,image=self.photoimg_left)
        f_1bl.place(x=70,y=70,width=100,height=100)

        # Right Frame
        Right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,font=("Times new roman",12,"bold"))
        Right_frame.place(x=220,y=10,width=1110,height=600)

        img_right= Image.open(r"image/SU_1.png")
        img_right= img_right.resize((700, 100), Image.LANCZOS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_1bl=Label(self.root,image=self.photoimg_right)
        f_1bl.place(x=450,y=70,width=700,height=100)

        # 2nd img
        img_right2= Image.open(r"image/atte11.jpg")
        img_right2= img_right2.resize((800, 350), Image.LANCZOS)
        self.photoimg_right2=ImageTk.PhotoImage(img_right2)

        f_1bl=Label(self.root,image=self.photoimg_right2)
        f_1bl.place(x=400,y=200,width=800,height=350)

        # Department Label
        Wel_label=Label(Right_frame,text="Welcome To Sonargaon University Student Attendance System",font=("Times new roman",25,"bold"),fg="darkblue" )
        Wel_label.grid(row=0,column=0,padx=0,sticky=W)
        Wel_label.place(x=120,y=500)
        Wel_label2=Label(Right_frame,text="Using Face Recognition",font=("Times new roman",25,"bold"),fg="darkblue" )
        Wel_label2.grid(row=0,column=0,padx=0,sticky=W)
        Wel_label2.place(x=390,y=540)

        # All Buttons  
        b1_1=Button(Left_frame,text="Student Details",command=self.student_details, cursor="hand2",font=("Times new roman",12,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=3,y=120,width=190,height=25)

        b1_2=Button(Left_frame,text="Train Data",command=self.train, cursor="hand2",font=("Times new roman",12,"bold"),bg="darkblue",fg="white")
        b1_2.place(x=3,y=155,width=190,height=25)

        b1_3=Button(Left_frame,text="Attendence",command=self.attendance, cursor="hand2",font=("Times new roman",12,"bold"),bg="darkblue",fg="white")
        b1_3.place(x=3,y=185,width=190,height=25)

        b1_4=Button(Left_frame,text="Face Detection",command=self.face_recognition, cursor="hand2",font=("Times new roman",12,"bold"),bg="darkblue",fg="white")
        b1_4.place(x=3,y=215,width=190,height=25)

        b1_5=Button(Left_frame,text="Student Photos",command=self.open_img, cursor="hand2",font=("Times new roman",12,"bold"),bg="darkblue",fg="white")
        b1_5.place(x=3,y=245,width=190,height=25)

        b1_6=Button(Left_frame,text="Devloper",command=self.developer, cursor="hand2",font=("Times new roman",12,"bold"),bg="darkblue",fg="white")
        b1_6.place(x=3,y=275,width=190,height=25)

        b1_7=Button(Left_frame,text="Help",command=self.root, cursor="hand2",font=("Times new roman",12,"bold"),bg="darkblue",fg="white")
        b1_7.place(x=3,y=305,width=190,height=25)
        
        b1_7=Button(Left_frame,text="Create Database",command=self.connect_database, cursor="hand2",font=("Times new roman",12,"bold"),bg="darkblue",fg="white")
        b1_7.place(x=3,y=305,width=190,height=25)

        b1_8=Button(Left_frame,text="Exit",command=self.Exit, cursor="hand2",font=("Times new roman",12,"bold"),bg="darkblue",fg="white")
        b1_8.place(x=3,y=335,width=190,height=25)
    
#========================================Function Buttos============================
    def open_img(self):
        os.startfile("dataset")

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def developer(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    def face_recognition(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def attendance(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
        
    def connect_database(self):
        self.new_window=Toplevel(self.root)
        self.app=Connect_database(self.new_window)

    def Exit(self):
        self.Exit=messagebox.askyesno("Face Rcognition","Are you sure Exit this project?",parent=self.root)
        if self.Exit>0:
            self.root.destroy()
        else:
            return
        
        
        
if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
