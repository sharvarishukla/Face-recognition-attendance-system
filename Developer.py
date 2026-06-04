from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

# ================= Developer Screen =================
class Developer:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition System")
        self.root.geometry("1530x790+0+0")

        # ===== Frame container for Developer screen =====
        self.frame = Frame(self.root)
        self.frame.pack(fill=BOTH, expand=True)

        # ===== Background Image =====
        img = Image.open(r"C:\Users\madhu\OneDrive\Desktop\Face_Regonition _Attendance_System\college_images\developer.jpg")
        img = img.resize((1530, 790), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        bg_img = Label(self.frame, image=self.photoimg)
        bg_img.place(x=0, y=0, width=1530, height=790)

        # ===== Title =====
        title_lbl = Label(bg_img, text="DEVELOPER", font=("times new roman", 35, "bold"),
                          bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=50)

        # ===== Exit Button =====
        btn_exit = Button(bg_img, text="EXIT", font=("Segoe UI", 12, "bold"),
                          bg="#e53935", fg="white", cursor="hand2",
                          command=self.exit_developer)
        btn_exit.place(x=1400, y=10, width=120, height=30)

         # == Developer 1 =====
        dev1_frame = Frame(bg_img, bd=4, relief=RIDGE, bg="white")
        dev1_frame.place(x=260, y=100, width=500, height=700)
        img1 = Image.open(r"C:\Users\madhu\OneDrive\Desktop\Face_Regonition _Attendance_System\college_images\1_5TRuG7tG0KrZJXKoFtHlSg.jpeg")
        img1 = img1.resize((200, 200), Image.LANCZOS)
        self.dev1_img = ImageTk.PhotoImage(img1)
        dev1_photo = Label(dev1_frame, image=self.dev1_img, bd=2, relief=RIDGE)
        dev1_photo.pack(pady=15)
        dev1_text = Label(dev1_frame, text="Name: Sharvari Shukla\nRole: Developer\nResponsibilities:\n- UI Optimization\n- System Testing\n- Database Integration\n- Model Training\n- Face Detection\nResponsibilities:\n- Attendance Automation\n- System Optimization\n\nEmail: sharvarishukla21@gmail.com\nContact: 7058356881",
                          font=("Segoe UI", 14), bg="white", justify=LEFT, anchor="nw", wraplength=460)
        dev1_text.pack(fill=BOTH, expand=True, padx=15, pady=10)

       
    def exit_developer(self):
       
        from main import Face_Recognition_System

        for widget in self.root.winfo_children():
            widget.destroy()

        Face_Recognition_System(self.root)
# ================= RUN APP =================
if __name__ == "__main__":
    root = Tk()
    Developer(root)
    root.mainloop()