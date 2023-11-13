from tkinter import*
from tkinter import ttk
from tkinter import  filedialog
from PIL import Image,ImageTk
from tkinter import messagebox
import pymysql
import cv2
import os
import csv

mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1400x700+0+0")
        self.root.title("Student Attendance System")

        #======================================Variables=================================
        self.var_id = StringVar()
        self.var_std_name = StringVar()
        self.var_roll = StringVar()
        self.var_dep = StringVar()
        self.var_time = StringVar()
        self.var_date = StringVar()
        self.var_att_status = StringVar()

#background Image
        img3= Image.open(r"image/Black.png")
        img3=img3.resize((1530,1900),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1350,height=1900)

        title_1b1=Label(bg_img,text="Student Attendance System",font=("Times new roman",30,"bold"),bg="BLACK",fg="white")
        title_1b1.place(x=0,y=3,width=1350,height=30)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=5,y=40,width=1335,height=650)

#*********************************************************************************************
 
  #left label frame
        Right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Attendance Details",font=("Times new roman",12,"bold"))
        Right_frame.place(x=10,y=10,width=700,height=630)


#==================================Table Frame===========================
        #Table Frame
        table_frame=Frame(Right_frame,bd=2,relief=RIDGE)
        table_frame.place(x=10,y=10,width=680,height=580)

        scroll_x = ttk.Scrollbar(table_frame, orient = HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient = VERTICAL)
        self.attendancereporttable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attenddance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.attendancereporttable.xview)
        scroll_y.config(command=self.attendancereporttable.yview)

        self.attendancereporttable.heading("id", text="StudentId")
        self.attendancereporttable.heading("roll", text="Roll No")
        self.attendancereporttable.heading("name", text="Name")
        self.attendancereporttable.heading("department", text="Department")
        self.attendancereporttable.heading("time", text="Time")
        self.attendancereporttable.heading("date", text="Date")
        self.attendancereporttable.heading("attenddance", text="Attenddance")
        self.attendancereporttable["show"]="headings"

        self.attendancereporttable.column("id", width=90)
        self.attendancereporttable.column("roll", width=90)
        self.attendancereporttable.column("name", width=90)
        self.attendancereporttable.column("department", width=90)
        self.attendancereporttable.column("time", width=90)
        self.attendancereporttable.column("date", width=90)
        self.attendancereporttable.column("attenddance", width=90)

        self.attendancereporttable.pack(fill=BOTH,expand=1)
        self.attendancereporttable.bind("<ButtonRelease>",self.get_cursor)

#########################################################
#Right label frame
      
        Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Information",font=("Times new roman",12,"bold"))
        Left_frame.place(x=720,y=10,width=600,height=630)

#Class Student Information
        class_student_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Class Student Attendance Information",font=("Times new roman",12,"bold"))
        class_student_frame.place(x=10,y=50,width=580,height=300)

        # Student Id
        studentId_label = Label(class_student_frame, text="Student Id :", font=("Times new roman", 12, "bold"))
        studentId_label.grid(row=0, column=0, padx=2,pady=20, sticky=W)
        #Student Id Entry Box
        studentId_entry=ttk.Entry(class_student_frame,textvariable=self.var_id,width=18, font=("Times new roman", 12, "bold"))
        studentId_entry.grid(row=0, column=1, padx=2,pady=20, sticky=W)
        #------------------------------------------------------------------------------------------------

        # Student name
        studentName_label = Label(class_student_frame, text="Name :", font=("Times new roman", 12, "bold"))
        studentName_label.grid(row=0, column=2, padx=2,pady=20, sticky=W)
        #Student Name Entry Box
        studentName_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=17, font=("Times new roman", 12, "bold"))
        studentName_entry.grid(row=0, column=3, padx=2,pady=20, sticky=W)
        #----------------------------------------------------------------------------------------------------

        # Student class Division
        student_roll_label = Label(class_student_frame, text="Roll :", font=("Times new roman", 12, "bold"))
        student_roll_label.grid(row=1, column=0, padx=2,pady=20, sticky=W)
        #Student Class Division Entry Box
        #studentdivision_entry=ttk.Entry(class_student_frame,textvariable=self.var_div,width=20, font=("Times new roman", 12, "bold"))
        student_roll_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=18, font=("Times new roman", 12, "bold"))
        student_roll_entry.grid(row=1, column=1, padx=2,pady=20, sticky=W)
        # ----------------------------------------------------------------------------------------------------

        # Student ROll No.
        student_dep_label = Label(class_student_frame, text="Department :", font=("Times new roman", 12, "bold"))
        student_dep_label.grid(row=1, column=2, padx=2, pady=20, sticky=W)
        # Student Roll No. Entry Box
        student_dep_entry = ttk.Entry(class_student_frame,textvariable=self.var_dep,width=17, font=("Times new roman", 12, "bold"))
        student_dep_entry.grid(row=1, column=3, padx=2, pady=20, sticky=W)
        #------------------------------------------------------------------------------------------------------
        # Student Gender
        student_time_label = Label(class_student_frame, text="Time :", font=("Times new roman", 12, "bold"))
        student_time_label.grid(row=2, column=0, padx=2, pady=20, sticky=W)
        # Student Gender Entry Box
        student_time_entry = ttk.Entry(class_student_frame,textvariable=self.var_time, width=18, font=("Times new roman", 12, "bold"))
        student_time_entry.grid(row=2, column=1, padx=2, pady=20, sticky=W)
        #-------------------------------------------------------------------------------------------
        # Student Date of Birth
        student_date_label = Label(class_student_frame, text="Date :", font=("Times new roman", 12, "bold"))
        student_date_label.grid(row=2, column=2, padx=2, pady=20, sticky=W)
        # Student Date of Birth Entry Box
        student_date_entry = ttk.Entry(class_student_frame,textvariable=self.var_date, width=17, font=("Times new roman", 12, "bold"))
        student_date_entry.grid(row=2, column=3, padx=2, pady=20, sticky=W)
        #---------------------------------------------------------------------------------------

        # Student Date of Birth
        attendance_status_label = Label(class_student_frame, text="Attendance Status :", font=("Times new roman", 12, "bold"))
        attendance_status_label.grid(row=3, column=0, padx=5, pady=20, sticky=W)

        # Student Gender Entry Box
        attendance_status_combo = ttk.Combobox(class_student_frame,textvariable=self.var_att_status, font=("Times new roman", 12, "bold"), state="readonly",width=18)
        attendance_status_combo["values"] = ("Status", "Present", 'Absent')
        attendance_status_combo.current(0)
        attendance_status_combo.grid(row=3, column=1, padx=5, pady=20, sticky=W)


        #Buttons Frame
        btn_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,font=("Times new roman",12,"bold"))
        btn_frame.place(x=10,y=440,width=575,height=38)

        save_btn=Button(btn_frame,text='Import csv',command=self.importcsv,width=15,font=("Times new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text='Export csv',command=self.exportcsv,width=15,font=("Times new roman",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        save_btn=Button(btn_frame,text='Update',width=15,font=("Times new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text='Reset',command=self.reset,width=15,font=("Times new roman",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

#===========================Import csv File====================
    def fetch_Data(self,rows):
        self.attendancereporttable.delete(*self.attendancereporttable.get_children())
        for i in rows:
            self.attendancereporttable.insert("",END,values=i)

    def importcsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetch_Data(mydata)

    def exportcsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data found to export ",parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV",filetypes=(("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to "+os.path.basename(fln)+" Successfully")
        except Exception as es:
            messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)


    #=======================================Get Cursor===================================
    def get_cursor(self,event=""):
        cursor_focus=self.attendancereporttable.focus()
        content=self.attendancereporttable.item(cursor_focus)
        data=content["values"]
        self.var_id.set(data[0]),
        self.var_roll.set(data[1]),
        self.var_std_name.set(data[2]),
        self.var_dep.set(data[3]),
        self.var_time.set(data[4]),
        self.var_date.set(data[5]),
        self.var_att_status.set(data[6])

    def reset(self):
        self.var_id.set(""),
        self.var_roll.set(""),
        self.var_std_name.set(""),
        self.var_dep.set(""),
        self.var_time.set(""),
        self.var_date.set(""),
        self.var_att_status.set("")


if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()
