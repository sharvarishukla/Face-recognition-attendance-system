from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student_1 import Student
from Train_Data import Train
from Face_Detector import FaceDetect
from Attendance import Attendance
from Developer import Developer
import mysql.connector
import cv2
import os
import numpy as np
from photos import Photos
from Help_desk import HelpDesk
from Exit import Exit



class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        img=Image.open(r"C:\Users\madhu\OneDrive\Desktop\Face_Regonition _Attendance_System\college_images\1_5TRuG7tG0KrZJXKoFtHlSg.jpeg")
        img=img.resize((1530,790),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=0,width=1530,height=790)
        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

    
        #Student Button
        img1=Image.open(r"C:\Users\madhu\OneDrive\Desktop\Face_Regonition _Attendance_System\college_images\student.jpg")
        img1=img1.resize((220,220),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1) 

        b1=Button(bg_img,image=self.photoimg1,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)
        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=300,width=220,height=40) 

        # Detect Face Button
        img2=Image.open(r"C:\Users\madhu\OneDrive\Desktop\Face_Regonition _Attendance_System\college_images\face_detector1.jpg")
        img2=img2.resize((220,220),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2) 

        b2=Button(bg_img,image=self.photoimg2,cursor="hand2",command=self.face_detector )
        b2.place(x=500,y=100,width=220,height=220)  
        b2_1=Button(bg_img,text="Face Detector",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b2_1.place(x=500,y=300,width=220,height=40)

        # Attendance Button
        img3=Image.open(r"C:\Users\madhu\OneDrive\Desktop\Face_Regonition _Attendance_System\college_images\attendance.jpg")
        img3=img3.resize((220,220),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3) 

        b3=Button(bg_img,image=self.photoimg3,cursor="hand2",command=self.attendance)   
        b3.place(x=800,y=100,width=220,height=220)

        b3_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b3_1.place(x=800,y=300,width=220,height=40)


        # Help Button
        img4=Image.open(r"C:\Users\madhu\OneDrive\Desktop\Face_Regonition _Attendance_System\college_images\help.jpg")
        img4=img4.resize((220,220),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4) 

        b4=Button(bg_img,image=self.photoimg4,cursor="hand2",command=self.help_desk)
        b4.place(x=1100,y=100,width=220,height=220)
        b4_1=Button(bg_img,text="Help Desk",cursor="hand2",command=self.help_desk,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b4_1.place(x=1100,y=300,width=220,height=40)

        # Train Data Button
        img5=Image.open(r"C:\Users\madhu\OneDrive\Desktop\Face_Regonition _Attendance_System\college_images\IMG_1183_augmented_reality_faces1.jpg")
        img5=img5.resize((220,220),Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5) 

        b5=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.train_data)
        b5.place(x=200,y=400,width=220,height=220)  
        b5_1=Button(bg_img,text="Train Data",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b5_1.place(x=200,y=600,width=220,height=40)

        # Photos Button
        img6=Image.open(r"C:\Users\madhu\OneDrive\Desktop\Face_Regonition _Attendance_System\college_images\opencv_face_reco_more_data.jpg")
        img6=img6.resize((220,220),Image.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6) 

        b6=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.photos)
        b6.place(x=500,y=400,width=220,height=220)      
        b6_1=Button(bg_img,text="Photos",cursor="hand2",command=self.photos,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b6_1.place(x=500,y=600,width=220,height=40)

        # Developer Button
        img7=Image.open(r"C:\Users\madhu\OneDrive\Desktop\Face_Regonition _Attendance_System\college_images\dev.jpg")
        img7=img7.resize((220,220),Image.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b7=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.developer)
        b7.place(x=800,y=400,width=220,height=220)
        b7_1=Button(bg_img,text="Developer",cursor="hand2",command=self.developer,font=("times new roman",15,"bold"),bg="darkblue",fg="white") 
        b7_1.place(x=800,y=600,width=220,height=40)

        # Exit Button
        img8=Image.open(r"C:\Users\madhu\OneDrive\Desktop\Face_Regonition _Attendance_System\college_images\exit.jpg")
        img8=img8.resize((220,220),Image.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8) 

        b8=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.exit)
        b8.place(x=1100,y=400,width=220,height=220)

        b8_1=Button(bg_img,text="Exit",cursor="hand2",command=self.exit,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b8_1.place(x=1100,y=600,width=220,height=40)



    #### Function Button ####
    def student_details(self):
        # Clear all existing widgets in root
        for widget in self.root.winfo_children():
                widget.destroy()
    
    # Initialize the Student UI on the same root window
        self.app = Student(self.root)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_detector(self):
        self.new_window=Toplevel(self.root)
        self.app=FaceDetect(self.new_window)
    
    def exit(self):
        self.root.destroy()
    
    def attendance(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.app = Attendance(self.root)
    def developer(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    def photos(self):
        self.new_window=Toplevel(self.root)
        self.app=Photos(self.new_window)

    def help_desk(self):
        # clear dashboard widgets
        for widget in self.root.winfo_children():
            widget.destroy()

    # open help desk in same window
        self.app = HelpDesk(self.root)




if __name__ == "__main__":
    root = Tk()
    app = Face_Recognition_System(root)
    root.mainloop()