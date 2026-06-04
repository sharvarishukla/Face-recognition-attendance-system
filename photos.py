from tkinter import *
from PIL import Image, ImageTk
import os


class Photos:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # ================= Background =================
        img = Image.open(r"C:\Users\madhu\OneDrive\Desktop\Face_Regonition _Attendance_System\college_images\solid.jpg")
        img = img.resize((1530, 790), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        bg_img = Label(self.root, image=self.photoimg)
        bg_img.place(x=0, y=0, width=1530, height=790)

        # ================= Title =================
        title_lbl = Label(bg_img, text="DATASET PHOTOS",
                          font=("times new roman", 35, "bold"),
                          bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=50)

        # ================= Frame for Photos =================
        photo_frame = Frame(bg_img, bg="white")
        photo_frame.place(x=100, y=100, width=1300, height=600)

        # ================= Load Images =================
        folder_path = r"C:\Users\madhu\OneDrive\Desktop\Face_Regonition _Attendance_System\data"

        row = 0
        col = 0
        self.images = []

        for file in os.listdir(folder_path):

            path = os.path.join(folder_path, file)

            try:
                img = Image.open(path)
                img = img.resize((150, 150), Image.LANCZOS)

                photo = ImageTk.PhotoImage(img)
                self.images.append(photo)

                lbl = Label(photo_frame, image=photo, bd=2, relief=RIDGE)
                lbl.grid(row=row, column=col, padx=10, pady=10)

                col += 1

                if col == 7:   # 7 images per row
                    col = 0
                    row += 1

            except:
                pass

        # ================= Back Button =================
        back_btn = Button(bg_img, text="Back",
                          command=self.back_to_home,
                          font=("times new roman", 15, "bold"),
                          bg="darkblue", fg="white")
        back_btn.place(x=650, y=720, width=200, height=40)

    def back_to_home(self):
        self.root.destroy()


if __name__ == "__main__":
    root = Tk()
    app = Photos(root)
    root.mainloop()