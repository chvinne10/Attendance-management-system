import tkinter as tk
from tkinter import *
import tkinter.font as tkFont
from tkinter import ttk #contains some specail tool kit
from PIL import  Image,ImageTk
from student_attandence import Student
from face import Login
from register import register
import os


class Face:
    def __init__(self,root):#slef size coversion we need not change it size
        self.root=root
        self.root.geometry("1270x640+0+0")
        self.root.title("Face recognation system") 
        
        #back ground image
        img=Image.open(r"C:\Users\DELL\Desktop\programmig\python\background.jpg")
        self.photoimg=ImageTk.PhotoImage(img)
        
        bg=Label(self.root,image=self.photoimg)
        bg.place(x=0,y=0,width=1270,height=640)
    
        font = tkFont.Font(family="Comic Sans MS", size=40)
        label = tk.Label(root, text="                 Face Recognition Attendance System                 ",fg="white",bg="black", font=font)
        label.pack()
        
        
        #button1 registion
        img2=Image.open(r"C:\Users\DELL\Desktop\programmig\python\img\registration.jpg")
        img2=img2.resize((150,150))
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        button=Button(self.root,image=self.photoimg2,command=self.register)
        button.place(x=100,y=200)
        
        button=Button(self.root,text="registration",bg="blue",fg="white",padx=43,command=self.register)
        button.place(x=100,y=355)
        
        #button2 student
        img3=Image.open(r"C:\Users\DELL\Pictures\Screenshots\Screenshot 2024-05-13 095008.png")
        img3=img3.resize((150,150))
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        button=Button(self.root,image=self.photoimg3,command=self.student)
        button.place(x=350,y=200)
        button=Button(self.root,text="student details",command=self.student,bg="blue",fg="white",padx=38)
        button.place(x=350,y=355)

       
        #button4  face recogination attendance
        img4=Image.open(r"C:\Users\DELL\Desktop\programmig\python\img\download.jpeg")
        img4=img4.resize((150,150))
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        button=Button(self.root,image=self.photoimg4,command=self.Login)
        button.place(x=600,y=200)
        button=Button(self.root,text="Face Detection",command=self.Login,bg="blue",fg="white",padx=36)
        button.place(x=600,y=355)
        
        img5 = Image.open(r"C:\Users\DELL\Pictures\Screenshots\Screenshot 2024-05-13 094930.png")
        img5 = img5.resize((150, 150))
        self.photoimg5 = ImageTk.PhotoImage(img5)

        button = Button(self.root, image=self.photoimg5, command=self.open_attendance_file)
        button.place(x=850, y=200)
        button = Button(self.root, text="Attendance", command=self.open_attendance_file, bg="blue", fg="white", padx=40)
        button.place(x=850, y=355)

    #************fuction button*************#
    def open_attendance_file(self):
        file_path = r"C:\Users\DELL\Desktop\programmig\python\attendance.csv"
        if os.path.exists(file_path):
            os.startfile(file_path)  
        else:
            print("File not found")
        
    def student(self):
        self.new=Toplevel(self.root)
        self.app=Student(self.new) 
    
    def Login(self):
        self.new=Toplevel(self.root)
        self.app=Login(self.new)
    
    def register(self):
        self.new=Toplevel(self.root)
        self.app=register(self.new)
  

if __name__ == "__main__":
    root=Tk()
    obj=Face(root)
    root.mainloop()
    
    