from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
import bcrypt
from main import Face_Recognition_System  # ✅ keep this


class Login:
    def __init__(self, root):
        self.root = root
        self.root.state("zoomed")
        self.root.title("Login System")

        # ================= DATABASE =================
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Khagraj@5172",
            database="login_system"
        )
        self.cursor = self.conn.cursor()

        # ================= BACKGROUND =================
        bg = Image.open(r"C:\Users\madhu\OneDrive\Desktop\Face_Regonition _Attendance_System\college_images\bg.jpg")
        bg = bg.resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()), Image.LANCZOS)
        self.bg = ImageTk.PhotoImage(bg)
        Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        # ================= VARIABLES =================
        self.username = StringVar()
        self.password = StringVar()

        # ================= LOGIN FRAME =================
        self.frame = Frame(self.root, bg="white", bd=3, relief=RIDGE)
        self.frame.place(relx=0.5, rely=0.5, anchor=CENTER, width=400, height=450)

        Label(self.frame, text="🔑 Login", font=("Segoe UI", 22, "bold"), bg="white", fg="#333").pack(pady=20)

        Label(self.frame, text="👤 Username", font=("Segoe UI", 12, "bold"), bg="white", fg="#333").pack(pady=(10,0))
        Entry(self.frame, textvariable=self.username, font=("Segoe UI", 12), bg="#f0f0f0", relief=FLAT).pack(pady=10, ipady=5, ipadx=5)

        Label(self.frame, text="🔒 Password", font=("Segoe UI", 12, "bold"), bg="white", fg="#333").pack(pady=(10,0))
        Entry(self.frame, textvariable=self.password, font=("Segoe UI", 12), bg="#f0f0f0", relief=FLAT, show="*").pack(pady=10, ipady=5, ipadx=5)

        # Buttons
        self.btn_login = Button(self.frame, text="➡️ Login", font=("Segoe UI", 12, "bold"), bg="#007bff", fg="white",
                                activebackground="#0056b3", activeforeground="white", command=self.login)
        self.btn_login.pack(pady=10, ipadx=10, ipady=5)
        self.btn_login.bind("<Enter>", lambda e: self.btn_login.config(bg="#0056b3"))
        self.btn_login.bind("<Leave>", lambda e: self.btn_login.config(bg="#007bff"))

        self.btn_register = Button(self.frame, text="📝 Register", font=("Segoe UI", 12, "bold"), bg="#28a745", fg="white",
                                activebackground="#1e7e34", activeforeground="white", command=self.register_window)
        self.btn_register.pack(pady=10, ipadx=10, ipady=5)
        self.btn_register.bind("<Enter>", lambda e: self.btn_register.config(bg="#1e7e34"))
        self.btn_register.bind("<Leave>", lambda e: self.btn_register.config(bg="#28a745"))

        Button(self.frame, text="❓ Forgot Password", font=("Segoe UI", 10, "bold"), fg="red", bd=0,
            command=self.forgot_password_window).pack(pady=5)

        # Logout button
        self.btn_logout = Button(self.root, text="Logout",
                                font=("Segoe UI", 12, "bold"),
                                bg="red", fg="white",
                                activebackground="#b30000", activeforeground="white",
                                command=self.logout)
        self.btn_logout.place(x=10, y=10)

    # ================= LOGOUT =================
    def logout(self):
        self.root.destroy()
        root = Tk()
        app = Login(root)
        root.mainloop()

    # ================= LOGIN =================
    
    def login(self):
        user = self.username.get().strip()
        pwd = self.password.get().strip()

        if user == "" or pwd == "":
            messagebox.showerror("Error", "Please fill all fields ❌")
            return

        self.cursor.execute("SELECT password FROM users WHERE username=%s", (user,))
        row = self.cursor.fetchone()

        if row and bcrypt.checkpw(pwd.encode(), row[0].encode()):
            # ✅ LOAD FACE_RECOGNITION ON SAME WINDOW

            # Destroy login frame
            self.frame.destroy()
            self.btn_logout.destroy()  # optional

            # Load Face Recognition System in same window
            self.face_system = Face_Recognition_System(self.root)

        else:
            messagebox.showerror("Error", "Invalid Username or Password ❌")

    # ================= REGISTER =================
    def register_window(self):
        win = Toplevel(self.root)
        win.title("Register")
        win.geometry("400x300")

        new_user = StringVar()
        new_pass = StringVar()

        Label(win, text="📝 Register New User", font=("Arial", 15, "bold")).pack(pady=20)
        Label(win, text="👤 Username").pack(pady=(10,0))
        Entry(win, textvariable=new_user, bg="#dbeede").pack(pady=5, ipady=5, ipadx=5)
        Label(win, text="🔒 Password").pack(pady=(10,0))
        Entry(win, textvariable=new_pass, show="*", bg="#def8e6").pack(pady=5, ipady=5, ipadx=5)

        def register():
            u = new_user.get().strip()
            p = new_pass.get().strip()
            if u == "" or p == "":
                messagebox.showerror("Error", "All fields required")
                return

            hashed = bcrypt.hashpw(p.encode(), bcrypt.gensalt()).decode()

            try:
                self.cursor.execute(
                    "INSERT INTO users (username, password) VALUES (%s, %s)",
                    (u, hashed)
                )
                self.conn.commit()
                messagebox.showinfo("Success", "Registered Successfully ✅")
                win.destroy()
            except mysql.connector.IntegrityError:
                messagebox.showerror("Error", "User already exists ❌")

        Button(win, text="Register", bg="#28a745", fg="white", command=register).pack(pady=10, ipadx=10, ipady=5)

    # ================= FORGOT PASSWORD =================
    def forgot_password_window(self):
        win = Toplevel(self.root)
        win.title("Forgot Password")
        win.geometry("400x300")

        user_var = StringVar()
        new_pass_var = StringVar()

        Label(win, text="❓ Forgot Password", font=("Arial", 15, "bold")).pack(pady=10)
        Label(win, text="👤 Enter Username").pack(pady=5)
        Entry(win, textvariable=user_var, bg="#f0f0f0").pack(pady=5, ipady=5, ipadx=5)

        Label(win, text="🔒 Enter New Password").pack(pady=5)
        Entry(win, textvariable=new_pass_var, show="*", bg="#f0f0f0").pack(pady=5, ipady=5, ipadx=5)

        def reset_password():
            u = user_var.get().strip()
            p = new_pass_var.get().strip()
            if u == "" or p == "":
                messagebox.showerror("Error", "All fields required", parent=win)
                return

            self.cursor.execute("SELECT * FROM users WHERE username=%s", (u,))
            row = self.cursor.fetchone()
            if not row:
                messagebox.showerror("Error", "User not found", parent=win)
                return

            hashed = bcrypt.hashpw(p.encode(), bcrypt.gensalt()).decode()
            self.cursor.execute("UPDATE users SET password=%s WHERE username=%s", (hashed, u))
            self.conn.commit()
            messagebox.showinfo("Success", "Password reset successfully ✅", parent=win)
            win.destroy()

        Button(win, text="Reset Password", bg="#ffc107", fg="black", command=reset_password).pack(pady=10, ipadx=10, ipady=5)


# ================= MAIN =================
if __name__ == "__main__":
    root = Tk()
    app = Login(root)
    root.mainloop()