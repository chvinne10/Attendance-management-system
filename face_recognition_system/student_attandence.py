from tkinter import *
from tkinter import ttk #contains some specail tool kit
from PIL import  Image,ImageTk
from tkinter import messagebox
import mysql.connector

class Student:
    def __init__(self,root):#slef size coversion we need not change it size
        self.root=root
        self.root.geometry("1270x640+0+0")
        self.root.title("student") 
        
        #****************variable**************#
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_studentname=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_email=StringVar()
        self.var_phoneno=StringVar()
        self.var_address=StringVar()
        self.var_dob=StringVar()
        self.var_studentid=StringVar()
        self.var_radio=StringVar()
        #back ground image
        img=Image.open(r"c:\Users\chvin\Pictures\Screenshot_2025-02-12-11-39-09-789_com.google.android.youtube.jpg")
        self.photoimg=ImageTk.PhotoImage(img)
        
        bg=Label(self.root,image=self.photoimg)
        bg.place(x=0,y=0,width=1270,height=640)
        
        title=Label(bg,text="   STUDENT DETAILS   ",font=("time new roman",35,"bold"),bg="white",fg="green")
        title.place(x=350,y=0)
        
        main_frame=Frame(bg,bd=4)
        main_frame.place(x=10,y=70,width=1250,height=550)
        
        #left side lable frame
        Left_frame=LabelFrame(main_frame,bd=4,bg="white",relief=RIDGE,text="Student Details",fg="green",font=("time new roman",12,"bold"))
        Left_frame.place(x=10,y=70,width=570,height=450)
        
        
        #current course infromation
        current_frame=LabelFrame(main_frame,bd=4,bg="white",relief=RIDGE,text="Current Course",font=("time new roman",12,"bold"))
        current_frame.place(x=10,y=100,width=570,height=150)
        #department
        dep_lable=Label(current_frame,text="Department",font=("time new roman",12,"bold"),fg="blue")
        dep_lable.grid(row=0,column=0)
        
        dep_combobox=ttk.Combobox(current_frame,textvariable=self.var_dep,font=("time new roman",12,"bold"),width=17,state="read only")
        dep_combobox["values"]=("select depatment","Computer","Civil","Mechaical","Electronics")
        dep_combobox.current(0)#window select with department
        dep_combobox.grid(row=0,column=1,padx=8,pady=2)
        
        #course
        course_lable=Label(current_frame,text="Course",font=("time new roman",12,"bold"),fg="blue")
        course_lable.grid(row=0,column=2,sticky=W)
        
        course_combobox=ttk.Combobox(current_frame,textvariable=self.var_course,font=("time new roman",12,"bold"),width=17,state="read only")
        course_combobox["values"]=("select course","CSE","CSM","ECE","EEE","CS","SE","BE","CE")
        course_combobox.current(0)#window select with department
        course_combobox.grid(row=0,column=3,padx=4,pady=8,sticky=W)
        
        #year
        year_lable=Label(current_frame,text="year",font=("time new roman",12,"bold"),fg="blue")
        year_lable.grid(row=1,column=0,sticky=W)
        
        year_combobox=ttk.Combobox(current_frame,textvariable=self.var_year,font=("time new roman",12,"bold"),width=17,state="read only")
        year_combobox["values"]=("select year","2022-23","2023-24","2024-25","2024-25")
        year_combobox.current(0)#window select with department
        year_combobox.grid(row=1,column=1,padx=4,pady=2,sticky=W)
        
        #semester
        semeseter_lable=Label(current_frame,text="semester",font=("time new roman",12,"bold"),fg="blue")
        semeseter_lable.grid(row=1,column=2,sticky=W)
        
        semeseter_combobox=ttk.Combobox(current_frame,textvariable=self.var_sem,font=("time new roman",12,"bold"),width=17,state="read only")
        semeseter_combobox["values"]=("select semester","I","II","III","IV")
        semeseter_combobox.current(0)#window select with department
        semeseter_combobox.grid(row=1,column=3,padx=4,pady=2,sticky=W)
        
        
        #class student information
        student_frame=LabelFrame(main_frame,bd=4,bg="white",relief=RIDGE,text="class student",font=("time new roman",12,"bold"))
        student_frame.place(x=10,y=250,width=570,height=250)
        
        #studentid
        studentid_lable=Label(student_frame,text="StudentId:-",font=("time new roman",12,"bold"),fg="blue")
        studentid_lable.grid(row=0,column=0,padx=10,sticky=W)
        Student_Entry=ttk.Entry(student_frame,textvariable=self.var_studentid,width=20).grid(row=0,column=1,padx=10,sticky=W)
        
        #student name
       
        
        student_lable=Label(student_frame,text="Studentname:-",font=("time new roman",12,"bold"),fg="blue")
        student_lable.grid(row=0,column=2,padx=10,sticky=W)
        Student_Entry=ttk.Entry(student_frame,textvariable=self.var_studentname,width=20).grid(row=0,column=3,padx=10,sticky=W)
        
        #section no
        
        
        section_lable=Label(student_frame,text="section:-",font=("time new roman",12,"bold"),fg="blue")
        section_lable.grid(row=1,column=0,padx=10,sticky=W)
        
        
        section_combobox=ttk.Combobox(student_frame,textvariable=self.var_roll,font=("time new roman",12,"bold"),width=12,state="read only")
        section_combobox["values"]=("select section","A","B","C","D")
        section_combobox.current(0)#window select with department
        section_combobox.grid(row=1,column=1,padx=2,pady=2,sticky=W)
        
        #gender

        
        gender_lable=Label(student_frame,text="gender:-",font=("time new roman",12,"bold"),fg="blue")
        gender_lable.grid(row=1,column=2,padx=10,sticky=W)
        
        gender_combobox=ttk.Combobox(student_frame,textvariable=self.var_gender,font=("time new roman",12,"bold"),width=12,state="read only")
        gender_combobox["values"]=("select gender","male","female","others")
        gender_combobox.current(0)#window select with department
        gender_combobox.grid(row=1,column=3,padx=10,pady=2,sticky=W)
        #DOB
      
        
        dob_lable=Label(student_frame,text="DOB:-",font=("time new roman",12,"bold"),fg="blue")
        dob_lable.grid(row=2,column=0,padx=10,sticky=W)
        dob_Entry=ttk.Entry(student_frame,textvariable=self.var_dob,width=20).grid(row=2,column=1,padx=10,sticky=W)
        
        #email
     
        
        email_lable=Label(student_frame,text="Email:-",font=("time new roman",12,"bold"),fg="blue")
        email_lable.grid(row=2,column=2,padx=10,sticky=W)
        email_Entry=ttk.Entry(student_frame,textvariable=self.var_email,width=20).grid(row=2,column=3,padx=10,sticky=W)
        
        #phone no
       
        
        phoneno_lable=Label(student_frame,text="Phone no:-",font=("time new roman",12,"bold"),fg="blue")
        phoneno_lable.grid(row=3,column=0,padx=10,sticky=W)
        phoneno_Entry=ttk.Entry(student_frame,textvariable=self.var_phoneno,width=20).grid(row=3,column=1,padx=10,sticky=W)
        
        #address
        
        address_lable=Label(student_frame,text="Address:-",font=("time new roman",12,"bold"),fg="blue")
        address_lable.grid(row=3,column=2,padx=10,sticky=W)
        address_Entry=ttk.Entry(student_frame,textvariable=self.var_address,width=20).grid(row=3,column=3,padx=10,sticky=W)
        
    
        #radio
        radio=ttk.Radiobutton(student_frame,text="no photo sample",value="NO",textvariable=self.var_radio)
        radio.grid(row=4,column=0)
        
        radio1=ttk.Radiobutton(student_frame,text="photo sample",value="YES",textvariable=self.var_radio)
        radio1.grid(row=4,column=2)
    
        #buttonframe
        butframe=Frame(student_frame,bd=4,relief=RIDGE,bg="white")
        butframe.place(x=1,y=140,width=570,height=160)
        
        button1=Button(butframe,text="save",command=self.add_data,width=17,font=("time new roman",12,"bold"),fg="blue")
        button1.grid(row=0,column=0)
        
        button2=Button(butframe,text="update",width=17,command=self.update_data,font=("time new roman",12,"bold"),fg="blue")
        button2.grid(row=0,column=1)
        
        button3=Button(butframe,text="Delete",width=17,command=self.delete_data,font=("time new roman",12,"bold"),fg="blue")
        button3.grid(row=0,column=2)
 
        
        
        #rght side lable frame
        Right_frame=LabelFrame(main_frame,bd=4,bg="white",relief=RIDGE,text="student details",font=("time new roman",12,"bold"),fg="green")
        Right_frame.place(x=640,y=70,width=560,height=450)
        
        #search system
        search_system_frame=LabelFrame(main_frame,bd=4,bg="white",relief=RIDGE,text="search system",font=("time new roman",12,"bold"))
        search_system_frame.place(x=640,y=90,width=555,height=400)
         
        search_lable=Label(search_system_frame,text="search by:-",font=("time new roman",12,"bold"),fg="blue",bg="red")
        search_lable.grid(row=0,column=0,padx=10,sticky=W)
      
        
        # ***********table******************#
        table_frame=Frame(search_system_frame,bd=4,relief=RIDGE,bg="white")
        table_frame.place(x=2,y=50,width=556,height=325)
        
        scroll_tk_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_tk_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(table_frame,column=("dept","course","year","semester","studentid","student name","section no","gender","dob","email","phone no","address","photoimage"),xscrollcommand=scroll_tk_x.set,yscrollcommand=scroll_tk_y.set)
        scroll_tk_x.pack(side=BOTTOM,fill=X)
        scroll_tk_y.pack(side=RIGHT,fill=Y)
        scroll_tk_x.config(command=self.student_table.xview)
        scroll_tk_y.config(command=self.student_table.yview)
        self.student_table.heading("dept",text="department")
        self.student_table.heading("course",text="course")
        self.student_table.heading("year",text="year")
        self.student_table.heading("semester",text="semester")
        self.student_table.heading("studentid",text="studentid")
        self.student_table.heading("student name",text="student name")
        self.student_table.heading("section no",text="section no")
        self.student_table.heading("gender",text="gender")
        self.student_table.heading("dob",text="dob")
        self.student_table.heading("email",text="email")
        self.student_table.heading("phone no",text="phone no")
        self.student_table.heading("address",text="address")
        self.student_table.heading("photoimage",text="photoimage")
        
        self.student_table["show"]="headings"
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    #******************funtion****************************
    
    def add_data(self):
        if self.var_dep.get()=="select department" or self.var_studentname.get()=="" or self.var_roll.get()=="":
            messagebox.showerror("ERROR","ALL will blank will be filled",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="projectpython")
                my_cusor=conn.cursor()
                my_cusor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                    self.var_dep.get(),
                                                                                                    self.var_course.get(),
                                                                                                    self.var_year.get(),
                                                                                                    self.var_sem.get(),
                                                                                                    self.var_studentid.get(),
                                                                                                    self.var_studentname.get(),
                                                                                                    self.var_roll.get(),
                                                                                                    self.var_gender.get(),
                                                                                                    self.var_dob.get(),
                                                                                                    self.var_email.get(),
                                                                                                    self.var_phoneno.get(),
                                                                                                    self.var_address.get(),
                                                                                                    self.var_radio.get()
                                                                                                    
                                                                                                  
                                                                                                    
                                                                                                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("sucsesss","student details added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("error","due to:{str(es)}",parent=self.root)
                
                #+++++++++++++fech data+++++++++#
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="projectpython")
        my_cusor=conn.cursor()
        my_cusor.execute("select * from student")
        data=my_cusor.fetchall()
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    #get cursor
    
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_sem.set(data[3]),
        self.var_studentid.set(data[4]),
        self.var_studentname.set(data[5]),
        self.var_roll.set(data[6]),
        self.var_gender.set(data[7]),
        self.var_dob.set(data[8]),
        self.var_email.set(data[9]),
        self.var_phoneno.set(data[10]),
        self.var_address.set(data[11]),
        self.var_radio.set(data[12])
#++++++++++++++update++++++++++
    def update_data(self):
        if self.var_dep.get()=="select department" or self.var_studentname.get()=="" or self.var_roll.get()=="":
            messagebox.showerror("ERROR","ALL will blank will be filled",parent=self.root)
        else:
            try:
                update=messagebox.askyesno("update","do u want to update",parent=self.root)
                if update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="projectpython")
                    my_cusor=conn.cursor()
                    my_cusor.execute("update student set dep=%s,course=%s,year=%s,sem=%s,studentname=%s,roll=%s,gender=%s,dob=%s,email=%s,phoneno=%s,address=%s,takephoto=%s where studentid=%s",(
                                                                                                                                                                                    self.var_dep.get(),
                                                                                                                                                                                    self.var_course.get(),
                                                                                                                                                                                    self.var_year.get(),
                                                                                                                                                                                    self.var_sem.get(),
                                                                                                                                                                                    self.var_studentname.get(),
                                                                                                                                                                                    self.var_roll.get(), 
                                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                                    self.var_phoneno.get(),
                                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                                    self.var_radio.get(),
                                                                                                                                                                                    self.var_studentid.get()
                                                                                                                                                                               ))
            
                else: 
                    if not update:
                        return
                messagebox.showinfo("sucess","student details are added",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("error","due to:{str=}",parent=self.root)    
    #delete function+++++++++++
    def delete_data(self):
        if self.var_roll.get()=="":
            messagebox.showerror("error","roll number is mandatary",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("student delete page","do u need to delete",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="projectpython")
                    my_cusor=conn.cursor()
                    sql="delete from student where studentid=%s"
                    val=(self.var_studentid.get(),)
                    my_cusor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("delete","succusfully deleted student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("error","due to:{str=}",parent=self.root) 
                
                
 
                
                    
        
            
    




if __name__ == "__main__":
        root=Tk()
        obj1=Student(root)
        root.mainloop()