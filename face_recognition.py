from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from time import strftime
from datetime import datetime
from tkinter import messagebox
import pymysql
# import mysql.connector
import os
import numpy as np
import cv2
import pandas
import time


date = time.strftime("%d_%m_%Y")
df =pandas.DataFrame(list(zip()))
if not os.path.exists("Attendance"):
    os.makedirs("Attendance")
paths =r'Attendance/stu' +str(date) +'.csv'.format()
df.to_csv(paths ,index=False)

class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Face Detection System")

        # background Image
        img3 = Image.open(r"image/Black.png")
        img3 = img3.resize((1530, 760), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=0, width=1350, height=700)

        title_1b1 = Label(bg_img, text="Face Recognition System", font=("Times new roman", 35, "bold"), bg="BLACK", fg="white")
        title_1b1.place(x=0, y=5, width=1350, height=50)

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=5, y=60, width=1335, height=650)



        # button
        b1_1 = Button(bg_img, text="Face Detection", command=self.face_recognition, cursor="hand2", font=("Times new roman", 18, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=550, y=400, width=250, height=45)

            #====================================Attendance==================================
    def mark_attendance(self,i,r,n,d):
        file="Attendance.csv"
        with open(file,'r+',newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"{i},{r},{n},{d},{dtString},{d1},Present\n")

 #================================Face Recognition===============================
    def face_recognition(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,recognizer):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=recognizer.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn = pymysql.connect(host='localhost', user='root', password='', database="face")
                my_cursor = conn.cursor()

                my_cursor.execute("select Name from student where Roll="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                # my_cursor.execute("select Roll from student where Roll="+str(id))
                # r=my_cursor.fetchone()
                # r="+".join(r)
                r=id

                my_cursor.execute("select Department from student where Roll="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)

                my_cursor.execute("select Student_id from student where Roll="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)

                if confidence>77:
                    cv2.putText(img,f"ID:{i}",(x,y-95),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x, y -65),cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img,f"Roll:{r}",(x,y-35),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}", (x,y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    self.mark_attendance(i, r,n,d)

                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0, 0, 255), 3)
                    cv2.putText(img,"Unknown Face", (x,y-5),cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coord=[x,y,w,y]

            return coord

        def recognize(img,recognizer,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",recognizer)
            return img

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read("classifier.xml")

        video_cap=cv2.VideoCapture(0, cv2.CAP_DSHOW)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,recognizer,faceCascade)
            cv2.imshow("Welcome to face Recignition",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()



if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()