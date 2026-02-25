import tkinter as tk
from tkinter import *
import tkinter.font as tkFont
import cv2
from PIL import Image, ImageTk
import os
from tkinter import messagebox
import face_recognition

class register:
    def __init__(self, root1):
        self.root1 = root1
        self.root1.geometry("1270x850+0+0")
        font = tkFont.Font(family="Comic Sans MS", size=10)

        
        self.name_label = Label(self.root1, text="Name:", font=("Comic Sans MS", 12))
        self.name_label.place(x=600, y=250)
        self.name_entry = Entry(self.root1, font=("Comic Sans MS", 12))
        self.name_entry.place(x=700, y=250, width=200)

        button = Button(self.root1, text="REGISTER", cursor="hand2", bg="green", fg="white", padx=43, pady=10, font=font, command=self.register_action)
        button.place(x=750, y=355)

        self.video_label = Label(self.root1)
        self.video_label.place(x=10, y=70, width=550, height=550)
        self.video_capture = cv2.VideoCapture(0)
        self.update_video()

    def update_video(self):
        ret, frame = self.video_capture.read()
        if ret:
            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(cv2image)
            imgtk = ImageTk.PhotoImage(image=img)
            self.video_label.imgtk = imgtk
            self.video_label.configure(image=imgtk)
            self.root1.after(10, self.update_video)

    def register_action(self):
        name = self.name_entry.get()
        if not name:
            messagebox.showwarning("Input Error", "Please enter your name")
            return

        ret, frame = self.video_capture.read()
        if ret:
            new_face_encoding = face_recognition.face_encodings(frame)
            if new_face_encoding:
                new_face_encoding = new_face_encoding[0]
                for file_name in os.listdir("photos"):
                    if file_name.endswith(".jpg"):
                        known_image = face_recognition.load_image_file(f"photos/{file_name}")
                        known_face_encoding = face_recognition.face_encodings(known_image)
                        if known_face_encoding:
                            known_face_encoding = known_face_encoding[0]
                            matches = face_recognition.compare_faces([known_face_encoding], new_face_encoding)
                            if True in matches:
                                messagebox.showinfo("Already Registered", "This face is already registered")
                                return
                cv2.imwrite(f"photos/{name}.jpg", frame)
                messagebox.showinfo("Success", f"Registered with Name: {name}")
                print("Photo saved")
            else:
                messagebox.showwarning("Face Not Found", "No face detected. Please try again.")

if __name__ == "__main__":
    if not os.path.exists("photos"):
        os.makedirs("photos")

    root1 = Tk()
    obj = register(root1)
    root1.mainloop()
