import Framework
import tkinter
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from PIL import Image,ImageTk

def Closing():
    if messagebox.askokcancel("Quit", "You are about to Quit Student Mark Analysis Application"):
        Obj=Framework.Update()
        SMA.destroy()
        
SMA=Tk()
SMA.title("Student Mark Analysis")
SMA.configure(background="white")
SMA.state("zoomed")
SMA.protocol("WM_DELETE_WINDOW", Closing)
SMA.resizable(False, False)

global Stu_Obj
global CT_Obj
global ST_Obj
global _Name
global User

Home=tkinter.Frame(SMA)
Home.pack(fill=BOTH, expand=True)

def Next():
    Home.forget()
    Obj=Page1()

Home.configure(background="white")
Home.columnconfigure(0, weight=1)
Home.columnconfigure(1, weight=1)
Home.columnconfigure(2, weight=1)

School_Logo=PhotoImage(file="School_Logo.png")
Logo=Label(Home, image = School_Logo, relief="solid")

Text1=Label(Home, text="Student Mark Analysis of Class - XII", font=("Verdana", 20), background="white")
Text2=Label(Home, text="Done By :", font=("Verdana", 20), background="white")

Arvin=Image.open("Arvin.png")
Ezhil=Image.open("Ezhil.png")
Kingston=Image.open("Kingston.png")

Arvin_Resize=Arvin.resize((150, 180), Image.ANTIALIAS)
Ezhil_Resize=Ezhil.resize((150, 180), Image.ANTIALIAS)
Kingston_Resize=Kingston.resize((150, 180), Image.ANTIALIAS)

Arvin=ImageTk.PhotoImage(Arvin_Resize)
Ezhil=ImageTk.PhotoImage(Ezhil_Resize)
Kingston=ImageTk.PhotoImage(Kingston_Resize)

Pic1=Label(Home, image = Arvin, relief="flat")
Pic2=Label(Home, image = Ezhil, relief="flat")
Pic3=Label(Home, image = Kingston, relief="flat")

Name1=Label(Home, text="Arvin Samuel A.", font=("Verdana", 10), background="white")
Name2=Label(Home, text="Ezhil Adhithya P.", font=("Verdana", 10), background="white")
Name3=Label(Home, text="Kingston Richard J.", font=("Verdana", 10), background="white")

Text=Label(Home, text="Click Here to Login", font=("Verdana", 18), background="white")
style=Style()
style.configure("Home.TButton", font=("Verdana", 15))

Login=Button(Home, text="Login", command=Next, style="Home.TButton")

Logo.grid(column=0, row=0, columnspan=4)
Text1.grid(column=0, row=1, columnspan=4, pady=10)
Text2.grid(column=0, row=2, columnspan=4, pady=10)
Pic1.grid(column=0, row=3, pady=10)
Pic2.grid(column=1, row=3, pady=10)
Pic3.grid(column=2, row=3, pady=10)

Name1.grid(column=0, row=4, pady=20)
Name2.grid(column=1, row=4, pady=20)
Name3.grid(column=2, row=4, pady=20)

Text.grid(column=0, row=5, columnspan=4, pady=10)
Login.grid(column=0, row=6, columnspan=4, pady=10)

class Menu_Bar:
    def __init__(self, Menu):
        SMA.config(menu=Menu)
        
class Page1:
    def __init__(self):
        Frame1=tkinter.Frame(SMA)
        Frame1.pack(fill=BOTH, expand=True)
        
        def Student():
            Frame1.forget()
            Obj=Login_Student()

        def ST():
            Frame1.forget()
            Obj=Login_ST()
            
        def CT():
            Frame1.forget()
            Obj=Login_CT()

        def Previous():
            Frame1.forget()
            Menubar=Menu()
            Top_Menu=Menu_Bar(Menubar)
            Home.pack(fill=BOTH, expand=True)   

        Frame1.configure(background="white")
        Frame1.columnconfigure(0, weight=1)
        Frame1.columnconfigure(1, weight=1)

        Menubar=Menu(Frame1)
        Back=Menubar.add_command(label="Back", command=Previous)

        Text=Label(Frame1, text="Are you a", font=("Verdana", 70), background="white")
        Student=Button(Frame1, text="Student / Parent", command=Student, style="A.TButton")
        Subject_Teacher=Button(Frame1, text="Subject Teacher", command=ST, style="A.TButton")
        Class_Teacher=Button(Frame1, text="Class Teacher", command=CT, style="A.TButton")

        style1=Style()
        style1.configure("A.TButton", font=("Verdana", 40))

        Text.grid(column=0, row=0, columnspan=2, pady=40)
        Student.grid(column=0, row=1, pady=40, ipadx=15, ipady=15)
        Subject_Teacher.grid(column=1, row=1, columnspan=2, pady=40, ipadx=15, ipady=15)
        Class_Teacher.grid(column=0, row=2, columnspan=2, pady=40, ipadx=15, ipady=15)

        Top_Menu=Menu_Bar(Menubar)

class Login_Student:
    def __init__(self):
        Frame2=tkinter.Frame(SMA)
        Frame2.pack(fill=BOTH, expand=True)

        def Login():
            if bool(_Name.get())==False or bool(_Date.get())==False or bool(_Month.get())==False or bool(_Year.get())==False or bool(_Phone.get())==False:
                    messagebox.showerror("Error", "Some Field or Fields are Left Empty !!")
                    
            else:
                login1=Framework.Student(_Name.get())
                login1.__init__(_Name.get())

                try:
                    login1.Login((int(_Date.get()), int(_Month.get()), int(_Year.get())), _Phone.get())
                    
                    if Framework.Login_S==False:
                        messagebox.showerror("Error", "Sorry the Entered Information is Wrong !!")

                    else:
                        Frame2.forget()
                        Obj=Student1()

                except:
                    messagebox.showerror("Error", "Sorry the Entered Information is Wrong !!")
                    
        def Previous():
            Frame2.forget()
            Obj=Page1()

        Frame2.configure(background="white")   
        Frame2.columnconfigure(0, weight=1)
        Frame2.columnconfigure(1, weight=1)

        _Name=StringVar()
        _Date=StringVar()
        _Month=StringVar()
        _Year=StringVar()
        _Phone=StringVar()

        Menubar=Menu(Frame2)
        Back=Menubar.add_command(label="Back", command=Previous)

        Text1=Label(Frame2, text="LOGIN", font=("Verdana", 40), background="white")
        Text2=Label(Frame2, text="(For Student)", font=("Verdana", 20), background="white")

        Name=Label(Frame2, text="Enter your Name : ", font=("Verdana", 20, "bold"), background="white")
        Name_Ext=Label(Frame2, text="(in lower case without initial)", font=("Verdana", 20, "bold"), background="white")
        Name_Input=Entry(Frame2, textvariable=_Name, font=("Verdana", 20, "normal"))

        Date=Label(Frame2, text="Enter your \"Date\" of Birth (from 1 to 31) : ", font=("Verdana", 20, "bold"), background="white")
        Date_Input=Entry(Frame2, textvariable=_Date, font=("Verdana", 20, "normal"))

        Month=Label(Frame2, text="Enter your \"Month\" of Birth (from 1 to 12) : ", font=("Verdana", 20, "bold"), background="white")
        Month_Input=Entry(Frame2, textvariable=_Month, font=("Verdana", 20, "normal"))

        Year=Label(Frame2, text="Enter your \"Year\" of Birth (ex. 2005) : ", font=("Verdana", 20, "bold"), background="white")
        Year_Input=Entry(Frame2, textvariable=_Year, font=("Verdana", 20, "normal"))

        Phone=Label(Frame2, text="Enter your Phone Number :", font=("Verdana", 20, "bold"), background="white")
        Phone_Input=Entry(Frame2, textvariable=_Phone, font=("Verdana", 20, "normal"))

        style2=Style()
        style2.configure("B.TButton", font=("Verdana", 15))

        Clear=Button(Frame2, text="CLEAR", command=lambda:[Name_Input.delete(0, END), Date_Input.delete(0, END), Month_Input.delete(0, END), Year_Input.delete(0, END), Phone_Input.delete(0, END) ], style="B.TButton")
        Submit=Button(Frame2, text="SUBMIT", command=Login, style="B.TButton")

        Text1.grid(column=0, row=0, columnspan=2, pady=15)
        Text2.grid(column=0, row=1, columnspan=2)
        Name.grid(column=0, row=2, sticky=W, padx=40)
        Name_Ext.grid(column=0, row=3, pady=15, sticky=W, padx=40)
        Name_Input.grid(column=1, row=2, rowspan=2, pady=15)
        Date.grid(column=0, row=4, pady=15, sticky=W, padx=40)
        Date_Input.grid(column=1, row=4, pady=15)
        Month.grid(column=0, row=5, pady=15, sticky=W, padx=40)
        Month_Input.grid(column=1, row=5, pady=15)
        Year.grid(column=0, row=6, pady=15, sticky=W, padx=40)
        Year_Input.grid(column=1, row=6, pady=15)
        Phone.grid(column=0, row=7, pady=15, sticky=W, padx=40)
        Phone_Input.grid(column=1, row=7, pady=15)
        Clear.grid(column=1, row=8, pady=15)
        Submit.grid(column=1, row=9)

        Top_Menu=Menu_Bar(Menubar)

class Student1:
    def __init__(self):
        Frame3=tkinter.Frame(SMA)
        Frame3.pack(fill=BOTH, expand=True)

        Stu_Obj=Framework.Student(Framework._Name)
        
        def Logout():
            if messagebox.askokcancel("Logout","You Are About to Logout"):
                Frame3.forget()
                Obj=Login_Student()

        def Logout1():
                    if messagebox.askokcancel("Logout","You Are About to Logout"):
                        Frame3.forget()
                        Obj=Login_CT()

        def Previous1():
            Frame3.forget()
            Obj=CT_Review()        

        def Report():
            Frame3.forget()
            Obj=Exams()

        def func1():
            Stu_Obj.Total_Bar()

        def func2():
            Stu_Obj.Pie_Marks_Distribution()
            
        def func3():
            Stu_Obj.Overall_Radar()
            
        def func4():
            Stu_Obj.Subject_Bar()

        Frame3.configure(background="white")
        Frame3.columnconfigure(0, weight=1)
        Frame3.columnconfigure(1, weight=1)

        Menubar=Menu(Frame3)
        Logout=Menubar.add_command(label="Logout", command=Logout)

        Text1=Label(Frame3, text="Hello, " + Framework._Name.title(), font=("Verdana", 40), background="white")
        Text2=Label(Frame3, text="What do you want to see ?", font=("Verdana", 25), background="white")

        style3=Style()
        style3.configure("C.TButton", font=("Verdana", 20))

        Total_Bar=Button(Frame3, text="Comparison of Total Marks", command=func1, style="C.TButton")
        Pie=Button(Frame3, text="Distribution of subject marks", command=func2, style="C.TButton")
        Radar=Button(Frame3, text="Overall Academic Performance", command=func3, style="C.TButton")
        Group_Bar=Button(Frame3, text="Overall Performance in each subject", command=func4, style="C.TButton")
        Report_Card=Button(Frame3, text="Report Card", command=Report, style="C.TButton")

        Text1.grid(column=0, row=0, columnspan=2, pady=20, padx=40, sticky=W)
        Text2.grid(column=0, row=1, columnspan=2, pady=20, padx=100, sticky=W)
        Total_Bar.grid(column=0, row=2, pady=20)
        Pie.grid(column=1, row=2, pady=20)
        Radar.grid(column=0, row=3, pady=20)
        Group_Bar.grid(column=1, row=3, pady=20)
        Report_Card.grid(column=0, row=4, columnspan=2, pady=20)

        Top_Menu=Menu_Bar(Menubar)

class Exams:
    def __init__(self):
        Frame4=tkinter.Frame(SMA)
        Frame4.pack(fill=BOTH, expand=True)

        Stu_Obj=Framework.Student(Framework._Name)
        
        def Previous():
            Frame4.forget()
            Obj=Student1()

        def func1():
            Stu_Obj.Exam("Midterm-1")
            Stu_Obj.Report_Card()
            
        def func2():
            Stu_Obj.Exam("Terminal-1")
            Stu_Obj.Report_Card()
            
        def func3():
            Stu_Obj.Exam("Midterm-2")
            Stu_Obj.Report_Card()
            
        def func4():
            Stu_Obj.Exam("Terminal-2")
            Stu_Obj.Report_Card()
             
        Frame4.configure(background="white")
        Frame4.columnconfigure(0, weight=1)
        Frame4.columnconfigure(1, weight=1)

        Menubar=Menu(Frame4)
        Back=Menubar.add_command(label="Back", command=Previous)

        style4=Style()
        style4.configure("D.TButton", font=("Verdana", 30))

        Text=Label(Frame4, text="Please select a Exam from Below", font=("Verdana", 40), background="white")
        Midterm1=Button(Frame4, text="Midterm-1", command=func1, style="D.TButton")
        Terminal1=Button(Frame4, text="Terminal-1", command=func2, style="D.TButton")
        Midterm2=Button(Frame4, text="Midterm-2", command=func3, style="D.TButton")
        Terminal2=Button(Frame4, text="Terminal-2", command=func4, style="D.TButton")

        Text.grid(column=0, row=0, columnspan=2, pady=40, padx=40, sticky=W)
        Midterm1.grid(column=0, row=1, pady=40)
        Terminal1.grid(column=1, row=1, pady=40)
        Midterm2.grid(column=0, row=2, pady=40)
        Terminal2.grid(column=1, row=2, pady=40)

        Top_Menu=Menu_Bar(Menubar)

class Login_ST:
    def __init__(self):
        Frame5=tkinter.Frame(SMA)
        Frame5.pack(fill=BOTH, expand=True)
        
        def Login():
            login2=Framework.Teacher(_Username.get(), _Password.get())

            if Framework.Login_T==False:
                messagebox.showerror("Error", "Sorry the Entered Username or Password is Wrong !!")

            else:
                Frame5.forget()
                Obj=ST1()

        def Previous():
            Frame5.forget()
            Obj=Page1()  

        Frame5.configure(background="white")
        Frame5.columnconfigure(0, weight=1)
        Frame5.columnconfigure(1, weight=1)

        _Username=StringVar()
        _Password=StringVar()

        Menubar=Menu(Frame5)
        Back=Menubar.add_command(label="Back", command=Previous)

        Text1=Label(Frame5, text="LOGIN", font=("Verdana", 40), background="white")
        Text2=Label(Frame5, text="(For Subject Teacher)", font=("Verdana", 20), background="white")

        Username=Label(Frame5, text="Enter the Username : ", font=("Verdana", 20, "bold"), background="white")
        Username_Input=Entry(Frame5, textvariable=_Username, font=("Verdana", 20, "normal"))

        Password=Label(Frame5, text="Enter the Password : ", font=("Verdana", 20, "bold"), background="white")
        Password_Input=Entry(Frame5, textvariable=_Password, font=("Verdana", 20, "normal"), show="*")

        style5=Style()
        style5.configure("E.TButton", font=("Verdana", 15))

        Clear=Button(Frame5, text="CLEAR", command=lambda:[Username_Input.delete(0, END), Password_Input.delete(0, END)], style="E.TButton")
        Submit=Button(Frame5, text="SUBMIT", command=Login, style="E.TButton")

        Text1.grid(column=0, row=0, columnspan=2, pady=20)
        Text2.grid(column=0, row=1, columnspan=2)
        Username.grid(column=0, row=2, sticky=W, padx=40)
        Username_Input.grid(column=1, row=2, pady=20)
        Password.grid(column=0, row=3, sticky=W, padx=40)
        Password_Input.grid(column=1, row=3, pady=20)
        Clear.grid(column=1, row=4, pady=20)
        Submit.grid(column=1, row=5)

        Top_Menu=Menu_Bar(Menubar)

class ST1:
    def __init__(self):
        Frame6=tkinter.Frame(SMA)
        Frame6.pack(fill=BOTH, expand=True)

        def Logout():
            if messagebox.askokcancel("Logout","You Are About to Logout"):
                Frame6.forget()
                Obj=Login_ST()

        def func1():
            Frame6.forget()
            Obj=ST_Edit()

        def func2():
            Frame6.forget()
            Obj=ST_View()    

        Frame6.configure(background="white")
        Frame6.columnconfigure(0, weight=1)
        Frame6.columnconfigure(1, weight=1)

        Menubar=Menu(Frame6)
        Logout=Menubar.add_command(label="Logout", command=Logout)

        style6=Style()
        style6.configure("F.TButton", font=("Verdana", 25))

        Text1=Label(Frame6, text="Hello, " + Framework.Teachers[Framework.User][0].title(), font=("Verdana", 40), background="white")
        Text2=Label(Frame6, text="What do you want to do ?", font=("Verdana", 25), background="white")
        Edit=Button(Frame6, text="Edit", command=func1, style="F.TButton")
        View=Button(Frame6, text="View", command=func2, style="F.TButton")

        Text1.grid(column=0, row=0, columnspan=2, pady=20, padx=40, sticky=W)
        Text2.grid(column=0, row=1, columnspan=2, pady=20, padx=100, sticky=W)
        Edit.grid(column=0, row=2, pady=40)
        View.grid(column=1, row=2, pady=40)

        Top_Menu=Menu_Bar(Menubar)

class ST_Edit:
    def __init__(self):
        Frame7=tkinter.Frame(SMA)
        Frame7.pack(fill=BOTH, expand=True)

        def Logout():
            if messagebox.askokcancel("Logout","You Are About to Logout"):
                Frame7.forget()
                Obj=Login_ST()

        def Previous():
            Frame7.forget()
            Obj=ST1()

        def func1():
            try:
                global ST_Obj
                ST_Obj=Framework.ST(_Section.get())
            except:
                pass
            
        def func2():
            if bool(_Section.get())==True:
                try:
                    Name_Input["values"]=tuple(Framework.MARK1.keys())

                except:
                    pass

        def func3():
            if bool(_Section.get())==False or bool(_Exam.get())==False or bool(_Name.get())==False or bool(_New_Marks.get())==False:
                    messagebox.showerror("Error", "Some Field or Fields are Left Empty !!")
            else:
                ST_Obj.Edit(_Name.get(), _Exam.get(), _New_Marks.get())

                if Framework.Mistake1==True:
                    messagebox.showerror("Error", "The Marks should be between 0 and 100 !!")
                    
                else:
                    messagebox.showinfo("Success", "The Marks of the Student is changed Successfully !!")

        Frame7.configure(background="white")
        Frame7.columnconfigure(0, weight=1)
        Frame7.columnconfigure(1, weight=1)
        Frame7.columnconfigure(2, weight=1)
        Frame7.columnconfigure(3, weight=1)
        Frame7.rowconfigure(0, weight=1)

        Menubar=Menu(Frame7)
        Logout=Menubar.add_command(label="Logout", command=Logout)
        Back=Menubar.add_command(label="Back", command=Previous)

        style7=Style()
        style7.configure("G.TButton", font=("Verdana", 20))

        _Section=StringVar()
        _Exam=StringVar()
        _Name=StringVar()
        _New_Marks=IntVar()

        Section=Label(Frame7, text="Section", font=("Verdana", 20), background="white")
        Section_Input=Combobox(Frame7, textvariable=_Section, font=("Verdana", 20), state = "readonly")
        Section_Input["values"]=Framework.Teachers[Framework.User][2]

        Exam=Label(Frame7, text="Exam", font=("Verdana", 20), background="white")
        Exam_Input=Combobox(Frame7, textvariable=_Exam, font=("Verdana", 20), postcommand=func1, state = "readonly")
        Exam_Input["values"]=("Midterm-1", "Terminal-1", "Midterm-2", "Terminal-2")

        Name=Label(Frame7, text="Name of the Student", font=("Verdana", 20), background="white")
        Name_Input=Combobox(Frame7, textvariable=_Name, font=("Verdana", 20), postcommand=lambda: [func1(), func2()], state = "readonly")
                               
        New_Marks=Label(Frame7, text="New Marks", font=("Verdana", 20), background="white")
        New_Marks_Input=Entry(Frame7, textvariable=_New_Marks, font=("Verdana", 20, "normal"))

        Submit=Button(Frame7, text="Submit", command=func3, style="G.TButton")
        Clear=Button(Frame7, text="Clear", command=lambda:[Section_Input.set(""), Exam_Input.set(""), Name_Input.set(""), New_Marks_Input.delete(0, END)] , style="G.TButton")

        Section.grid(column=0, row=1, pady=20, padx=10)
        Exam.grid(column=1, row=1, pady=20, padx=10)
        Name.grid(column=2, row=1, pady=20, padx=10)
        New_Marks.grid(column=3, row=1, pady=20, padx=10)

        Section_Input.grid(column=0, row=2, pady=20, padx=10)
        Exam_Input.grid(column=1, row=2, pady=20, padx=10)
        Name_Input.grid(column=2, row=2, pady=20, padx=10)
        New_Marks_Input.grid(column=3, row=2, pady=20, padx=10)

        Submit.grid(column=0, row=3, columnspan=2, pady=100)
        Clear.grid(column=2, row=3, columnspan=2, pady=100)

        Top_Menu=Menu_Bar(Menubar)

class ST_View:
    def __init__(self):
        Frame8=tkinter.Frame(SMA)
        Frame8.pack(fill=BOTH, expand=True)

        def Logout():
            if messagebox.askokcancel("Logout","You Are About to Logout"):
                Frame8.forget()
                Obj=Login_ST()

        def Previous():
            Frame8.forget()
            Obj=ST1()

        def func1():
            try:
                global ST_Obj
                ST_Obj=Framework.ST(_Section.get())
            except:
                pass

        def func2():
            try:
                if bool(_Section.get())==True:
                    Name_Input["values"]=tuple(Framework.MARK1.keys())
            except:
                pass


        def func3():
            if bool(_Section.get())==False or bool(_Exam.get())==False or bool(_Name.get())==False:
                    messagebox.showerror("Error", "Some Field or Fields are Left Empty !!")
            else:
                ST_Obj.View(_Name.get(), _Exam.get())
                messagebox.showinfo("Marks",  _Name.get().title() + " have scored " + str(Framework.Marks) + " in " + _Exam.get())

        Frame8.configure(background="white")
        Frame8.columnconfigure(0, weight=1)
        Frame8.columnconfigure(1, weight=1)
        Frame8.columnconfigure(2, weight=1)
        Frame8.rowconfigure(0, weight=1)

        Menubar=Menu(Frame8)
        Logout=Menubar.add_command(label="Logout", command=Logout)
        Back=Menubar.add_command(label="Back", command=Previous)

        style8=Style()
        style8.configure("H.TButton", font=("Verdana", 20))

        _Section=StringVar()
        _Exam=StringVar()
        _Name=StringVar()
        _New_Marks=IntVar()

        Section=Label(Frame8, text="Section", font=("Verdana", 20), background="white")
        Section_Input=Combobox(Frame8, textvariable=_Section, font=("Verdana", 20), state = "readonly")
        Section_Input["values"]=Framework.Teachers[Framework.User][2]

        Exam=Label(Frame8, text="Exam", font=("Verdana", 20), background="white")
        Exam_Input=Combobox(Frame8, textvariable=_Exam, font=("Verdana", 20), postcommand=func1, state = "readonly")
        Exam_Input["values"]=("Midterm-1", "Terminal-1", "Midterm-2", "Terminal-2")

        Name=Label(Frame8, text="Name of the Student", font=("Verdana", 20), background="white")
        Name_Input=Combobox(Frame8, textvariable=_Name, font=("Verdana", 20), postcommand=lambda: [func1(), func2()], state = "readonly")
                               
        Submit=Button(Frame8, text="Submit", command=func3, style="H.TButton")
        Clear=Button(Frame8, text="Clear", command=lambda:[Section_Input.set(""), Exam_Input.set(""), Name_Input.set("")] , style="H.TButton")

        Section.grid(column=0, row=1, pady=20, padx=10)
        Exam.grid(column=1, row=1, pady=20, padx=10)
        Name.grid(column=2, row=1, pady=20, padx=10)

        Section_Input.grid(column=0, row=2, pady=20, padx=10)
        Exam_Input.grid(column=1, row=2, pady=20, padx=10)
        Name_Input.grid(column=2, row=2, pady=20, padx=10)

        Submit.grid(column=0, row=3, pady=100)
        Clear.grid(column=2, row=3, pady=100)

        Top_Menu=Menu_Bar(Menubar)

class Login_CT:
    def __init__(self):
        Frame9=tkinter.Frame(SMA)
        Frame9.pack(fill=BOTH, expand=True)

        def Login():
            login3=Framework.Teacher(_Username.get(), _Password.get())

            if Framework.Login_T==False and Framework.Login_CT==False:
                messagebox.showerror("Error", "Sorry the Entered Username or Password is Wrong !!")

            elif Framework.Login_T==True and Framework.Login_CT==False:
                messagebox.showerror("Error", "You're Not a Class Teacher !!")

            else:
                Frame9.forget()
                Obj=CT1()
                
        def Previous():
            Frame9.forget()
            Obj=Page1()
            
        Frame9.configure(background="white")
        Frame9.columnconfigure(0, weight=1)
        Frame9.columnconfigure(1, weight=1)

        _Username=StringVar()
        _Password=StringVar()

        Menubar=Menu(Frame9)
        Back=Menubar.add_command(label="Back", command=Previous)

        Text1=Label(Frame9, text="LOGIN", font=("Verdana", 40), background="white")
        Text2=Label(Frame9, text="(For Class Teacher)", font=("Verdana", 20), background="white")

        Username=Label(Frame9, text="Enter the Username : ", font=("Verdana", 20, "bold"), background="white")
        Username_Input=Entry(Frame9, textvariable=_Username, font=("Verdana", 20, "normal"))

        Password=Label(Frame9, text="Enter the Password : ", font=("Verdana", 20, "bold"), background="white")
        Password_Input=Entry(Frame9, textvariable=_Password, font=("Verdana", 20, "normal"), show="*")

        style9=Style()
        style9.configure("I.TButton", font=("Verdana", 15))

        Clear=Button(Frame9, text="CLEAR", command=lambda:[Username_Input.delete(0, END), Password_Input.delete(0, END)], style="I.TButton")
        Submit=Button(Frame9, text="SUBMIT", command=Login, style="I.TButton")

        Text1.grid(column=0, row=0, columnspan=2, pady=20)
        Text2.grid(column=0, row=1, columnspan=2)
        Username.grid(column=0, row=2, sticky=W, padx=40)
        Username_Input.grid(column=1, row=2, pady=20)
        Password.grid(column=0, row=3, sticky=W, padx=40)
        Password_Input.grid(column=1, row=3, pady=20)
        Clear.grid(column=1, row=4, pady=20)
        Submit.grid(column=1, row=5)

        Top_Menu=Menu_Bar(Menubar)

class CT1:
    def __init__(self):
        Frame10=tkinter.Frame(SMA)
        Frame10.pack(fill=BOTH, expand=True)

        def Logout():
            if messagebox.askokcancel("Logout","You Are About to Logout"):
                Frame10.forget()
                Obj=Login_CT()

        def func1():
            Frame10.forget()
            Obj=CT_Edit()

        def func2():
            Frame10.forget()
            Obj=CT_View()

        def func3():
            Frame10.forget()
            Obj=CT_Review()

        Frame10.configure(background="white")
        Frame10.columnconfigure(0, weight=1)
        Frame10.columnconfigure(1, weight=1)

        Menubar=Menu(Frame10)
        Logout=Menubar.add_command(label="Logout", command=Logout)

        style10=Style()
        style10.configure("J.TButton", font=("Verdana", 25))

        Text1=Label(Frame10, text="Hello, " + Framework.Teachers[Framework.User][0].title(), font=("Verdana", 40), background="white")
        Text2=Label(Frame10, text="What do you want to do ?", font=("Verdana", 25), background="white")
        Edit=Button(Frame10, text="Edit", command=func1, style="J.TButton")
        View=Button(Frame10, text="View", command=func2, style="J.TButton")
        Review=Button(Frame10, text="Review a Student's Performance", command=func3, style="J.TButton")

        Text1.grid(column=0, row=0, columnspan=2, pady=20, padx=40, sticky=W)
        Text2.grid(column=0, row=1, columnspan=2, pady=20, padx=100, sticky=W)
        Edit.grid(column=0, row=2, pady=40)
        View.grid(column=1, row=2, pady=40)
        Review.grid(column=0, row=3, columnspan=2, pady=40)

        Top_Menu=Menu_Bar(Menubar)

class CT_Edit:
    def __init__(self):
        Frame11=tkinter.Frame(SMA)
        Frame11.pack(fill=BOTH, expand=True)

        global CT_Obj
        CT_Obj=Framework.CT()
        
        def Logout():
            if messagebox.askokcancel("Logout","You Are About to Logout"):
                Frame11.forget()
                Obj=Login_CT()

        def Previous():
            Frame11.forget()
            Obj=CT1()
            
        def func1():
            if bool(_Subject.get())==False or bool(_Exam.get())==False or bool(_Name.get())==False or bool(_New_Marks.get())==False:
                    messagebox.showerror("Error", "Some Field or Fields are Left Empty !!")

            else:
                CT_Obj.Edit(_Name.get(), _Exam.get(), _Subject.get(), _New_Marks.get())

                if Framework.Mistake2==True:
                    messagebox.showerror("Error", "The Marks should be between 0 and 100 !!")

                else:
                    messagebox.showinfo("Success", "The Marks of the Student is changed Successfully !!")

        Frame11.configure(background="white")
        Frame11.columnconfigure(0, weight=1)
        Frame11.columnconfigure(1, weight=1)
        Frame11.columnconfigure(2, weight=1)
        Frame11.columnconfigure(3, weight=1)
        Frame11.rowconfigure(0, weight=1)

        Menubar=Menu(Frame11)
        Logout=Menubar.add_command(label="Logout", command=Logout)
        Back=Menubar.add_command(label="Back", command=Previous)

        style11=Style()
        style11.configure("K.TButton", font=("Verdana", 20))

        _Name=StringVar()
        _Exam=StringVar()
        _Subject=StringVar()
        _New_Marks=IntVar()

        Name=Label(Frame11, text="Name of the Student", font=("Verdana", 20), background="white")
        Name_Input=Combobox(Frame11, textvariable=_Name, font=("Verdana", 20), state = "readonly")
        Name_Input["values"]=tuple(Framework.MARK2.keys())

        Exam=Label(Frame11, text="Exam", font=("Verdana", 20), background="white")
        Exam_Input=Combobox(Frame11, textvariable=_Exam, font=("Verdana", 20), state = "readonly")
        Exam_Input["values"]=("Midterm-1", "Terminal-1", "Midterm-2", "Terminal-2")

        Subject=Label(Frame11, text="Subject", font=("Verdana", 20), background="white")
        Subject_Input=Combobox(Frame11, textvariable=_Subject, font=("Verdana", 20), state = "readonly")
        Subject_Input["values"]=Framework.Subjects
                               
        New_Marks=Label(Frame11, text="New Marks", font=("Verdana", 20), background="white")
        New_Marks_Input=Entry(Frame11, textvariable=_New_Marks, font=("Verdana", 20, "normal"))

        Submit=Button(Frame11, text="Submit", command=func1, style="K.TButton")
        Clear=Button(Frame11, text="Clear", command=lambda:[ Name_Input.set(""), Subject_Input.set(""), Exam_Input.set(""), New_Marks_Input.delete(0, END)] , style="K.TButton")

        Name.grid(column=0, row=1, pady=20, padx=10)
        Exam.grid(column=1, row=1, pady=20, padx=10)
        Subject.grid(column=2, row=1, pady=20, padx=10)
        New_Marks.grid(column=3, row=1, pady=20, padx=10)

        Name_Input.grid(column=0, row=2, pady=20, padx=10)
        Exam_Input.grid(column=1, row=2, pady=20, padx=10)
        Subject_Input.grid(column=2, row=2, pady=20, padx=10)
        New_Marks_Input.grid(column=3, row=2, pady=20, padx=10)

        Submit.grid(column=0, row=3, columnspan=2, pady=100)
        Clear.grid(column=2, row=3, columnspan=2, pady=100)

        Top_Menu=Menu_Bar(Menubar)

class CT_View:
    def __init__(self):
        Frame12=tkinter.Frame(SMA)
        Frame12.pack(fill=BOTH, expand=True)

        global CT_Obj
        CT_Obj=Framework.CT()

        def Logout():
            if messagebox.askokcancel("Logout","You Are About to Logout"):
                Frame12.forget()
                Obj=Login_CT()

        def Previous():
            Frame12.forget()
            Obj=CT1()

        def func1():
            if bool(_Subject.get())==False or bool(_Exam.get())==False or bool(_Name.get())==False:
                    messagebox.showerror("Error", "Some Field or Fields are Left Empty !!")

            else:
                CT_Obj.View(_Name.get(), _Exam.get(), _Subject.get())
                messagebox.showinfo("Marks",  _Name.get().title() + " have scored " + str(Framework.Marks) + " in " + _Subject.get() + " in " + _Exam.get())

        Frame12.configure(background="white")
        Frame12.columnconfigure(0, weight=1)
        Frame12.columnconfigure(1, weight=1)
        Frame12.columnconfigure(2, weight=1)
        Frame12.rowconfigure(0, weight=1)

        Menubar=Menu(Frame12)
        Logout=Menubar.add_command(label="Logout", command=Logout)
        Back=Menubar.add_command(label="Back", command=Previous)

        style12=Style()
        style12.configure("L.TButton", font=("Verdana", 20))

        _Name=StringVar()
        _Exam=StringVar()
        _Subject=StringVar()

        Name=Label(Frame12, text="Name of the Student", font=("Verdana", 20), background="white")
        Name_Input=Combobox(Frame12, textvariable=_Name, font=("Verdana", 20), state = "readonly")
        Name_Input["values"]=tuple(Framework.MARK2.keys())

        Exam=Label(Frame12, text="Exam", font=("Verdana", 20), background="white")
        Exam_Input=Combobox(Frame12, textvariable=_Exam, font=("Verdana", 20), state = "readonly")
        Exam_Input["values"]=("Midterm-1", "Terminal-1", "Midterm-2", "Terminal-2")

        Subject=Label(Frame12, text="Subject", font=("Verdana", 20), background="white")
        Subject_Input=Combobox(Frame12, textvariable=_Subject, font=("Verdana", 20), state = "readonly")
        Subject_Input["values"]=Framework.Subjects

        Submit=Button(Frame12, text="Submit", command=func1, style="L.TButton")
        Clear=Button(Frame12, text="Clear", command=lambda:[ Name_Input.set(""), Subject_Input.set(""), Exam_Input.set("")] , style="L.TButton")

        Name.grid(column=0, row=1, pady=20, padx=10)
        Exam.grid(column=1, row=1, pady=20, padx=10)
        Subject.grid(column=2, row=1, pady=20, padx=10)

        Name_Input.grid(column=0, row=2, pady=20, padx=10)
        Exam_Input.grid(column=1, row=2, pady=20, padx=10)
        Subject_Input.grid(column=2, row=2, pady=20, padx=10)

        Submit.grid(column=0, row=3, pady=100)
        Clear.grid(column=2, row=3, pady=100)

        Top_Menu=Menu_Bar(Menubar)

class CT_Review:
    def __init__(self):
        Frame13=tkinter.Frame(SMA)
        Frame13.pack(fill=BOTH, expand=True)

        global CT_Obj
        CT_Obj=Framework.CT()


        def Logout():
            if messagebox.askokcancel("Logout","You Are About to Logout"):
                Frame13.forget()
                Obj=Login_CT()

        def Previous():
            Frame13.forget()
            Obj=CT1()

        def func1():
            if bool(_Name.get())==False:
                    messagebox.showerror("Error", "The Name is Left Empty !!")
                    
            else:                    
                Framework._Name=_Name.get()
                Frame13.forget()
                Obj=CT_Student()
                
        Frame13.configure(background="white")
        Frame13.columnconfigure(0, weight=1)
        Frame13.columnconfigure(1, weight=1)

        Menubar=Menu(Frame13)
        Logout=Menubar.add_command(label="Logout", command=Logout)
        Back=Menubar.add_command(label="Back", command=Previous)

        style13=Style()
        style13.configure("M.TButton", font=("Verdana", 20))

        _Name=StringVar()

        Text=Label(Frame13, text="Please Select the Name of the Student from the Following : ", font=("Verdana", 40), background="white")

        Name_Input=Combobox(Frame13, textvariable=_Name, font=("Verdana", 20), state = "readonly")
        Name_Input["values"]=tuple(Framework.MARK2.keys())

        Submit=Button(Frame13, text="Submit", command=func1, style="M.TButton")
        Clear=Button(Frame13, text="Clear", command=lambda:[ Name_Input.set("")] , style="M.TButton")

        Text.grid(column=0, row=0, columnspan=2, padx=40, pady=10, sticky=W)
        Name_Input.grid(column=0, row=1, columnspan=2, pady=100)

        Submit.grid(column=0, row=2, pady=20)
        Clear.grid(column=1, row=2, pady=20)

        Top_Menu=Menu_Bar(Menubar)

class CT_Student:
    def __init__(self):
        Frame14=tkinter.Frame(SMA)
        Frame14.pack(fill=BOTH, expand=True)

        Stu_Obj=Framework.Student(Framework._Name)
        
        def Logout():
            if messagebox.askokcancel("Logout","You Are About to Logout"):
                Frame14.forget()
                Obj=Login_CT()

        def Previous():
            Frame14.forget()
            Obj=CT_Review()        

        def Report():
            Frame14.forget()
            Obj=CT_Exams()

        def func1():
            Stu_Obj.Total_Bar()

        def func2():
            Stu_Obj.Pie_Marks_Distribution()
            
        def func3():
            Stu_Obj.Overall_Radar()
            
        def func4():
            Stu_Obj.Subject_Bar()

        Frame14.configure(background="white")
        Frame14.columnconfigure(0, weight=1)
        Frame14.columnconfigure(1, weight=1)

        Menubar=Menu(Frame14)
        Logout=Menubar.add_command(label="Logout", command=Logout)
        Back=Menubar.add_command(label="Back", command=Previous)
        Top_Menu=Menu_Bar(Menubar)

        Text1=Label(Frame14, text="Hello, " + Framework._Name.title(), font=("Verdana", 40), background="white")
        Text2=Label(Frame14, text="What do you want to see ?", font=("Verdana", 25), background="white")

        style14=Style()
        style14.configure("N.TButton", font=("Verdana", 20))

        Total_Bar=Button(Frame14, text="Comparison of Total Marks", command=func1, style="N.TButton")
        Pie=Button(Frame14, text="Distribution of subject marks", command=func2, style="N.TButton")
        Radar=Button(Frame14, text="Overall Academic Performance", command=func3, style="N.TButton")
        Group_Bar=Button(Frame14, text="Overall Performance in each subject", command=func4, style="N.TButton")
        Report_Card=Button(Frame14, text="Report Card", command=Report, style="N.TButton")

        Text1.grid(column=0, row=0, columnspan=2, pady=20, padx=40, sticky=W)
        Text2.grid(column=0, row=1, columnspan=2, pady=20, padx=100, sticky=W)
        Total_Bar.grid(column=0, row=2, pady=20)
        Pie.grid(column=1, row=2, pady=20)
        Radar.grid(column=0, row=3, pady=20)
        Group_Bar.grid(column=1, row=3, pady=20)
        Report_Card.grid(column=0, row=4, columnspan=2, pady=20)

        Top_Menu=Menu_Bar(Menubar)

class CT_Exams:
    def __init__(self):
        Frame15=tkinter.Frame(SMA)
        Frame15.pack(fill=BOTH, expand=True)

        Stu_Obj=Framework.Student(Framework._Name)
        
        def Previous():
            Frame15.forget()
            Obj=CT_Student()

        def func1():
            Stu_Obj.Exam("Midterm-1")
            Stu_Obj.Report_Card()
            Frame15.forget()
            Obj=CT_Student()
            
        def func2():
            Stu_Obj.Exam("Terminal-1")
            Stu_Obj.Report_Card()
            Frame15.forget()
            Obj=CT_Student()
            
        def func3():
            Stu_Obj.Exam("Midterm-2")
            Stu_Obj.Report_Card()
            Frame15.forget()
            Obj=CT_Student()
            
        def func4():
            Stu_Obj.Exam("Terminal-2")
            Stu_Obj.Report_Card()
            Frame15.forget()
            Obj=CT_Student()
             
        Frame15.configure(background="white")
        Frame15.columnconfigure(0, weight=1)
        Frame15.columnconfigure(1, weight=1)

        Menubar=Menu(Frame15)
        Back=Menubar.add_command(label="Back", command=Previous)

        style15=Style()
        style15.configure("O.TButton", font=("Verdana", 30))

        Text=Label(Frame15, text="Please select a Exam from Below", font=("Verdana", 40), background="white")
        Midterm1=Button(Frame15, text="Midterm-1", command=func1, style="O.TButton")
        Terminal1=Button(Frame15, text="Terminal-1", command=func2, style="O.TButton")
        Midterm2=Button(Frame15, text="Midterm-2", command=func3, style="O.TButton")
        Terminal2=Button(Frame15, text="Terminal-2", command=func4, style="O.TButton")

        Text.grid(column=0, row=0, columnspan=2, pady=40, padx=40, sticky=W)
        Midterm1.grid(column=0, row=1, pady=40)
        Terminal1.grid(column=1, row=1, pady=40)
        Midterm2.grid(column=0, row=2, pady=40)
        Terminal2.grid(column=1, row=2, pady=40)

        Top_Menu=Menu_Bar(Menubar)        

SMA.mainloop()
