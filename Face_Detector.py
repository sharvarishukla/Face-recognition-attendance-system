from datetime import datetime
from tkinter import *
from PIL import Image, ImageTk
import mysql.connector
import cv2

class FaceDetect:

    def __init__(self, root):

        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Attendance System")

        title = Label(self.root, text="Face Detection",
                      font=("Segoe UI", 35, "bold"),
                      bg="#4a0bdd", fg="white")
        title.place(x=0, y=0, width=1530, height=45)

        # ================= EXIT BUTTON =================
        btn_exit = Button(self.root, text="EXIT",
                          font=("Segoe UI", 12, "bold"),
                          bg="#e53935", fg="white",
                          cursor="hand2",
                          command=self.open_main)
        btn_exit.place(x=1400, y=10, width=120, height=30)

        # ================= Top Image =================
        img_top = Image.open(r"C:\Users\madhu\OneDrive\Desktop\Face_Regonition _Attendance_System\college_images\face_detector1.jpg")
        img_top = img_top.resize((650, 700), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        f_lb1 = Label(self.root, image=self.photoimg_top)
        f_lb1.place(x=0, y=55, width=650, height=700)

        # ================= Bottom Image =================
        img_bottom = Image.open(r"C:\Users\madhu\OneDrive\Desktop\Face_Regonition _Attendance_System\college_images\Futuristic face recognition scan complete.png")
        img_bottom = img_bottom.resize((950, 700), Image.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        f_lb2 = Label(self.root, image=self.photoimg_bottom)
        f_lb2.place(x=650, y=55, width=950, height=700)

        # ================= Detect Button =================
        b1 = Button(f_lb2, text="DETECT FACE",
                    cursor="hand2",
                    font=("times new roman", 18, "bold"),
                    bg="dark green",
                    fg="white",
                    command=self.face_recog)
        b1.place(x=367, y=610, width=200, height=50)

        # ================= Face Cascade =================
        self.faceCascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
        )

        # ================= LBPH Model =================
        self.clf = cv2.face.LBPHFaceRecognizer_create()
        self.clf.read("classifier.xml")

    # ================= Open Main Dashboard =================
    def open_main(self):
        # Clear all widgets in current window
        for widget in self.root.winfo_children():
            widget.destroy()

        # Import main dashboard here to avoid circular import
        from main import Face_Recognition_System
        Face_Recognition_System(self.root)

    # ================= Attendance =================
    def mark_attendance(self, i, n, r, d):
        with open("attendance.csv", "a+", newline="\n") as f:
            myDataList = f.readlines()
            nameList = []

            for line in myDataList:
                entry = line.split(",")
                nameList.append(entry[0])

            if i not in nameList:
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{n},{r},{d},{dtString},{d1},Present")

    # ================= Face Recognition =================
    def draw_boundary(self, img, classifier, scaleFactor, minNeighbors, color, clf):
        gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

        for (x, y, w, h) in features:
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 3)
            id, predict = clf.predict(gray_image[y:y + h, x:x + w])
            confidence = int((100 * (1 - predict / 300)))

            # Database connection
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Khagraj@5172",
                database="face_recognizer"
            )
            my_cursor = conn.cursor()
            my_cursor.execute(
                "SELECT student_id,name,roll,dep FROM student WHERE student_id=%s",
                (id,)
            )
            result = my_cursor.fetchone()
            conn.close()

            if result:
                i, n, r, d = result
            else:
                i = n = r = d = "Unknown"

            if confidence > 60:
                cv2.putText(img, f"ID:{i}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                cv2.putText(img, f"Name:{n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                cv2.putText(img, f"Roll:{r}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                cv2.putText(img, f"Department:{d}", (x, y + h + 25), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                self.mark_attendance(i, n, r, d)
            else:
                cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 2)

        return img

    def recognize(self, img):
        img = self.draw_boundary(img, self.faceCascade, 1.1, 10, (255, 25, 255), self.clf)
        return img

    # ================= Camera =================
    def face_recog(self):
        cap = cv2.VideoCapture(0)
        ret, img = cap.read()

        if ret:
            img = self.recognize(img)
            cv2.imshow("Face Detection", img)
            cv2.waitKey(3000)

        cap.release()
        cv2.destroyAllWindows()


# ================= Run Program =================
if __name__ == "__main__":
    root = Tk()
    obj = FaceDetect(root)
    root.mainloop()