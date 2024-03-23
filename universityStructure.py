
import sqlite3

# Admin credentials
ADMIN_NAME = "admin"
ADMIN_PASSWORD = "admin123"

# Function to create the database and tables
def create_db():
    conn = sqlite3.connect('DBMS.db')
    c = conn.cursor()

    # Create tables
    c.execute('''CREATE TABLE IF NOT EXISTS Student (
                    ID INTEGER PRIMARY KEY,
                    Name TEXT NOT NULL,
                    Email TEXT NOT NULL,
                    Major TEXT,
                    PhoneNumbers TEXT
                )''')

    c.execute('''CREATE TABLE IF NOT EXISTS Course (
                    CourseID INTEGER PRIMARY KEY,
                    Name TEXT NOT NULL,
                    Department TEXT,
                    AvailableSeats INTEGER,
                    EnrolledStudents INTEGER,
                    CourseDescription TEXT
                )''')

    c.execute('''CREATE TABLE IF NOT EXISTS Faculty (
                    EmpId INTEGER PRIMARY KEY,
                    Name TEXT NOT NULL,
                    Department TEXT,
                    Email TEXT
                )''')

    c.execute('''CREATE TABLE IF NOT EXISTS Department (
                    DeptID INTEGER PRIMARY KEY,
                    Name TEXT NOT NULL,
                    Location TEXT
                )''')

    c.execute('''CREATE TABLE IF NOT EXISTS Student_Course (
                    StudentID INTEGER,
                    CourseID INTEGER,
                    FOREIGN KEY(StudentID) REFERENCES Student(ID),
                    FOREIGN KEY(CourseID) REFERENCES Course(CourseID),
                    PRIMARY KEY (StudentID, CourseID)
                )''')

    c.execute('''CREATE TABLE IF NOT EXISTS Faculty_Course (
                    EmployeeID INTEGER,
                    CourseID INTEGER,
                    FOREIGN KEY(EmployeeID) REFERENCES Faculty(EmpId),
                    FOREIGN KEY(CourseID) REFERENCES Course(CourseID),
                    PRIMARY KEY (EmployeeID, CourseID)
                )''')

    c.execute('''CREATE TABLE IF NOT EXISTS Department_Course (
                    DepartmentID INTEGER,
                    CourseID INTEGER,
                    FOREIGN KEY(DepartmentID) REFERENCES Department(DeptID),
                    FOREIGN KEY(CourseID) REFERENCES Course(CourseID),
                    PRIMARY KEY (DepartmentID, CourseID)
                )''')

    conn.commit()
    conn.close()

# Function to insert dummy records into tables
def insert_dummy_records():
    conn = sqlite3.connect('DBMS.db')
    c = conn.cursor()

    # Insert dummy records for all tables
    c.execute("INSERT INTO Student (Name, Email, Major, PhoneNumbers) VALUES ('John Doe', 'john@example.com', 'Computer Science', '1234567890')")
    c.execute("INSERT INTO Faculty (Name, Department, Email) VALUES ('Jane Smith', 'Mathematics', 'jane@example.com')")
    c.execute("INSERT INTO Department (Name, Location) VALUES ('Computer Science', 'Building A')")
    c.execute("INSERT INTO Course (Name, Department, AvailableSeats, EnrolledStudents, CourseDescription) VALUES ('Database Systems', 'Computer Science', 50, 0, 'Introduction to databases')")
    c.execute("INSERT INTO Student_Course (StudentID, CourseID) VALUES (1, 1)")
    c.execute("INSERT INTO Faculty_Course (EmployeeID, CourseID) VALUES (1, 1)")
    c.execute("INSERT INTO Department_Course (DepartmentID, CourseID) VALUES (1, 1)")

    conn.commit()
    conn.close()

# Function to insert records into any table
def insert_record(table_name, values):
    conn = sqlite3.connect('DBMS.db')
    c = conn.cursor()

    placeholders = ', '.join(['?'] * len(values))

    c.execute(f"INSERT INTO {table_name} VALUES ({placeholders})", values)
    

    conn.commit()
    conn.close()

# Function to delete records
def delete_record(table_name, condition):
    conn = sqlite3.connect('DBMS.db')
    c = conn.cursor()    
    c.execute(f"DELETE FROM {table_name} WHERE {condition}")        

    conn.commit()
    conn.close()

# Function to update records
def update_record(table_name, set_values, condition):
    conn = sqlite3.connect('DBMS.db')
    c = conn.cursor()    
    c.execute(f"UPDATE {table_name} SET {set_values} WHERE {condition}")        
        
    conn.commit()
    conn.close()

# Function to display records from a table
def display_records(table_name):
    conn = sqlite3.connect('DBMS.db')
    c = conn.cursor()
    
    c.execute(f"SELECT * FROM {table_name}")
    records = c.fetchall()       

    if not records:
        print("No records found.")
    else:
        print(f"Records from {table_name}:")
        for record in records:
            print(record)

    conn.close()

# Admin login
def admin_login():
    name = input("Enter admin name: ")
    password = input("Enter admin password: ")
    if name == ADMIN_NAME and password == ADMIN_PASSWORD:
        return True
    else:
        print("Invalid credentials. Access denied.")
        return False


# Admin menu
def admin_menu():
    while True:
        print("\nAdmin Menu:")
        print("1. Create database DBMS")
        print("2. Insert dummy records")
        print("3. Insert records")
        print("4. Delete records")
        print("5. Update records")
        print("6. Display records from a table")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_db()
            print("Database DBMS created.")
        elif choice == "2":
            insert_dummy_records()
            print("Dummy records inserted successfully.")
        elif choice == "3":
            table_name = input("Enter table name to insert into: ")
            values_str = input("Enter values separated by comma: ")
            values = tuple(values_str.split(', '))
            insert_record(table_name, values)
            print("Record inserted successfully.")
        elif choice == "4":
            table_name = input("Enter table name to delete from: ")
            condition = input("Enter condition for deletion: ")
            delete_record(table_name, condition)
            print("Record(s) deleted successfully.")
        elif choice == "5":
            table_name = input("Enter table name to update: ")
            set_values = input("Enter set values: ")
            condition = input("Enter condition: ")
            update_record(table_name, set_values, condition)
            print("Record(s) updated successfully.")
        elif choice == "6":
            table_name = input("Enter table name to display records from: ")
            display_records(table_name)
        elif choice == "7":
            break

# Function to display records from a table
def display_records(table_name):
    conn = sqlite3.connect('DBMS.db')
    c = conn.cursor()

    c.execute(f"SELECT * FROM {table_name}")
    records = c.fetchall()

    if not records:
        print("No records found.")
    else:
        print(f"Records from {table_name}:")
        for record in records:
            print(record)

    conn.close()


# Function to view student details
def view_student_details(student_id):
    conn = sqlite3.connect('DBMS.db')
    c = conn.cursor()

    c.execute("SELECT * FROM Student WHERE ID = ?", (student_id,))
    student_data = c.fetchone()
    if student_data:
        print("Student Details:")
        print("ID:", student_data[0])
        print("Name:", student_data[1])
        print("Email:", student_data[2])
        print("Major:", student_data[3])
        print("Phone Numbers:", student_data[4])
    else:
        print("Student not found.")

    conn.close()

# Function to view student course details
def view_student_course_details(student_id):
    conn = sqlite3.connect('DBMS.db')
    c = conn.cursor()

    c.execute('''SELECT Course.*
                 FROM Course
                 JOIN Student_Course ON Course.CourseID = Student_Course.CourseID
                 WHERE Student_Course.StudentID = ?''', (student_id,))
    course_data = c.fetchall()
    if course_data:
        print("Courses Enrolled:")
        for course in course_data:
            print("CourseID:", course[0])
            print("Name:", course[1])
            print("Department:", course[2])
            print("Available Seats:", course[3])
            print("Enrolled Students:", course[4])
            print("Course Description:", course[5])
            print()
    else:
        print("No courses enrolled.")

    conn.close()

# Function to view faculty details
# Function to view faculty details
def view_faculty_details(faculty_id):
    conn = sqlite3.connect('DBMS.db')
    c = conn.cursor()

    c.execute("SELECT * FROM Faculty WHERE EmpId = ?", (faculty_id,))
    faculty_data = c.fetchone()
    if faculty_data:
        print("Faculty Details:")
        print("EmpId:", faculty_data[0])
        print("Name:", faculty_data[1])
        print("Department:", faculty_data[2])
        print("Email:", faculty_data[3])
    else:
        print("Faculty not found.")

    conn.close()

# Function to view faculty course details
def view_faculty_course_details(faculty_id):
    conn = sqlite3.connect('DBMS.db')
    c = conn.cursor()

    c.execute('''SELECT Course.*
                 FROM Course
                 JOIN Faculty_Course ON Course.CourseID = Faculty_Course.CourseID
                 WHERE Faculty_Course.EmployeeID = ?''', (faculty_id,))
    course_data = c.fetchall()
    if course_data:
        print("Courses Teaching:")
        for course in course_data:
            print("CourseID:", course[0])
            print("Name:", course[1])
            print("Department:", course[2])
            print("Available Seats:", course[3])
            print("Enrolled Students:", course[4])
            print("Course Description:", course[5])
            print()
    else:
        print("No courses being taught.")

    conn.close()

# User login function
def user_login(user_type):
    while True:
        user_id = input(f"Enter {user_type} ID to login or type 'exit' to go back to main menu: ")
        if user_id.lower() == 'exit':
            break
        else:
            if user_type == 'Student':
                view_student_details(int(user_id))
                view_student_course_details(int(user_id))
            elif user_type == 'Faculty':
                view_faculty_details(int(user_id))
                view_faculty_course_details(int(user_id))
            else:
                print("Invalid user type.")
                break

# Main function
def main():
    while True:
        print("\nMain Menu:")
        print("1. Admin Login")
        print("2. Student Login")
        print("3. Faculty Login")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            if admin_login():
                admin_menu()
        elif choice == "2":
            user_login('Student')
        elif choice == "3":
            user_login('Faculty')
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
