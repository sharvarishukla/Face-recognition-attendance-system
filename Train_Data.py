from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
import cv2
import numpy as np
import os

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Attendance System")

        title = Label(self.root, text="Train Dataset",
                    font=("Segoe UI", 18, "bold"),
                    bg="#4a0bdd", fg="white")
        title.place(x=0, y=0, width=1530, height=45)

        # EXIT BUTTON
        exit_btn = Button(self.root, text="EXIT",
                        command=self.exit,
                        font=("times new roman", 15, "bold"),
                        bg="red", fg="white")
        exit_btn.place(x=1400, y=5, width=100, height=35)

        # Top Image
        img_top = Image.open(r"C:\Users\madhu\OneDrive\Desktop\Face_Regonition _Attendance_System\college_images\face-recognition.png")
        img_top = img_top.resize((1530, 325), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lb1 = Label(self.root, image=self.photoimg_top)
        f_lb1.place(x=0, y=55, width=1530, height=325)

        # Train Button
        b1 = Button(self.root, text="TRAIN DATA",command=self.train_classifier,
                    cursor="hand2",
                    font=("times new roman", 30, "bold"),
                    bg="blue", fg="white")
        b1.place(x=0, y=380, width=1530, height=60)

        # Bottom Image
        img_bottom = Image.open(r"C:\Users\madhu\OneDrive\Desktop\Face_Regonition _Attendance_System\college_images\face_det.png")
        img_bottom = img_bottom.resize((1530, 325), Image.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lb2 = Label(self.root, image=self.photoimg_bottom)
        f_lb2.place(x=0, y=440, width=1530, height=325)


    # EXIT FUNCTION
    def exit(self):
        from main import Face_Recognition_System

        for widget in self.root.winfo_children():
            widget.destroy()

        self.app = Face_Recognition_System(self.root)
        
    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') # Gray Scale Image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])   

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        
        ids=np.array(ids)

        ######## Train The Classifier And Save #######
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training DataSet Completed !!!")


# ================= MAIN =================
if __name__ == "__main__":
    root = Tk()
    app = Train(root)
    root.mainloop()