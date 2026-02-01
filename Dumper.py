from sqlite3 import *

tc1 = [
    ("A0001", "amine bakkari", 1),
    ("A0002", "fatima abdelaziz", 1),
    ("A0003", "youssef elhaj", 1),
    ("A0004", "sara lahlou", 1),
    ("A0005", "khalid rachid", 1)
]

tc2 = [
    ("B0001", "nadia saidi", 1),
    ("B0002", "omar ziani", 1),
    ("B0003", "laila benjelloun", 1),
    ("B0004", "hassan elouardi", 1),
    ("B0005", "meryem chafik", 1)
]

tc3 = [
    ("C0001", "rachid tazi", 1),
    ("C0002", "salma idrissi", 1),
    ("C0003", "yassine fassi", 1),
    ("C0004", "imane bouzid", 1),
    ("C0005", "adil mansouri", 1)
]

tc4 = [
    ("D0001", "khadija El Amrani", 1),
    ("D0002", "said bennis", 1),
    ("D0003", "nour el houda", 1),
    ("D0004", "jamal ezzarouali", 1),
    ("D0005", "wafaa laaroussi", 1)
]

tc5 = [
    ("E0001", "tariq alami", 1),
    ("E0002", "salim hariri", 1),
    ("E0003", "dounia rifi", 1),
    ("E0004", "yasmina choukri", 1),
    ("E0005", "hicham bouazza", 1)
]

tc1_schudle = [
    ("8:30", "math", "khadija khaddiri", "E0001"),
    ("9:30", "physics", "nour jamal", "E0002"),
    ("10:30", "chemistry", "omar zaki", "E0003"),
    ("11:30", "biology", "laila saadi", "E0004"),
    ("12:30", "history", "yassine faska", "E0005")
]

tc2_schudle = [
    ("8:30", "physics", "nour jamal", "E0002"),
    ("9:30", "chemistry", "omar zaki", "E0003"),
    ("10:30", "biology", "laila saadi", "E0004"),
    ("11:30", "history", "yassine faska", "E0005"),
    ("12:30", "math", "khadija khaddiri", "E0001")
]

tc3_schudle = [
    ("8:30", "chemistry", "omar zaki", "E0003"),
    ("9:30", "biology", "laila saadi", "E0004"),
    ("10:30", "history", "yassine faska", "E0005"),
    ("11:30", "math", "khadija khaddiri", "E0001"),
    ("12:30", "physics", "nour jamal", "E0002")
]

tc4_schudle = [
    ("8:30", "biology", "laila saadi", "E0004"),
    ("9:30", "history", "yassine faska", "E0005"),
    ("10:30", "math", "khadija khaddiri", "E0001"),
    ("11:30", "physics", "nour jamal", "E0002"),
    ("12:30", "chemistry", "omar zaki", "E0003")
]

tc5_schudle = [
    ("8:30", "history", "yassine faska", "E0005"),
    ("9:30", "math", "khadija khaddiri", "E0001"),
    ("10:30", "physics", "nour jamal", "E0002"),
    ("11:30", "chemistry", "omar zaki", "E0003"),
    ("12:30", "biology", "laila saadi", "E0004")
]

DBF = connect('DataBase.db')
Cursor = DBF.cursor()
# # Create tables for students in each class
Cursor.execute("CREATE TABLE IF NOT EXISTS tc1_students (studentID TEXT, studentName TEXT, entringPermession BOOLEAN DEFAULT 1)")
Cursor.execute("CREATE TABLE IF NOT EXISTS tc2_students (studentID TEXT, studentName TEXT, entringPermession BOOLEAN DEFAULT 1)")
Cursor.execute("CREATE TABLE IF NOT EXISTS tc3_students (studentID TEXT, studentName TEXT, entringPermession BOOLEAN DEFAULT 1)")
Cursor.execute("CREATE TABLE IF NOT EXISTS tc4_students (studentID TEXT, studentName TEXT, entringPermession BOOLEAN DEFAULT 1)")
Cursor.execute("CREATE TABLE IF NOT EXISTS tc5_students (studentID TEXT, studentName TEXT, entringPermession BOOLEAN DEFAULT 1)")
# # Insert student data into respective tables
Cursor.executemany("INSERT INTO tc1_students VALUES (?, ?, ?)", tc1)
Cursor.executemany("INSERT INTO tc2_students VALUES (?, ?, ?)", tc2)
Cursor.executemany("INSERT INTO tc3_students VALUES (?, ?, ?)", tc3)
Cursor.executemany("INSERT INTO tc4_students VALUES (?, ?, ?)", tc4)
Cursor.executemany("INSERT INTO tc5_students VALUES (?, ?, ?)", tc5)

# # Create tables for absences in each class
Cursor.execute("CREATE TABLE IF NOT EXISTS tc1_absences (studentID TEXT, absenceDate TEXT, absenceTime TEXT)")
Cursor.execute("CREATE TABLE IF NOT EXISTS tc2_absences (studentID TEXT, absenceDate TEXT, absenceTime TEXT)")
Cursor.execute("CREATE TABLE IF NOT EXISTS tc3_absences (studentID TEXT, absenceDate TEXT, absenceTime TEXT)")
Cursor.execute("CREATE TABLE IF NOT EXISTS tc4_absences (studentID TEXT, absenceDate TEXT, absenceTime TEXT)")
Cursor.execute("CREATE TABLE IF NOT EXISTS tc5_absences (studentID TEXT, absenceDate TEXT, absenceTime TEXT)")

# # Create tables for schedules in each class
Cursor.execute("CREATE TABLE IF NOT EXISTS tc1_schedule (time TEXT, subject TEXT, teacherName TEXT, teacherID TEXT)")
Cursor.execute("CREATE TABLE IF NOT EXISTS tc2_schedule (time TEXT, subject TEXT, teacherName TEXT, teacherID TEXT)")
Cursor.execute("CREATE TABLE IF NOT EXISTS tc3_schedule (time TEXT, subject TEXT, teacherName TEXT, teacherID TEXT)")
Cursor.execute("CREATE TABLE IF NOT EXISTS tc4_schedule (time TEXT, subject TEXT, teacherName TEXT, teacherID TEXT)")
Cursor.execute("CREATE TABLE IF NOT EXISTS tc5_schedule (time TEXT, subject TEXT, teacherName TEXT, teacherID TEXT)")
# # Insert schedule data into respective tables
Cursor.executemany("INSERT INTO tc1_schedule VALUES (?, ?, ?, ?)", tc1_schudle)
Cursor.executemany("INSERT INTO tc2_schedule VALUES (?, ?, ?, ?)", tc2_schudle)
Cursor.executemany("INSERT INTO tc3_schedule VALUES (?, ?, ?, ?)", tc3_schudle)
Cursor.executemany("INSERT INTO tc4_schedule VALUES (?, ?, ?, ?)", tc4_schudle)
Cursor.executemany("INSERT INTO tc5_schedule VALUES (?, ?, ?, ?)", tc5_schudle)

DBF.commit()
DBF.close()