Face Recognition Attendance System

A smart and automated attendance management system that uses Computer Vision and Machine Learning to recognize faces in real-time and automatically mark attendance. This project eliminates manual attendance processes, reduces human errors, and prevents proxy attendance through biometric facial recognition.

📌 Project Overview

Traditional attendance systems are time-consuming and vulnerable to fraudulent practices such as proxy attendance. This project provides an intelligent solution that captures facial images through a webcam, recognizes registered users, and automatically records attendance with date and time stamps.

The system is designed for:

Educational Institutions
Corporate Offices
Training Centers
Organizations requiring automated attendance management





✨ Features

🔹 Face Detection

Detects human faces in real-time using OpenCV Haar Cascade classifiers.

🔹 Face Recognition

Recognizes registered users using the LBPH (Local Binary Pattern Histogram) algorithm.

🔹 Automatic Attendance Marking

Marks attendance automatically after successful face recognition.

🔹 Real-Time Processing

Processes webcam video streams instantly for quick attendance recording.

🔹 Secure Login System

Uses password hashing with bcrypt to protect user credentials.

🔹 Student Management

Add, update, delete, and manage student records through a user-friendly interface.

🔹 Attendance Management

Stores attendance records with:

Student ID
Student Name
Date
Time
Attendance Status



🔹 CSV Export

Attendance records are saved in CSV format for easy reporting and analysis.

🔹 User-Friendly GUI

Built using Tkinter with an intuitive dashboard and management panels.





🛠️ Technology Stack

| Technology       | Purpose                                 |
| ---------------- | --------------------------------------- |
| Python           | Core Programming Language               |
| OpenCV           | Face Detection & Recognition            |
| NumPy            | Image Processing & Numerical Operations |
| Tkinter          | GUI Development                         |
| Pillow (PIL)     | Image Handling                          |
| MySQL            | Student & User Data Storage             |
| MySQL Connector  | Database Connectivity                   |
| Passlib (bcrypt) | Password Hashing & Security             |







🏗️ System Architecture

Workflow


Register Student

Capture Face Images

Train Recognition Model

Detect Face using Webcam

Recognize Registered User

Mark Attendance Automatically

Store Attendance Records


The trained facial recognition model is stored and reused for future attendance sessions.






🚀 Installation


1. Clone Repository
git clone https://github.com/your-username/Face-Recognition-Attendance-System.git
cd Face-Recognition-Attendance-System

2. Create Virtual Environment
python -m venv venv

3. Activate Environment
Windows
venv\Scripts\activate
Linux/Mac
source venv/bin/activate

4. Install Dependencies
pip install -r requirements.txt

Or manually install:

pip install opencv-python
pip install numpy
pip install pillow
pip install mysql-connector-python
pip install passlib



⚙️ Database Setup

Install MySQL Server.

Create a database:

CREATE DATABASE face_attendance;

Update database credentials in the project configuration file.

host="localhost"
user="root"
password="your_password"
database="face_attendance"

Run the application.






▶️ How to Run

Start the Application

python main.py

Usage Steps

Step 1: Register User
Create an account.
Login securely.

Step 2: Add Student Details
Enter student information.
Save to database.

Step 3: Capture Face Dataset
Capture multiple facial images.

Step 4: Train Model
python train.py

Step 5: Start Face Recognition
python face_recognition.py

Step 6: Automatic Attendance
Attendance gets recorded automatically.

Records are stored in CSV files and database.




🔒 Security Features

Password Hashing using bcrypt

User Authentication System

Secure Database Storage

Prevention of Proxy Attendance

Contactless Attendance Process





📊 Advantages

✅ Eliminates manual attendance

✅ Saves time and effort

✅ Prevents proxy attendance

✅ Improves accuracy

✅ Real-time attendance tracking

✅ Easy record management

✅ Cost-effective implementation

✅ Contactless and hygienic solution





🔮 Future Enhancements

Deep Learning (CNN-based Face Recognition)

Liveness Detection

Mask Detection

Mobile Application Support

Cloud Database Integration

Multi-Face Recognition

SMS & Email Notification
