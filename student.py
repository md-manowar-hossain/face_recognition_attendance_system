from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from time import strftime
from tkinter import messagebox
import pymysql
import cv2
import os


# Parent Class
class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Student Management System")
        
        #======================================Variables=================================
        self.var_dep=StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_id = StringVar()
        self.var_name = StringVar()
        self.var_section = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()
        self.var_radio1=StringVar()

        # background Image
        img3 = Image.open(r"image/Black.png")
        img3 = img3.resize((1530, 760), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=0, width=1350, height=700)

        title_1b1 = Label(bg_img, text="STUDENT MANAGEMENT SYSTEM", font=("Times new roman", 35, "bold"), bg="BLACK", fg="white")
        title_1b1.place(x=0, y=5, width=1350, height=50)

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=5, y=60, width=1335, height=650)

        # button
        b1_1 = Button(bg_img, text="Register New Student", command=self.registration, cursor="hand2", font=("Times new roman", 18, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=310, y=250, width=250, height=45)

        b1_2 = Button(bg_img, text="Student Details", command=self.update_student_details, cursor="hand2", font=("Times new roman", 18, "bold"), bg="darkblue", fg="white")
        b1_2.place(x=760, y=250, width=250, height=45)

        b1_3 = Button(bg_img, text="Exit", command=self.exit_app, cursor="hand2", font=("Times new roman", 18, "bold"), bg="darkblue", fg="white")
        b1_3.place(x=595, y=350, width=140, height=45)

    def registration(self):
        self.new_window = Toplevel(self.root)
        self.app = Registration(self.new_window)

    def update_student_details(self):
        self.new_window = Toplevel(self.root)
        self.app =UpdateDetails(self.new_window)

    def exit_app(self):
        self.root.destroy()
        
#==================================================================================

    def student_form(self, Right_Frame):

        #Current curse Information
        current_curse_frame=LabelFrame(Right_Frame,bd=2,relief=RIDGE,text="Current Curse",font=("Times new roman",12,"bold"))
        current_curse_frame.place(x=10,y=20,width=575,height=110)
#----------------------------------------------------------------------------------------------
        #Department Label
        dep_label=Label(current_curse_frame,text="Department",font=("Times new roman",12,"bold"),)
        dep_label.grid(row=0,column=0,padx=0,sticky=W)
        
        # Department Label ComboBox
        dep_combo=ttk.Combobox(current_curse_frame,textvariable=self.var_dep,font=("Times new roman",12,"bold"),state="readonly")
        dep_combo["values"]=("Select Department","CSE",'IT',"Civil","Mechnical",'BBA')
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=5,sticky=W)
# -----------------------------------------------------------------------------------------------
        # Course Label
        dep_label = Label(current_curse_frame, text="Course", font=("Times new roman", 12, "bold"))
        dep_label.grid(row=0, column=2, padx=10, sticky=W)
        
        # Course Label ComboBox
        dep_combo = ttk.Combobox(current_curse_frame,textvariable=self.var_course,font=("Times new roman", 12, "bold"), state="readonly")
        dep_combo["values"] = ("Select Course", "Numerical Methods", 'Computer Networks', "Pattern Recoggnition", "Mobile Application","Image Processing and Computer Vision",'Software Engineering','Simulation and Modelling','Artificial Intelligence','Computer Graphics')
        dep_combo.current(0)
        dep_combo.grid(row=0, column=3, padx=0, pady=5, sticky=W)
# ------------------------------------------------------------------------------------------------
        # Year Label
        dep_label = Label(current_curse_frame,text="Year",font=("Times new roman", 12, "bold"))
        dep_label.grid(row=1, column=0, padx=0, sticky=W)
        
        # Year Label ComboBox
        dep_combo = ttk.Combobox(current_curse_frame,textvariable=self.var_year,font=("Times new roman", 12, "bold"), state="readonly")
        dep_combo["values"] = ("Select Year","2020-21", "2021-22", '2022-23', "2023-24", "2024-25","2025-26","2026-27","2027-28","2028-29","2029-30")
        dep_combo.current(0)
        dep_combo.grid(row=1, column=1, padx=0, pady=5, sticky=W)

# --------------------------------------------------------------------------------------------------
        # Semester Label
        dep_label = Label(current_curse_frame, text="Semester", font=("Times new roman", 12, "bold"))
        dep_label.grid(row=1, column=2, padx=10, sticky=W)
        
        # Semester Label ComboBox
        dep_combo = ttk.Combobox(current_curse_frame,textvariable=self.var_semester,font=("Times new roman", 12, "bold"), state="readonly")
        dep_combo["values"] = ("Select Semester", "Fall", 'Summer', "Spring")
        dep_combo.current(0)
        dep_combo.grid(row=1, column=3, padx=2, pady=5, sticky=W)
        
#==================== Class Student Information ========================
        #Class Student Frame
        class_student_frame=LabelFrame(Right_Frame,bd=2,relief=RIDGE,text="Class Student Information",font=("Times new roman",12,"bold"))
        class_student_frame.place(x=10,y=150,width=575,height=440)
        
        # Student Id
        studentId_label = Label(class_student_frame, text="Student Id :", font=("Times new roman", 12, "bold"))
        studentId_label.grid(row=0, column=0, padx=2,pady=10, sticky=W)
        
        #Student Id Entry Box
        studentId_entry=ttk.Entry(class_student_frame,textvariable=self.var_id, font=("Times new roman", 12, "bold"))
        studentId_entry.grid(row=0, column=1, padx=2,pady=10, sticky=W)
#-----------------------------------------------------------------
        # Student name
        studentName_label = Label(class_student_frame, text="Student Name :", font=("Times new roman", 12, "bold"))
        studentName_label.grid(row=0, column=2, padx=5,pady=10, sticky=W)
        
        #Student Name Entry Box
        studentName_entry=ttk.Entry(class_student_frame,textvariable=self.var_name, font=("Times new roman", 12, "bold"))
        studentName_entry.grid(row=0, column=3, padx=2,pady=10, sticky=W)

#----------------------------------------------------------------------------------------------------
        # Student class Division/Section
        studentdivision_label = Label(class_student_frame, text="Section :", font=("Times new roman", 12, "bold"))
        studentdivision_label.grid(row=1, column=0, padx=2,pady=10, sticky=W)

        #Student Class Division Entry Box
        studentdivision_entry=ttk.Entry(class_student_frame,textvariable=self.var_section,font=("Times new roman", 12, "bold"))
        studentdivision_entry.grid(row=1, column=1, padx=2,pady=10, sticky=W)
# ----------------------------------------------------------------------------------------------------

        # Student ROll No.
        student_roll_no_label = Label(class_student_frame, text="Roll No. :", font=("Times new roman", 12, "bold"))
        student_roll_no_label.grid(row=1, column=2, padx=5, pady=10, sticky=W)
        
        # Student Roll No. Entry Box
        student_roll_no_entry = ttk.Entry(class_student_frame,textvariable=self.var_roll,font=("Times new roman", 12, "bold"))
        student_roll_no_entry.grid(row=1, column=3, padx=2, pady=10, sticky=W)
#------------------------------------------------------------------------------------------------------
        # Student Gender
        student_gender_label = Label(class_student_frame, text="Gender :", font=("Times new roman", 12, "bold"))
        student_gender_label.grid(row=2, column=0, padx=2, pady=10, sticky=W)
        
        # Student Gender Entry Box
        student_gender_combo = ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("Times new roman", 12, "bold"), state="readonly",width=18)
        student_gender_combo["values"] = ("Select Gender", "Male", 'Female', "Others")
        student_gender_combo.current(0)
        student_gender_combo.grid(row=2, column=1, padx=2, pady=10, sticky=W)
#-------------------------------------------------------------------------------------------
        # Student Date of Birth
        student_dob_label = Label(class_student_frame, text="D.O.B. :", font=("Times new roman", 12, "bold"))
        student_dob_label.grid(row=2, column=2, padx=5, pady=10, sticky=W)
        
        # Student Date of Birth Entry Box
        student_dob_entry = ttk.Entry(class_student_frame,textvariable=self.var_dob, font=("Times new roman", 12, "bold"))
        student_dob_entry.grid(row=2, column=3, padx=2, pady=10, sticky=W)
#---------------------------------------------------------------------------------------
        # Student Email
        student_email_label = Label(class_student_frame, text="Email :", font=("Times new roman", 12, "bold"))
        student_email_label.grid(row=3, column=0, padx=2, pady=10, sticky=W)
        
        # Student Date of Birth Entry Box
        student_email_entry = ttk.Entry(class_student_frame,textvariable=self.var_email, font=("Times new roman", 12, "bold"))
        student_email_entry.grid(row=3, column=1, padx=2, pady=10, sticky=W)
#---------------------------------------------------------------------------------------------
        # Student Phone Number
        student_phone_no_label = Label(class_student_frame, text="Phone No. :", font=("Times new roman", 12, "bold"))
        student_phone_no_label.grid(row=3, column=2, padx=5, pady=10, sticky=W)
        
        # Student Phone Number Entry Box
        student_phone_no_entry = ttk.Entry(class_student_frame,textvariable=self.var_phone, font=("Times new roman", 12, "bold"))
        student_phone_no_entry.grid(row=3, column=3, padx=2, pady=10, sticky=W)
#-------------------------------------------------------------------------------------------
        # Student Address
        student_address_label = Label(class_student_frame, text="Address :", font=("Times new roman", 12, "bold"))
        student_address_label.grid(row=4, column=0, padx=2, pady=10, sticky=W)
        
        # Student Address Entry Box
        student_address_entry = ttk.Entry(class_student_frame,textvariable=self.var_address, font=("Times new roman", 12, "bold"))
        student_address_entry.grid(row=4, column=1, padx=2, pady=10, sticky=W)
#------------------------------------------------------------------------------------------
        # Student Class Teacher Name
        student_teacher_label = Label(class_student_frame, text="Teacher :", font=("Times new roman", 12, "bold"))
        student_teacher_label.grid(row=4, column=2, padx=5, pady=10, sticky=W)
        
        # Student Class Teacher Name Entry Box
        student_teacher_entry = ttk.Entry(class_student_frame,textvariable=self.var_teacher,font=("Times new roman", 12, "bold"))
        student_teacher_entry.grid(row=4, column=3, padx=1, pady=10, sticky=W)
#--------------------------------------------------------------------------------------
        #Radio buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text='Take Photo Sample',value='Yes')
        radiobtn1.grid(row=6,column=1,padx=5, pady=20)
        
        #Radio buttons
        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text='No Photo Sample',value='NO')
        radiobtn2.grid(row=6,column=3,padx=5, pady=20)  
        
        
        
#=======================================Add Data===================================

    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="" or self.var_roll.get()=="":
            messagebox.showerror("Error","All Fields are Required",parent=self.root)
        else:
            try:
                conn=pymysql.connect(host='localhost', user='root', password="", database="face")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_id.get(),
                    self.var_name.get(),
                    self.var_section.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get()
                    
                ))
                conn.commit()
                # self.fetch_data()
                messagebox.showinfo("Success","Student details has been added Sucessfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}", parent=self.root)
                
            self.root.destroy()


#=======================================Fetch Data===================================
    def fetch_data(self):
        conn=pymysql.connect(host='localhost', user='root', password="", database="face")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

#=======================================Get Cursor===================================
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_id.set(data[4]),
        self.var_name.set(data[5]),
        self.var_section.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

#=================================================Reset Function======================
    def reset_data(self):
        self.var_dep.set("Select Department"),
        self.var_course.set("Select Course"),
        self.var_year.set("Select Year"),
        self.var_semester.set("Select Semester"),
        self.var_id.set(""),
        self.var_name.set(""),
        self.var_section.set(""),
        self.var_roll.set(""),
        self.var_gender.set("Select Gender"),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_teacher.set(""),
        self.var_radio1.set("")


#====================================== Update Function ================================
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="" or self.var_roll.get()=="":
            messagebox.showerror("Error","All Fields are Required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("update","Do you want to Update This Student Details",parent=self.root)
                if Update>0:
                    conn =pymysql.connect(host='localhost', user='root', password="", database="face")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set Department=%s,Course=%s,Year=%s,Semester=%s,Student_id=%s,Name=%s,Section=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSamplesStatus=%s where Roll=%s",(

                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_id.get(),
                        self.var_name.get(),
                        self.var_section.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_roll.get()
                        
                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student Details SuccessFully Update Completed",parent=self.root)
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)
                
#==========================Delete Student================================
    def delete_data(self):
        if self.var_roll.get()=="":
            messagebox.showerror("Error","Student Roll must be required",parent=self.root)

        else:
            try:
                delete=messagebox.askyesno("Delete","Do you want to Delet This Student Details",parent=self.root)
                if delete>0:
                    conn =pymysql.connect(host='localhost', user='root', password="",database="face")
                    my_cursor = conn.cursor()
                    sql="delete from student where Roll=%s"
                    val=(self.var_roll.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully Deleted Student Detials",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)

#========================================Search Student Data=====================================
    def search_data(self):
        if self.var_com_search.get()=="" or self.var_search.get()=="":
            messagebox.showerror("Error","Please Select Option")
        else:
            try:
                conn =pymysql.connect(host='localhost', user='root', password="", database="face")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student where "+str(self.var_com_search.get())+" LIKE '%"+str(self.var_search.get())+"%'")
                data=my_cursor.fetchall()
                if len(data)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in data:
                        self.student_table.insert("",END,values=i)
                    conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)
                
#=====================================Generate data set and take photo samples====================
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="" or self.var_roll.get()=="":
            messagebox.showerror("Error","All Fields are Required",parent=self.root)
        else:
            try:
                conn =pymysql.connect(host='localhost', user='root', password="",database="face")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Department=%s, Course=%s,Year=%s,Semester=%s,Name=%s,Section=%s,Student_id=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSamplesStatus=%s where Roll=%s", (

                                      self.var_dep.get(),
                                      self.var_course.get(),
                                      self.var_year.get(),
                                      self.var_semester.get(),
                                      self.var_name.get(),
                                      self.var_section.get(),
                                      self.var_id.get(),
                                      self.var_gender.get(),
                                      self.var_dob.get(),
                                      self.var_email.get(),
                                      self.var_phone.get(),
                                      self.var_address.get(),
                                      self.var_teacher.get(),
                                      self.var_radio1.get(),
                                      self.var_roll.get()
                 ))

                std_roll=self.var_roll.get()
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                
                #==========Load predifiend data on face frontals from opencv============
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    if not os.path.exists("dataset"):
                        os.makedirs("dataset")

                    if not os.path.exists("Attendance"):
                        os.makedirs("Attendance")

                    #Scaling factor=1.3
                    #minimum Neighbor=5

                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                    
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="dataset/user."+str(std_roll)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Crooped Face", face)

                    if cv2.waitKey(1)==13 or int(img_id)==20:
                        break
                    
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating Data sets Completed")
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)
        
#====================================================================================================
#========================================= Child Class ==============================================
#========================================= Registration =============================================

class Registration(Student):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.root.title("Student Registration")
        self.root.geometry("1350x700+0+0")

        #background Image
        img3= Image.open(r"image/Black.png")
        img3=img3.resize((1530,760),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1350,height=700)

        title_1b1=Label(bg_img,text="Student Registration",font=("Times new roman",26,"bold"),bg="black",fg="white")
        title_1b1.place(x=0,y=3,width=1350,height=30)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=5,y=40,width=1335,height=720)
        
        # label frame
        Right_Frame=LabelFrame(main_frame,bd=2,relief=RIDGE, text="Student Information",font=("Times new roman",12,"bold"))
        Right_Frame.place(x=360,y=10,width=600,height=635)
        
        
        self.student_form(Right_Frame)
        
#======================================== Command Buttons ===========================================
        # Button Frame        
        button_frame=Frame(Right_Frame,bd=2,border=0)
        button_frame.place(x=12,y=470,width=572,height=100)
        
        # Buttons Sub Frame
        btn_frame=Frame(button_frame,bd=2,relief=RIDGE,bg="black")
        btn_frame.place(x=10,y=10,width=550,height=35)    
   
        #save
        save_btn=Button(btn_frame,text='Save', command=self.add_data,width=32,font=("Times new roman",12,"bold"),bg="dark blue",fg="white")
        save_btn.grid(row=0,column=0,)  

        #Reset
        reset_btn=Button(btn_frame,text='Reset',command=self.reset_data,width=35,font=("Times new roman",13,"bold"),bg="dark blue",fg="white")
        reset_btn.grid(row=0,column=3)

        # Buttons Sub Frame
        btn_frame1=Frame(button_frame,bd=2,relief=RIDGE,bg="black")
        btn_frame1.place(x=150,y=50,width=300,height=35)

        take_photo_sample_btn=Button(btn_frame1,command=self.generate_dataset,text='Take Photo Sample',width=34,font=("Times new roman",12,"bold"),bg="dark blue",fg="white")
        take_photo_sample_btn.grid(row=1,column=0)

        #save_btn=Button(btn_frame1,text='No Photo Sample',width=35,font=("Times new roman",12,"bold"),bg="dark blue",fg="white")
        #save_btn.grid(row=1,column=1)


#====================================================================================================
#========================================= Child Class ==============================================
#======================================== Update Details ============================================

class UpdateDetails(Student):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.root.title("Student Details")
        self.root.geometry("1350x2000+0+0")

        #background Image
        img3= Image.open(r"image/Black.png")
        img3=img3.resize((1530,1900),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1350,height=1900)

        title_1b1=Label(bg_img,text="Student Details",font=("Times new roman",30,"bold"),bg="BLACK",fg="white")
        title_1b1.place(x=0,y=3,width=1350,height=30)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=5,y=40,width=1335,height=650)
        
#=====================================================================================================
#========================================= Left Area =================================================
 
        #left label frame
        Left_Frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("Times new roman",12,"bold"))
        Left_Frame.place(x=10,y=10,width=700,height=630)


        #Search frame
        search_frame=LabelFrame(Left_Frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("Times new roman",12,"bold"))
        search_frame.place(x=20,y=20,width=655,height=80)

        #Search  Label
        Search_label=Label(search_frame,text="Search By:",font=("Times new roman",12,"bold"),fg="Darkblue")
        Search_label.grid(row=0,column=0,padx=5,sticky=W)

        # Search  Label ComboBox
        self.var_com_search=StringVar()
        Search_combo=ttk.Combobox(search_frame,textvariable=self.var_com_search,font=("Times new roman",12,"bold"),state="readonly",width=12)
        Search_combo["values"]=("Select","Student Id",'Phone number',"Name")
        Search_combo.current(0)
        Search_combo.grid(row=0,column=1,padx=5,pady=10,sticky=W)
        
        # Student Phone Number Entry Box
        self.var_search=StringVar()
        Search_entry = ttk.Entry(search_frame,textvariable=self.var_search, font=("Times new roman", 12, "bold"),width=20)
        Search_entry.grid(row=0, column=2, padx=5, pady=10, sticky=W)
        
        #button
        Search_btn=Button(search_frame,text='Search',command=self.search_data,width=12,font=("Times new roman",12,"bold"),bg="dark blue",fg="white")
        Search_btn.grid(row=0,column=3,padx=5, pady=10, sticky=W)

        showall_btn=Button(search_frame,text='Show All',command=self.fetch_data,width=12,font=("Times new roman",12,"bold"),bg="dark blue",fg="white")
        showall_btn.grid(row=0,column=4,padx=5, pady=10, sticky=W)

        #Table Frame
        table_frame=Frame(Left_Frame,bd=2,relief=RIDGE)
        table_frame.place(x=20,y=120,width=655,height=470)
        
        scroll_x = ttk.Scrollbar(table_frame, orient = HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient = VERTICAL)
        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","section","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)


        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="Student_id")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("section", text="Section")
        self.student_table.heading("roll", text="Roll")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="Dob")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="PhotoSamplesStatus")
        self.student_table["show"]="headings" 

        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("section", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("photo", width=150)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
#================================================================================
#=============================== Right Area =====================================
        Right_Frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Information",font=("Times new roman",12,"bold"))
        Right_Frame.place(x=720,y=10,width=600,height=630)
        
        self.student_form(Right_Frame)
        
        
#=================================== Command Buttons =======================================
        # Button Frame        
        button_frame=Frame(Right_Frame,bd=2,border=0)
        button_frame.place(x=12,y=470,width=572,height=100)
        
        # btn Sub Frame black       
        btn_frame=Frame(button_frame,bd=2,relief=RIDGE,bg="black")
        btn_frame.place(x=25,y=10,width=520,height=35)    
   
        
        save_btn=Button(btn_frame,text='Add New', command=self.add_data,width=14,font=("Times new roman",12,"bold"),bg="dark blue",fg="white")
        save_btn.grid(row=0,column=0,)  

        update_btn=Button(btn_frame,text='Update', command=self.update_data,width=13,font=("Times new roman",12,"bold"),bg="dark blue",fg="white")
        update_btn.grid(row=0,column=1)

        reset_btn=Button(btn_frame,text='Reset',command=self.reset_data,width=13,font=("Times new roman",12,"bold"),bg="dark blue",fg="white")
        reset_btn.grid(row=0,column=3)

        save_btn=Button(btn_frame,text='Delete', command=self.delete_data,width=14,font=("Times new roman",12,"bold"),bg="dark blue",fg="white")
        save_btn.grid(row=0,column=2)

        # btn Sub Frame black       
        btn_frame1=Frame(button_frame,bd=2,relief=RIDGE,bg="black")
        btn_frame1.place(x=80,y=55,width=410,height=35)

        take_photo_sample_btn=Button(btn_frame1,command=self.generate_dataset,text='Take Photo Sample',width=22,font=("Times new roman",12,"bold"),bg="dark blue",fg="white")
        take_photo_sample_btn.grid(row=1,column=0)

        save_btn=Button(btn_frame1,text='No Photo Sample',width=22,font=("Times new roman",12,"bold"),bg="dark blue",fg="white")
        save_btn.grid(row=1,column=1)

#================================= Logout ===================================
        b1_9=Button(title_1b1,text="Logout",command=self.root, cursor="hand2", font=("Times new roman", 10, "bold"),bg="black",fg="white")
        b1_9.place(x=1250,y=5,width=80,height=20)      
        

if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()