from tkinter import*
from PIL import Image,ImageTk

mydata=[]
class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Face Recognition System")
        
        # background Image
        img3 = Image.open(r"image/Black.png")
        img3 = img3.resize((1530, 760), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=0, width=1350, height=700)

        #====================================== Variables =================================
        title_1b1=Label(bg_img,text="Student Management System Help Line and Developer ",font=("Times new roman",32,"bold"),bg="white",fg="blue")
        title_1b1.place(x=0, y=5, width=1350, height=50)

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=5, y=65, width=1335, height=650)

        #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE)
        Left_frame.place(x=10,y=10,width=600,height=620)

        #Third Image
        img_l=Image.open(r"image/Black.png")
        img_l=img_l.resize((590,270),Image.LANCZOS)
        self.photoimg_l=ImageTk.PhotoImage(img_l)

        f_1bl1=Label(Left_frame,image=self.photoimg_l)
        f_1bl1.place(x=5,y=5,width=590,height=270)

        # Class Student Information
        help_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE)
        help_frame.place(x=10,y=280,width=580,height=325)

        help1_label = Label(help_frame, text="Requirement 1:", font=("Times new roman", 15, "bold"), fg="red")
        help1_label.place(x=50,y=50)
        
        help1_label = Label(help_frame, text="MySQL Server", font=("Times new roman", 15, "bold"),fg='green')
        help1_label.place(x=190,y=52)

        help1_label = Label(help_frame, text="Requirement 2:", font=("Times new roman", 15, "bold"), fg="red")
        help1_label.place(x=50,y=80)

        help1_label = Label(help_frame, text="Student Roll Must be Integer.", font=("Times new roman", 15, "bold"),fg='green')
        help1_label.place(x=190,y=82)



        #----------------------------------------------------------------------------------------------------

        #Right label frame
        Right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Developer Information",font=("Times new roman",10,"bold"))
        Right_frame.place(x=620,y=10,width=720,height=620)
        
        # ============================= Person 1 ===============================
        man1_frame=LabelFrame(Right_frame,bd=2,relief=RIDGE)
        man1_frame.place(x=10,y=10,width=220,height=290)

        img1=Image.open(r"image/Black.png")
        img1=img1.resize((220,180),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        bg_img1=Label(man1_frame,image=self.photoimg1)
        bg_img1.place(x=0,y=0,width=220,height=180)

        man1_label = Label(man1_frame, text="Arifur Rhaman", font=("Times new roman", 15, "bold"))
        man1_label.place(x=10,y=190)

        man1_label1 = Label(man1_frame, text="Lecturer, Department of CSE", font=("Times new roman", 12, "bold"))
        man1_label1.place(x=10,y=215)

        man1_label1 = Label(man1_frame, text="Project Supervisor", font=("Times new roman", 15, "bold"))
        man1_label1.place(x=10,y=240)
        
        # ============================= Person 2 ===============================
        man2_frame=LabelFrame(Right_frame,bd=2,relief=RIDGE)
        man2_frame.place(x=240,y=10,width=220,height=290)

        img2=Image.open(r"image/Black.png")
        img2=img2.resize((220,180),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        bg_img=Label(man2_frame,image=self.photoimg2)
        bg_img.place(x=0,y=0,width=220,height=180)


        man2_label = Label(man2_frame, text="Sayed Mynul Islam Apu", font=("Times new roman", 15, "bold"))
        man2_label.place(x=10,y=190)

        man2_label1 = Label(man2_frame, text="Id: CSE2001019168", font=("Times new roman", 15, "bold"))
        man2_label1.place(x=10,y=215)

        man2_label1 = Label(man2_frame, text="Project Programmer", font=("Times new roman", 15, "bold"))
        man2_label1.place(x=10,y=240)
        
        # ============================= Person 3 ===============================
        man3_frame=LabelFrame(Right_frame,bd=2,relief=RIDGE)
        man3_frame.place(x=470,y=10,width=220,height=290)

        img3=Image.open(r"image/Black.png")
        img3=img3.resize((220,180),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(man3_frame,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=220,height=180)

        man3_label = Label(man3_frame, text="Sabria Tarannum Orin", font=("Times new roman", 15, "bold"))
        man3_label.place(x=10,y=190)

        man3_label1 = Label(man3_frame, text="Id: CSE2001019183", font=("Times new roman", 15, "bold"))
        man3_label1.place(x=10,y=215)

        man3_label1 = Label(man3_frame, text="Project Captain", font=("Times new roman", 15, "bold"))
        man3_label1.place(x=10,y=240)
        
        # ============================= Person 4 ===============================
        man4_frame=LabelFrame(Right_frame,bd=2,relief=RIDGE)
        man4_frame.place(x=10,y=310,width=220,height=290)

        img4=Image.open(r"image/Black.png")
        img4=img4.resize((220,180),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img=Label(man4_frame,image=self.photoimg4)
        bg_img.place(x=0,y=0,width=220,height=180)

        man4_label = Label(man4_frame, text="Mohammad Sohag", font=("Times new roman", 15, "bold"))
        man4_label.place(x=10,y=190)

        man4_label1 = Label(man4_frame, text="Id: CSE2001019141", font=("Times new roman", 15, "bold"))
        man4_label1.place(x=10,y=215)

        man4_label1 = Label(man4_frame, text="Project Concept Creator", font=("Times new roman", 15, "bold"))
        man4_label1.place(x=10,y=240)
        
        # ============================= Person 5 ===============================
        man5_frame=LabelFrame(Right_frame,bd=2,relief=RIDGE)
        man5_frame.place(x=240,y=310,width=220,height=290)

        img5=Image.open(r"image/Black.png")
        img5=img5.resize((220,180),Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        bg_img=Label(man5_frame,image=self.photoimg5)
        bg_img.place(x=0,y=0,width=220,height=180)

        man5_label = Label(man5_frame, text="Meharab Hossain", font=("Times new roman", 15, "bold"))
        man5_label.place(x=10,y=190)

        man5_label1 = Label(man5_frame, text="Id: CSE2001019153", font=("Times new roman", 15, "bold"))
        man5_label1.place(x=10,y=215)

        man5_label1 = Label(man5_frame, text="Project Presenter", font=("Times new roman", 15, "bold"))
        man5_label1.place(x=10,y=240)



if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()
