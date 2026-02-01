from customtkinter import *
from sqlite3 import *
import datetime
from PIL import Image

Icon = Image.open("absent.ico")

MainWindow = CTk()
MainWindow.geometry("500x400")
MainWindow.title("Absence Entring Part")
MainWindow.configure(fg_color="#fffed7")
MainWindow.resizable(False, False)
MainWindow.iconbitmap("absent.ico")

Image = CTkImage(light_image=Icon, size=(45, 45))

date = str(datetime.datetime.now().date())
time = str(datetime.datetime.now().time().strftime("%H") + ":30")
# time = "8:30"

DateLabel = CTkLabel(MainWindow, text=date, font=("Arial", 14), fg_color="#fffed7")
DateLabel.place(y=0, x=420)

ImageLabel = CTkLabel(MainWindow, image=Image, text="", fg_color="#fffed7")
ImageLabel.place(y=0, x=230)

EntryFrame = CTkFrame(MainWindow, width=480, height=210, fg_color="#e6e2b3", corner_radius=10)
EntryFrame.place(y=50, x=10)

StudentNameOrIDEntry = CTkEntry(EntryFrame, width=200, height=30, placeholder_text="Student Name or ID")
StudentNameOrIDEntry.place(y=30, x=140)

TeacherNameOrIDEntry = CTkEntry(EntryFrame, width=200, height=30, placeholder_text="Teacher Name Or ID")
TeacherNameOrIDEntry.place(y=70, x=140)

ClassEntry = CTkEntry(EntryFrame, width=200, height=30, placeholder_text="Class")
ClassEntry.place(y=110, x=140)

def SubmitHandler():
    Student = StudentNameOrIDEntry.get().lower()
    Teacher = TeacherNameOrIDEntry.get().lower()
    Class = ClassEntry.get().lower()
    
    DBF = connect("DataBase.db")
    Cursor = DBF.cursor()

    # Verify if class exists:
    try:
        Students = Cursor.execute(f"SELECT studentname FROM {Class}_students").fetchall()
    except OperationalError:
        SuccessLabel.configure(text="Class Not Found!", text_color="#ff0000")
        SuccessLabel.place(y=195, relx=0.5, anchor="center")

    # Verify if teacher exists:
    TeacherExistanceVerification = Cursor.execute(f"SELECT teacherName FROM {Class}_schedule WHERE teacherName = ?", (Teacher,)).fetchone()
    if not TeacherExistanceVerification:
        SuccessLabel.configure(text="Teacher Not Found!", text_color="#ff0000")
        SuccessLabel.place(y=195, relx=0.5, anchor="center")
        DBF.close()
        return
    else:
        pass
    
    # Verify if Teacher exists and that Teacher teaches the class at this time:
    TeacherVerification = Cursor.execute(f"SELECT teacherName FROM {Class}_schedule WHERE time = ?", (time, )).fetchone()
    if Teacher != TeacherVerification[0]:
        SuccessLabel.configure(text="You can't enter the absences of this class now!", text_color="#ff0000")
        SuccessLabel.place(y=195, relx=0.5, anchor="center")
        DBF.close()
        return
    else:
        pass

    # Verify if student exists:
    try:
        if (Student,) in Students:
            # Verify if absence already recorded:
            Absence = Cursor.execute(f"SELECT * FROM {Class}_absences WHERE STUDENTID = ? AND ABSENCEDATE = ? AND ABSENCETIME = ?", (Student, date, time)).fetchall()
            if not Absence:
                Cursor.execute(f"INSERT INTO {Class}_absences VALUES(?,?,?)", (Student, date, time))
                Cursor.execute(f"UPDATE {Class}_students SET entringpermession = '0' WHERE STUDENTNAME = ?", (Student,))
                SuccessLabel.configure(text="Absence Recorded Successfully!", text_color="#00c51d")
                SuccessLabel.place(y=194, relx=0.5, anchor="center")
                StudentNameOrIDEntry.delete("0", "end")
                StudentNameOrIDEntry.configure(placeholder_text="Student Name or ID")
            else:
                SuccessLabel.configure(text="Absence Already Recorded!", text_color="#ff0000")
                SuccessLabel.place(y=194, relx=0.5, anchor="center")
        else:
            SuccessLabel.configure(text="Student Not Found!", text_color="#ff0000")
            SuccessLabel.place(y=194, relx=0.5, anchor="center")
            DBF.close()
            return
    except:
        return
    
    DBF.commit()
    DBF.close()
    SearchingNotAllowedStudents()

SubmitButton = CTkButton(EntryFrame, width=100, height=30, text="Submit", command= SubmitHandler)
SubmitButton.place(y=150, x=100)

def RemoveHandler():
    Student = StudentNameOrIDEntry.get().lower()
    Teacher = TeacherNameOrIDEntry.get()
    Class = ClassEntry.get().lower()
    
    DBF = connect("DataBase.db")
    Cursor = DBF.cursor()

    # Verify if class exists:
    try:
        Students = Cursor.execute(f"SELECT studentName FROM {Class}_students").fetchall()
    except:
        SuccessLabel.configure(text="Class Not Found!", text_color="#ff0000")
        SuccessLabel.place(y=194, relx=0.5, anchor="center")

    # Verify if Teacher exists and that Teacher teaches the class at this time:
    TeacherVerification = Cursor.execute(f"SELECT teacherName FROM {Class}_schedule WHERE time = ?", (time, )).fetchone()
    if Teacher != TeacherVerification[0]:
        SuccessLabel.configure(text="You can't remove the absences of this class now!", text_color="#ff0000")
        SuccessLabel.place(y=194, relx=0.5, anchor="center")
        DBF.close()
        return
    else:
        pass
    
    # Verify if Student exists:
    try:
        if (Student,) in Students:
            # Verify if absence exists:
            Absence = Cursor.execute(f"SELECT * FROM {Class}_absences WHERE STUDENTID = ? AND ABSENCEDATE = ? AND ABSENCETIME = ?", (Student, date, time)).fetchall()
            if Absence:
                Cursor.execute(f"DELETE FROM {Class}_absences WHERE STUDENTID = ? AND ABSENCEDATE = ? AND ABSENCETIME = ?", (Student, date, time))
                Cursor.execute(f"UPDATE {Class}_students SET entringpermession = '1' WHERE STUDENTNAME = ?", (Student,))
                SuccessLabel.configure(text="Absence Deleted Successfully!", text_color="#00c51d")
                SuccessLabel.place(y=194, relx=0.5, anchor="center")
                StudentNameOrIDEntry.delete("0", "end")
                StudentNameOrIDEntry.configure(placeholder_text="Student Name or ID")
            else:
                SuccessLabel.configure(text="Absence Not Found!", text_color="#ff0000")
                SuccessLabel.place(y=194, relx=0.5, anchor="center")
        else:
            SuccessLabel.configure(text="Student Not Found!", text_color="#ff0000")
            SuccessLabel.place(y=194, relx=0.5, anchor="center")
            DBF.close()
            return
    except:
        return
    
    DBF.commit()
    DBF.close()
    SearchingNotAllowedStudents()


RemoveButton = CTkButton(EntryFrame, width=100, height=30, text="Remove", fg_color="#ff0000", hover_color="#cc0000", cursor="hand2", command=RemoveHandler)
RemoveButton.place(y=150, x=200)

def JustifyHandler():
    Student = StudentNameOrIDEntry.get().lower()
    Teacher = TeacherNameOrIDEntry.get()
    Class = ClassEntry.get().lower()
    
    DBF = connect("DataBase.db")
    Cursor = DBF.cursor()

    # Verify if class exists:
    try:
        Students = Cursor.execute(f"SELECT studentName FROM {Class}_students").fetchall()
    except:
        SuccessLabel.configure(text="Class Not Found!", text_color="#ff0000")
        SuccessLabel.place(y=194, relx=0.5, anchor="center")

    # Verify if Teacher exists and that Teacher teaches the class at this time:
    TeacherVerification = Cursor.execute(f"SELECT teacherName FROM {Class}_schedule WHERE time = ?", (time, )).fetchone()
    if Teacher != TeacherVerification[0]:
        SuccessLabel.configure(text="You can't justify the absences of this class now!", text_color="#ff0000")
        SuccessLabel.place(y=194, relx=0.5, anchor="center")
        DBF.close()
        return
    else:
        pass
    
    # Verify if Student exists:
    try:
        if (Student,) in Students:
            Cursor.execute(f"UPDATE {Class}_students SET entringpermession = '1' WHERE STUDENTNAME = ?", (Student,))
            SuccessLabel.configure(text="Absence Justified Successfully!", text_color="#00c51d")
            SuccessLabel.place(y=194, relx=0.5, anchor="center")
            StudentNameOrIDEntry.delete("0", "end")
            StudentNameOrIDEntry.configure(placeholder_text="Student Name or ID")
        else:
            SuccessLabel.configure(text="Student Not Found!", text_color="#ff0000")
            SuccessLabel.place(y=194, relx=0.5, anchor="center")
            DBF.close()
            return
    except:
        return
    
    DBF.commit()
    DBF.close()
    SearchingNotAllowedStudents()

JustifyButton = CTkButton(EntryFrame, width=100, height=30, text="Justify", fg_color="#25df00", hover_color="#21c500", cursor="hand2", command=JustifyHandler)
JustifyButton.place(y=150, x=300)

SuccessLabel = CTkLabel(EntryFrame, text="", font=("Arial", 14), fg_color="transparent", text_color="#00c51d")
SuccessLabel.place(y=194, relx=0.5, anchor="center")

def SearchingNotAllowedStudents():
    DBF = connect("DataBase.db")
    Cursor = DBF.cursor()

    NotAllowedStudents = Cursor.execute("SELECT StudentName FROM tc1_students WHERE entringPermession = 0").fetchall()
    for Student in NotAllowedStudents:
        CTkLabel(LastAbsencesFrame, text=Student[0], font=("Arial", 14)).pack(anchor="w", pady=0, padx=10)

    DBF.commit()
    DBF.close()
    
LastAbsencesFrame = CTkScrollableFrame(MainWindow, width=455, height=200, fg_color="#e6e2b3", corner_radius=10, orientation="vertical")
LastAbsencesFrame.place(y=270, x=10, relheight=0.3)

SearchingNotAllowedStudents() 
MainWindow.mainloop()