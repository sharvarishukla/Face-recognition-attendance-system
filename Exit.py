from tkinter import *
from tkinter import messagebox

class Exit:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition Attendance System")
        self.root.geometry("1530x790")

        # Clear previous widgets
        for widget in self.root.winfo_children():
            widget.destroy()

        # ================= HEADER =================
        header = Frame(self.root, bg="#1e1e2f", height=60)
        header.pack(fill=X)

        title = Label(header,
                      text="FACE RECOGNITION ATTENDANCE SYSTEM - DASHBOARD",
                      font=("Segoe UI",18,"bold"),
                      bg="#1e1e2f",
                      fg="white")
        title.pack(side=LEFT, padx=20)

        # EXIT BUTTON
        btn_exit = Button(header,
                          text="EXIT",
                          font=("Segoe UI",10,"bold"),
                          bg="#e53935",
                          fg="white",
                          cursor="hand2",
                          command=self.exit_system)
        btn_exit.pack(side=RIGHT, padx=20, pady=10)

        # ================= MAIN FRAME =================
        main_frame = Frame(self.root, bg="white")
        main_frame.pack(fill=BOTH, expand=True)

        label = Label(main_frame,
                      text="Welcome to Face Recognition Attendance System",
                      font=("Arial",24,"bold"),
                      bg="white")
        label.pack(pady=200)

    # ================= EXIT FUNCTION =================
    def exit_system(self):
        confirm = messagebox.askyesno("Exit", "Are you sure you want to exit?")
        if confirm:
            self.root.destroy()


# ================= MAIN PROGRAM =================
if __name__ == "__main__":
    root = Tk()
    root.state("zoomed")
    app = Exit(root)
    root.mainloop()
