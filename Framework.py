import pickle
import numpy as np
import plotly.graph_objects as go
import plotly.offline as pyo
import plotly.express as px
import pandas as pd
from jinja2 import Environment, FileSystemLoader
import webbrowser
from PIL import Image
from copy import deepcopy
        
File=open("Data.bin", "rb")

Marks_A=pickle.load(File)
Marks_B=pickle.load(File)
Marks_C=pickle.load(File)
Marks_D=pickle.load(File)
Details_A=pickle.load(File)
Details_B=pickle.load(File)
Details_C=pickle.load(File)
Details_D=pickle.load(File)
Attendance_A=pickle.load(File)
Attendance_B=pickle.load(File)
Attendance_C=pickle.load(File)
Attendance_D=pickle.load(File)
Teachers=pickle.load(File)
Class_Teachers=pickle.load(File)
Sub=pickle.load(File)

File.close()

class Student:
    def __init__(self, Student_Name):
        global _Name

        def Total():
            self.Total={}

            for i in self.Marks:
                Dup={}
                for j in self.Marks[i]:
                    try:
                        Dup[j]=sum(self.Marks[i][j])
                    except:
                        pass
                    
                self.Total[i]=Dup
                
            del self.Total["Section"]
                    
        _Name=Student_Name
        self.Name=Student_Name
        
        if self.Name in Marks_A:
            self.Marks=Marks_A
            Total()
            self.Details=Details_A
            self.Attend=Attendance_A
            self.Sec=self.Marks["Section"]
            self.Login_S=True

        elif self.Name in Marks_B:
            self.Marks=Marks_B
            Total()
            self.Details=Details_B
            self.Attend=Attendance_B
            self.Sec=self.Marks["Section"]
            self.Login_S=True

        elif self.Name in Marks_C:
            self.Marks=Marks_C
            Total()
            self.Details=Details_C
            self.Attend=Attendance_C
            self.Sec=self.Marks["Section"]
            self.Login_S=True

        elif self.Name in Marks_D:
            self.Marks=Marks_D
            Total()
            self.Details=Details_D
            self.Attend=Attendance_D
            self.Sec=self.Marks["Section"]
            self.Login_S=True

        else:
            self.Login_S=False
                
            
    def Login(self, DOB, Phone):
        global Login_S
        self.Dob=DOB
        self.Phone_No=Phone

        if self.Login_S:
            if self.Dob==self.Details[self.Name]["DOB"] and self.Phone_No==self.Details[self.Name]["Phone"]:
                    Login_S=True

            else:
                Login_S=False

        else:
            Login_S=False

    def Exam(self, Exam):
        self.Exam=Exam
            
    def Percentage(self):
        Total_Mark=self.Total[self.Name][self.Exam]

        self.Percent=round((Total_Mark/500)*100, 2)

    def Rank(self):        
        Ranking=[]
        Ranks=[]
        Num=1

        for i in self.Total:
            Ranking.append((i,self.Total[i][self.Exam]))
            Ranks.append([Num])
            Num+=1
            
        Ranking=np.array(Ranking)
        Ranking=sorted(Ranking, key=lambda x:x[1], reverse=True)        
        Ranking=np.concatenate((Ranking,Ranks), axis=1)

        Var=[0,0,0]

        for j in Ranking:
            if j[1]==Var[1]:
                Ranking[(int(j[2])-1),2]=Var[2]

            else:
                Var=j

        for k in Ranking:
            if self.Name in k:
                self.Rank_Info=k

    def Attendance(self):        
        self.Atten=self.Attend[self.Name][self.Exam]
        self.Atten_Percent=round((self.Atten[0]/self.Atten[1])*100,2)

    def Grade(self):        
        Subject_Marks=self.Marks[self.Name][self.Exam]
        self.Grade=()

        for x in Subject_Marks:
            if 90<x<=100:
                self.Grade+=("A1",)

            elif 80<x<=90:
                self.Grade+=("A2",)

            elif 70<x<=80:
                self.Grade+=("B1",)

            elif 60<x<=70:
                self.Grade+=("B2",)

            elif 50<x<=60:
                self.Grade+=("C1",)

            elif 40<x<=50:
                self.Grade+=("C2",)

            elif 33<x<=40:
                self.Grade+=("D",)

            else:
                self.Grade+=("E",)


    def Report_Card(self):
        Student.Grade(self)
        Student.Attendance(self)
        Student.Percentage(self)
        Student.Rank(self)

        Report=[{}]

        Report[0]["Exam"]=self.Exam
        Report[0]["Name"]=self.Name.title()
        Report[0]["Sec"]=self.Sec
        Report[0]["Teacher"]=Class_Teachers[self.Sec]
        Report[0]["Date"]=self.Details[self.Name]["DOB"][0]
        Report[0]["Month"]=self.Details[self.Name]["DOB"][1]
        Report[0]["Year"]=self.Details[self.Name]["DOB"][2]
        Report[0]["Subject"]=Sub[self.Sec]
        Report[0]["Marks"]=self.Marks[self.Name][self.Exam]
        Report[0]["Grade"]=self.Grade
        Report[0]["Total"]=self.Total[self.Name][self.Exam]
        Report[0]["Percent"]=self.Percent
        Report[0]["Rank"]=self.Rank_Info[2]
        Report[0]["Atten"]=self.Atten
        Report[0]["Atten_Percent"]=self.Atten_Percent
        Report=list(Report)

        file_loader = FileSystemLoader(r'C:\Users\dell\OneDrive\Desktop\IP\2022-2023\CSc IP')
        env = Environment(loader=file_loader)

        template = env.get_template('Report_Card.html')
        output = template.render(content=Report)

        file=open('Report.html', 'w')
        file.write(output)
        file.close()
        
        webbrowser.open('Report.html')
        
                
    def Total_Bar(self):

        Data={"Total":[self.Total[self.Name]["Midterm-1"],self.Total[self.Name]["Terminal-1"],self.Total[self.Name]["Midterm-2"],self.Total[self.Name]["Terminal-2"]]}

        Df=pd.DataFrame(Data, index=["Midterm-1", "Terminal-1", "Midterm-2", "Terminal-2"])

        TotalBar=px.bar(Df,title="Total Marks of across all Examinations of " + self.Name.title(), text_auto=True)
        TotalBar.show()
        
    def Overall_Radar(self):

        Subjects=np.array(Sub[self.Sec])
        Subjects=np.array([*Subjects, Subjects[0]])

        Midterm_1=np.array(self.Marks[self.Name]["Midterm-1"])
        Terminal_1=np.array(self.Marks[self.Name]["Terminal-1"])
        Midterm_2=np.array(self.Marks[self.Name]["Midterm-2"])
        Terminal_2=np.array(self.Marks[self.Name]["Terminal-2"])

        Midterm_1=np.array([*Midterm_1, Midterm_1[0]])
        Terminal_1=np.array([*Terminal_1, Terminal_1[0]])
        Midterm_2=np.array([*Midterm_2, Midterm_2[0]])
        Terminal_2=np.array([*Terminal_2, Terminal_2[0]])

        Radar=go.Figure(
            data=[go.Scatterpolar(r=Midterm_1, theta=Subjects, fill='toself', name="Midterm-1"),
                  go.Scatterpolar(r=Terminal_1, theta=Subjects, fill='toself', name="Terminal-1"),
                  go.Scatterpolar(r=Midterm_2, theta=Subjects, fill='toself', name="Midterm-2"),
                  go.Scatterpolar(r=Terminal_2, theta=Subjects, fill='toself', name="Terminal-2")],

            layout=go.Layout(title=go.layout.Title(text="Overall Marks Comparison of " + self.Name.title() + " in the Academic Year 2022-23"), polar={"radialaxis": {"visible": True}}, showlegend=True)
            )

        Radar.show()

    def Pie_Marks_Distribution(self):

        All_Marks=self.Marks[self.Name]["Midterm-1"] + self.Marks[self.Name]["Terminal-1"] + self.Marks[self.Name]["Midterm-2"] + self.Marks[self.Name]["Terminal-2"]

        Lower_Limit=[0,10,20,30,40,50,60,70,80,90]
        Max=100

        Var1=np.histogram(All_Marks, Lower_Limit+[Max])[0]

        Var2=[]
        Var3=["0-10","10-20","20-30","30-40","40-50","50-60","60-70","70-80","80-90","90-100"]

        for x in Var1:                
            x=(x/20)*100
            Var2+=[x]
            

        Distribution=[]
        Class_Intervals=[]
        Counter=0

        while Counter<len(Var2):
            if Var2[Counter]>0:
                Distribution.append(Var2[Counter])
                Class_Intervals.append(Var3[Counter])

            Counter+=1    

        Distribution=Distribution[::-1]
        Class_Intervals=Class_Intervals[::-1]
        
        Data={"Distribution":Distribution,
                 "Class_Intervals":Class_Intervals}

        Df=pd.DataFrame(Data)

        Pie=px.pie(Df, title="Marks Distribution of " + self.Name.title(), values="Distribution", names="Class_Intervals")
        Pie.update_traces(textposition='inside', textinfo='percent+label')
        Pie.show()

    def Subject_Bar(self):
        
        Data={"Midterm-1":self.Marks[self.Name]["Midterm-1"],
              "Terminal-1":self.Marks[self.Name]["Terminal-1"],
              "Midterm-2":self.Marks[self.Name]["Midterm-2"],
              "Terminal-2":self.Marks[self.Name]["Terminal-2"]}

        Df=pd.DataFrame(Data, index=Sub[self.Sec])

        Bar=px.bar(Df, x=["Midterm-1","Terminal-1","Midterm-2","Terminal-2"], y=Sub[self.Sec], title="Total Marks of Each Subject of " + self.Name.title(), text_auto=True, barmode='group')

        Bar.show()
      

class Teacher:
    def __init__(self, Username, Password):
        global Login_T
        global Login_CT
        global User

        User=Username
        self.Teachers=Teachers

        if Username in self.Teachers and Password==self.Teachers[Username][1]:
            Login_T=True

            if self.Teachers[Username][-1]=="CT":
                Login_CT=True

            else:
                Login_CT=False

        else:
            Login_T=False
            Login_CT=False
            
class ST:
    def __init__(self, Section):
        global MARK1

        self.Teachers=Teachers
        self.Sub=Sub
        
        self.Sec=Section
        self.Class=self.Teachers[User][2]
        self.Subject=self.Teachers[User][3]
        self.Index=self.Sub[Section].index(self.Subject)

        if Marks_A["Section"]==self.Sec:
            self.Marks=Marks_A

        elif Marks_B["Section"]==self.Sec:
            self.Marks=Marks_B

        elif Marks_C["Section"]==self.Sec:
            self.Marks=Marks_C

        else:
            self.Marks=Marks_D

        MARK1=self.Marks
        
    def Edit(self, Name, Exam, New_Marks):
        global Mistake1
        
        if 0<=New_Marks<=100:
            self.Marks[Name][Exam]=list(self.Marks[Name][Exam])
            self.Marks[Name][Exam][self.Index]=New_Marks
            self.Marks[Name][Exam]=tuple(self.Marks[Name][Exam])
            Mistake1=False

        else:
            Mistake1=True

            
    def View(self, Name, Exam):
        global Marks
        Marks=self.Marks[Name][Exam][self.Index]

class CT:
    def __init__(self):
        global MARK2
        global Subjects
        
        CT_Name=Teachers[User][0]

        for x in Class_Teachers:
            if Class_Teachers[x]==CT_Name:
                self.Sec=x

        if Marks_A["Section"]==self.Sec:
            self.Marks=Marks_A

        elif Marks_B["Section"]==self.Sec:
            self.Marks=Marks_B

        elif Marks_C["Section"]==self.Sec:
            self.Marks=Marks_C

        else:
            self.Marks=Marks_D

        MARK2=self.Marks
        Subjects=Sub[self.Sec]
            
    def Edit(self, Name, Exam, Subject, New_Marks):
        global Mistake2

        self.Index=Sub[self.Sec].index(Subject)
        if 0<=New_Marks<=100:
            self.Marks[Name][Exam]=list(self.Marks[Name][Exam])
            self.Marks[Name][Exam][self.Index]=New_Marks
            self.Marks[Name][Exam]=tuple(self.Marks[Name][Exam])
            Mistake2=False

        else:
            Mistake2=True

    def View(self, Name, Exam, Subject):
        global Marks
        self.Index=Sub[self.Sec].index(Subject)
        
        Marks=self.Marks[Name][Exam][self.Index]

class Update():
    def __init__(self):
        File=open("Data.bin", "wb")
        pickle.dump(Marks_A, File)
        pickle.dump(Marks_B, File)
        pickle.dump(Marks_C, File)
        pickle.dump(Marks_D, File)
        pickle.dump(Details_A, File)
        pickle.dump(Details_B, File)
        pickle.dump(Details_C, File)
        pickle.dump(Details_D, File)
        pickle.dump(Attendance_A, File)
        pickle.dump(Attendance_B, File)
        pickle.dump(Attendance_C, File)
        pickle.dump(Attendance_D, File)
        pickle.dump(Teachers, File)
        pickle.dump(Class_Teachers, File)
        pickle.dump(Sub, File)
        File.close()
