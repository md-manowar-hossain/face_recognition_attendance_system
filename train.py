from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from time import strftime
from tkinter import messagebox
import pymysql
import os
import numpy as np
import cv2

class Train:
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

        title_1b1 = Label(bg_img, text="Train Dataset", font=("Times new roman", 35, "bold"), bg="BLACK", fg="white")
        title_1b1.place(x=0, y=5, width=1350, height=50)

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=5, y=60, width=1335, height=650)

        # button
        b1_1 = Button(bg_img, text="Training DataSet", command=self.train_dataset, cursor="hand2", font=("Times new roman", 18, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=550, y=400, width=250, height=45)

    def train_dataset(self):
        data_dir = "dataset"
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]
        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L')  # Gray Scale Image
            imageNp = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)        # Extra
            cv2.waitKey(1)==13

        ids = np.array(ids)

        # ==============================Train the dataset and save==============
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.train(faces, ids)
        recognizer.save("classifier.xml")
        messagebox.showinfo("Result", "Training Dataset Completed")


if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()