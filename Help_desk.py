from tkinter import *

class HelpDesk:
    def __init__(self, root):
        self.root = root
        self.root.title("Help Desk - Face Recognition Attendance System")
        self.root.geometry("1530x790")

        # Clear previous widgets
        for widget in self.root.winfo_children():
            widget.destroy()

        # ================= HEADER =================
        header = Frame(self.root, bg="#2c3e50", height=60)
        header.pack(fill=X)

        header.pack_propagate(False)

        title = Label(header,
                      text="FACE RECOGNITION ATTENDANCE SYSTEM - HELP DESK",
                      font=("Arial",18,"bold"),
                      bg="#2c3e50",
                      fg="white")
        title.pack(side=LEFT,padx=20)

        btn_back = Button(header,
                          text="BACK",
                          font=("Arial",11,"bold"),
                          bg="#e74c3c",
                          fg="white",
                          cursor="hand2",
                          command=self.back_dashboard)
        btn_back.pack(side=RIGHT,padx=20,pady=10)

        # ================= MAIN FRAME =================
        main_frame = Frame(self.root,bg="white")
        main_frame.pack(fill=BOTH,expand=True,padx=20,pady=20)

        heading = Label(main_frame,
                        text="Help & User Guide",
                        font=("Calibri",22,"bold"),
                        bg="white",
                        fg="#2c3e50")
        heading.pack(pady=10)

        # ================= HELP CONTENT =================
        help_content = """
            Welcome to the Help Desk of the Face Recognition Attendance System.

            This system helps automate attendance using face recognition technology.
            It reduces manual work and improves accuracy.

            ==================== MODULES ====================

            1. Student Details
            • Add new student information
            • Update existing records
            • Delete student data
            • Capture face dataset

            2. Train Data
            • Train the system with captured images
            • Creates a recognition model

            3. Face Recognition
            • Detects faces using webcam
            • Matches faces with trained dataset
            • Marks attendance automatically

            4. Attendance
            • Displays attendance records
            • Stores date and time

            ==================== HOW TO USE ====================

            Step 1 : Add student details in the Student module.

            Step 2 : Capture student face images using "Take Photo".

            Step 3 : Train the system using the Train Data module.

            Step 4 : Start Face Recognition to mark attendance.

            ==================== TECHNOLOGIES ====================

            • Python Programming
            • OpenCV Computer Vision
            • Tkinter GUI
            • MySQL Database
            • Haar Cascade Face Detection

            ==================== SUPPORT ====================

            Developer : Madhura Deshmukh
            Project   : Face Recognition Attendance System
            Email     : madhurad2005@gmail.com
            """

        # ================= TEXT AREA =================
        text_frame = Frame(main_frame)
        text_frame.pack(fill=BOTH,expand=True)

        scroll = Scrollbar(text_frame)
        scroll.pack(side=RIGHT,fill=Y)

        help_textbox = Text(text_frame,
                            font=("Calibri",13),
                            wrap=WORD,
                            yscrollcommand=scroll.set,
                            bg="#f5f5f5")

        help_textbox.insert(END,help_content)
        help_textbox.config(state=DISABLED)

        help_textbox.pack(fill=BOTH,expand=True)

        scroll.config(command=help_textbox.yview)

    # ================= BACK FUNCTION =================
    def back_dashboard(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        from main import Face_Recognition_System
        Face_Recognition_System(self.root)