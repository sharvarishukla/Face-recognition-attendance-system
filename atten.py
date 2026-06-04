from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata = []

class Attendance:

    def __init__(self, root):

        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Attendance System")

        # ================== VARIABLES ==================
        self.var_atten_id = StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendance = StringVar()

        # ================= TOP IMAGE =================
        try:
            img_top = Image.open("college_images/atten.jpg")
            img_top = img_top.resize((765, 200), Image.LANCZOS)
            self.photoimg_top = ImageTk.PhotoImage(img_top)

            top_lbl = Label(self.root, image=self.photoimg_top)
            top_lbl.place(x=0, y=0, width=765, height=200)
        except:
            top_lbl = Label(self.root, text="Top Image Missing", bg="gray")
            top_lbl.place(x=0, y=0, width=765, height=200)

        # ================= SECOND IMAGE =================
        try:
            img2 = Image.open("college_images/clg.jpeg")
            img2 = img2.resize((765, 200), Image.LANCZOS)
            self.photoimg2 = ImageTk.PhotoImage(img2)

            lbl2 = Label(self.root, image=self.photoimg2)
            lbl2.place(x=765, y=0, width=765, height=200)
        except:
            lbl2 = Label(self.root, text="Second Image Missing", bg="gray")
            lbl2.place(x=765, y=0, width=765, height=200)

        # ================= BACKGROUND =================
        try:
            img3 = Image.open("college_images/solid.jpg")
            img3 = img3.resize((1530, 590), Image.LANCZOS)
            self.photoimg3 = ImageTk.PhotoImage(img3)

            bg_lbl = Label(self.root, image=self.photoimg3)
            bg_lbl.place(x=0, y=200, width=1530, height=590)
        except:
            bg_lbl = Label(self.root, bg="lightblue")
            bg_lbl.place(x=0, y=200, width=1530, height=590)

        # ================= TITLE =================
        title = Label(
            bg_lbl,
            text="Attendance Management",
            font=("Segoe UI", 35, "bold"),
            bg="#09021c",
            fg="white"
        )
        title.place(x=0, y=0, width=1530, height=50)

        # ================= MAIN FRAME =================
        main_frame = Frame(bg_lbl, bd=2, bg="white")
        main_frame.place(x=20, y=70, width=1480, height=500)

        # ================= LEFT FRAME =================
        left_frame = LabelFrame(
            main_frame,
            bd=2,
            bg="white",
            relief=RIDGE,
            text="Student Attendance",
            font=("Segoe UI", 12, "bold")
        )
        left_frame.place(x=10, y=10, width=720, height=480)

        # ================= RIGHT FRAME =================
        right_frame = LabelFrame(
            main_frame,
            bd=2,
            bg="white",
            relief=RIDGE,
            text="Attendance Details",
            font=("Segoe UI", 12, "bold")
        )
        right_frame.place(x=740, y=10, width=720, height=480)

        table_frame = Frame(right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=5, width=710, height=470)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.attendance_table = ttk.Treeview(
            table_frame,
            columns=("attendance_id", "student_id", "name", "department", "time", "date", "status"),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set
        )

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.attendance_table.xview)
        scroll_y.config(command=self.attendance_table.yview)

        self.attendance_table.heading("attendance_id", text="Attendance ID")
        self.attendance_table.heading("student_id", text="Student ID")
        self.attendance_table.heading("name", text="Name")
        self.attendance_table.heading("department", text="Department")
        self.attendance_table.heading("time", text="Time")
        self.attendance_table.heading("date", text="Date")
        self.attendance_table.heading("status", text="Status")

        self.attendance_table["show"] = "headings"

        self.attendance_table.pack(fill=BOTH, expand=1)
        self.attendance_table.bind("<ButtonRelease>", self.get_cursor)

        # ================= FORM FRAME =================
        form_frame = Frame(left_frame, bg="white")
        form_frame.place(x=0, y=140, width=700, height=320)

        Label(form_frame, text="Attendance ID:", font=("Segoe UI", 12, "bold"), bg="white").grid(row=0, column=0, padx=10, pady=10, sticky=W)
        Entry(form_frame, textvariable=self.var_atten_id, font=("Segoe UI", 12), bg="lightyellow").grid(row=0, column=1, padx=10, pady=10)

        Label(form_frame, text="Student ID:", font=("Segoe UI", 12, "bold"), bg="white").grid(row=1, column=0, padx=10, pady=10, sticky=W)
        Entry(form_frame, textvariable=self.var_atten_roll, font=("Segoe UI", 12), bg="lightyellow").grid(row=1, column=1, padx=10, pady=10)

        Label(form_frame, text="Student Name:", font=("Segoe UI", 12, "bold"), bg="white").grid(row=2, column=0, padx=10, pady=10, sticky=W)
        Entry(form_frame, textvariable=self.var_atten_name, font=("Segoe UI", 12), bg="lightyellow").grid(row=2, column=1, padx=10, pady=10)

        Label(form_frame, text="Attendance Status:", font=("Segoe UI", 12, "bold"), bg="white").grid(row=3, column=0, padx=10, pady=10, sticky=W)

        status_combo = ttk.Combobox(
            form_frame,
            textvariable=self.var_atten_attendance,
            font=("Segoe UI", 12),
            state="readonly",
            values=("Present", "Absent")
        )
        status_combo.grid(row=3, column=1, padx=10, pady=10)
        status_combo.current(0)

        # ================= BUTTONS =================
        button_frame = Frame(form_frame, bg="white")
        button_frame.grid(row=4, column=0, columnspan=2, pady=20)

        Button(button_frame,text="Import Csv",command=self.import_csv,font=("Segoe UI",12,"bold"),bg="#28a745",fg="white",width=10).grid(row=0,column=0,padx=10)

        Button(button_frame,text="Export Csv",command=self.export_csv,font=("Segoe UI",12,"bold"),bg="#007bff",fg="white",width=10).grid(row=0,column=1,padx=10)

        Button(button_frame,text="Update",command=self.update_data,font=("Segoe UI",12,"bold"),bg="#dc3545",fg="white",width=10).grid(row=0,column=2,padx=10)

        Button(button_frame,text="Reset",command=self.reset_data,font=("Segoe UI",12,"bold"),bg="#6c757d",fg="white",width=10).grid(row=0,column=3,padx=10)

        Button(button_frame,text="Exit",command=self.exit_window,font=("Segoe UI",12,"bold"),bg="black",fg="white",width=10).grid(row=0,column=4,padx=10)

    # ================= EXIT =================
    def exit_window(self):
        self.root.destroy()

    # ================= FETCH DATA =================
    def fetch_data(self, rows):
        self.attendance_table.delete(*self.attendance_table.get_children())
        for i in rows:
            self.attendance_table.insert("", END, values=i)

    # ================= IMPORT CSV =================
    def import_csv(self):
        global mydata
        mydata.clear()

        file = filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)

        if file == "":
            return

        with open(file) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for row in csvread:
                mydata.append(row)

        self.fetch_data(mydata)

    # ================= EXPORT CSV =================
    def export_csv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror("No Data","No data available to export",parent=self.root)
                return False

            file = filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Save CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)

            with open(file,mode="w",newline="") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)

            messagebox.showinfo("Data Exported","CSV exported successfully",parent=self.root)

        except Exception as e:
            messagebox.showerror("Error",f"Error : {str(e)}",parent=self.root)

    def get_cursor(self,event=""):
        cursor_row=self.attendance_table.focus()
        content=self.attendance_table.item(cursor_row)
        data=content["values"]

        if len(data)!=0:
            self.var_atten_id.set(data[0])
            self.var_atten_roll.set(data[1])
            self.var_atten_name.set(data[2])
            self.var_atten_dep.set(data[3])
            self.var_atten_time.set(data[4])
            self.var_atten_date.set(data[5])
            self.var_atten_attendance.set(data[6])

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")

    def update_data(self):
        pass


if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()