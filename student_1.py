from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector
import cv2
import os
from datetime import datetime



class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1580x750")
        self.root.title("Student Management System")

        # ================= VARIABLES =================
        self.vars = {
            "Student ID": StringVar(),
            "Roll": StringVar(),
            "Name": StringVar(),
            "Section": StringVar(),
            "College": StringVar(),
            "Department": StringVar(),
            "Course": StringVar(),
            "Semester": StringVar(),
            "Year": StringVar(),
            "Phone": StringVar(),
            "Email": StringVar(),
            "Address": StringVar(),
            "Gender": StringVar(),
            "DOB": StringVar()
        }

        # ================= HEADER =================
        header = Frame(self.root, bg="#1e1e2f", height=60)
        header.pack(fill=X)

        title = Label(header, text="Student Management System",
                    font=("Segoe UI", 18, "bold"),
                    bg="#1e1e2f", fg="white")
        title.pack(side=LEFT, padx=20)

        # EXIT BUTTON (redirects to main.py)
        btn_exit = Button(header, text="EXIT",
                        font=("Segoe UI", 10, "bold"),
                        bg="#e53935", fg="white",
                        cursor="hand2",
                        command=self.open_main)
        btn_exit.pack(side=RIGHT, padx=20, pady=10)

        # ================= MAIN FRAME =================
        main_frame = Frame(self.root, bg="white")
        main_frame.pack(fill=BOTH, expand=1, padx=10, pady=10)

        # ================= LEFT FRAME =================
        left_frame = LabelFrame(main_frame, text="Student Form",
                                font=("Calibri", 14, "bold"), bg="white")
        left_frame.pack(side=LEFT, fill=BOTH, expand=1, padx=10)

        canvas = Canvas(left_frame, bg="white")
        scrollbar = Scrollbar(left_frame, orient=VERTICAL, command=canvas.yview)
        form_frame = Frame(canvas, bg="white")

        form_frame.bind("<Configure>",
                        lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        canvas.create_window((0, 0), window=form_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side=LEFT, fill=BOTH, expand=1)
        scrollbar.pack(side=RIGHT, fill=Y)

        row = 0
        for field, var in self.vars.items():
            Label(form_frame, text=field,
                font=("Calibri", 11, "bold"),
                bg="white").grid(row=row, column=0, padx=15, pady=8, sticky="w")

            if field in ["Department", "Course", "Year", "Semester", "Gender", "College"]:
                combo = ttk.Combobox(form_frame, textvariable=var, state="readonly", width=25)

                if field == "Department":
                    combo["values"] = ("CS","CA", "IT", "Mechanical","Civil","Data Science")
                elif field == "Course":
                    combo["values"] = ("B.Tech", "B.Sc", "B.Com","M.Sc","M.Com")
                elif field == "Year":
                    combo["values"] = ("1st", "2nd", "3rd", "4th")
                elif field == "Semester":
                    combo["values"] = ("1","2","3","4","5","6","7","8")
                elif field == "Gender":
                    combo["values"] = ("Male", "Female", "Other")
                elif field == "College":
                    combo["values"] = ("Garware", "SPPU", "MIT","Symbiosis","Modern College","St.Mira","Bharati Vidyapeeth")

                combo.grid(row=row, column=1, padx=15, pady=8)
            else:
                Entry(form_frame, textvariable=var, width=27).grid(row=row, column=1, padx=15, pady=8)

            row += 1

        # ================= BUTTONS =================
        btn_frame = Frame(form_frame, bg="white")
        btn_frame.grid(row=row, column=0, columnspan=2, pady=20)

        Button(btn_frame, text="Save", command=self.add_data, width=12, bg="#2E7D32", fg="white").grid(row=0, column=0, padx=5)
        Button(btn_frame, text="Take Photo", command=self.generate_dataset, width=12, bg="#1565C0", fg="white").grid(row=1, column=0, padx=5, pady=5)
        Button(btn_frame, text="Update", command=self.update_data, width=12, bg="#00897B", fg="white").grid(row=0, column=1, padx=5)
        Button(btn_frame, text="Delete", command=self.delete_data, width=12, bg="#C62828", fg="white").grid(row=0, column=2, padx=5)
        Button(btn_frame, text="Reset", command=self.reset_data, width=12, bg="#616161", fg="white").grid(row=0, column=3, padx=5)

        # ================= RIGHT FRAME =================
        right_frame = LabelFrame(main_frame, text="Student Records",
                                font=("Calibri", 14, "bold"), bg="white")
        right_frame.pack(side=RIGHT, fill=BOTH, expand=1, padx=10)

        table_frame = Frame(right_frame)
        table_frame.pack(fill=BOTH, expand=1)

        columns = tuple(self.vars.keys())
        self.table = ttk.Treeview(table_frame, columns=columns, show="headings")

        scroll_y = Scrollbar(table_frame, orient=VERTICAL, command=self.table.yview)
        scroll_y.pack(side=RIGHT, fill=Y)
        self.table.configure(yscrollcommand=scroll_y.set)

        for col in columns:
            self.table.heading(col, text=col)
            self.table.column(col, width=120, anchor="center")

        self.table.pack(fill=BOTH, expand=1)
        self.table.bind("<ButtonRelease>", self.get_cursor)

        self.fetch_data()

    # ================= FUNCTIONS =================
    def open_main(self):
        confirm = messagebox.askyesno("Exit", "Return to Main Dashboard?")
        if confirm:
            for widget in self.root.winfo_children():
                widget.destroy()

            from main import Face_Recognition_System
            Face_Recognition_System(self.root)

    def connect(self):
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="Khagraj@5172",
            database="face_recognizer"
        )

    def add_data(self):
        if self.vars["Student ID"].get() == "" or self.vars["Name"].get() == "":
            messagebox.showerror("Error", "Student ID and Name required")
            return

        try:
            dob = datetime.strptime(self.vars["DOB"].get(), "%d/%m/%Y").strftime("%Y-%m-%d")
        except:
            messagebox.showerror("Error", "DOB must be DD/MM/YYYY")
            return

        try:
            conn = self.connect()
            cursor = conn.cursor()
            cursor.execute("""
            INSERT INTO student 
            (student_id, roll, name, section, college, dep, course, semester, year,
            phone, email, address, gender, dob)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """, (
                self.vars["Student ID"].get(),
                self.vars["Roll"].get(),
                self.vars["Name"].get(),
                self.vars["Section"].get(),
                self.vars["College"].get(),
                self.vars["Department"].get(),
                self.vars["Course"].get(),
                self.vars["Semester"].get(),
                self.vars["Year"].get(),
                self.vars["Phone"].get(),
                self.vars["Email"].get(),
                self.vars["Address"].get(),
                self.vars["Gender"].get(),
                dob
            ))
            conn.commit()
            conn.close()
            self.fetch_data()
            messagebox.showinfo("Success", "Record Added")
        except Exception as e:
            messagebox.showerror("Database Error", str(e))

    def fetch_data(self):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM student")
        rows = cursor.fetchall()

        self.table.delete(*self.table.get_children())
        for row in rows:
            self.table.insert("", END, values=row)

        conn.close()

    def get_cursor(self, event=""):
        data = self.table.item(self.table.focus())["values"]
        if data:
            for i, key in enumerate(self.vars.keys()):
                self.vars[key].set(data[i])

    def update_data(self):
        try:
            dob = datetime.strptime(self.vars["DOB"].get(), "%d/%m/%Y").strftime("%Y-%m-%d")
        except:
            messagebox.showerror("Error", "DOB must be DD/MM/YYYY")
            return

        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("""
        UPDATE student SET 
        roll=%s,name=%s,section=%s,college=%s,dep=%s,course=%s,
        semester=%s,year=%s,phone=%s,email=%s,address=%s,gender=%s,dob=%s
        WHERE student_id=%s
        """, (
            self.vars["Roll"].get(),
            self.vars["Name"].get(),
            self.vars["Section"].get(),
            self.vars["College"].get(),
            self.vars["Department"].get(),
            self.vars["Course"].get(),
            self.vars["Semester"].get(),
            self.vars["Year"].get(),
            self.vars["Phone"].get(),
            self.vars["Email"].get(),
            self.vars["Address"].get(),
            self.vars["Gender"].get(),
            dob,
            self.vars["Student ID"].get()
        ))
        conn.commit()
        conn.close()
        self.fetch_data()
        messagebox.showinfo("Success", "Record Updated")

    def delete_data(self):
        if self.vars["Student ID"].get() == "":
            messagebox.showerror("Error", "Student ID required")
            return

        confirm = messagebox.askyesno("Delete", "Delete this student?")
        if confirm:
            conn = self.connect()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM student WHERE student_id=%s", (self.vars["Student ID"].get(),))
            conn.commit()
            conn.close()
            self.fetch_data()
            messagebox.showinfo("Success", "Record Deleted")

    def reset_data(self):
        for v in self.vars.values():
            v.set("")

    def generate_dataset(self):
        if self.vars["Student ID"].get() == "" or self.vars["Name"].get() == "":
            messagebox.showerror("Error", "Student ID and Name required before taking photo")
            return

        cap = cv2.VideoCapture(0)
        img_id = 0

        if not os.path.exists("data"):
            os.makedirs("data")

        face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

        while True:
            ret, frame = cap.read()
            if not ret:
                break
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_classifier.detectMultiScale(gray, 1.3, 5)

            for (x, y, w, h) in faces:
                img_id += 1
                face = gray[y:y+h, x:x+w]
                face = cv2.resize(face, (450, 450))

                file_name = f"data/user.{self.vars['Student ID'].get()}.{img_id}.jpg"
                cv2.imwrite(file_name, face)
                cv2.imshow("Face", face)

            # Exit if ESC pressed or enough images captured
            key = cv2.waitKey(1)
            if key == 27 or img_id >= 20:   # ESC key or 20 images
                break

        cap.release()
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", f"Dataset created with {img_id} images")
   

# ================= MAIN LOOP =================
if __name__ == "__main__":
    root = Tk()
    root.state("zoomed")
    obj = Student(root)
    root.mainloop()