# Add Student

students = []

def add_student():
  roll_no = input("Enter Roll No: ")
  name = input("Enter Name: ")
  course = input("Enter Course: ")
  marks = input("Enter Marks: ")
  
  student = {
  "Roll No": roll_no,
  "Name": name,
  "Course": course,
  "Marks": marks}
  
  students.append(student)
  print("✅ Student Added Successfully")

def view_students():
  
  if not students:
    print("No student records found.")
    return
    
  print("\n--- Student Records ---")
    
  for student in students:
    print(f"Roll No : {student['Roll No']}")
    print(f"Name : {student['Name']}")
    print(f"Course : {student['Course']}")
    print(f"Marks : {student['Marks']}")


# Search Student

def search_student():
  roll_no = input("Enter Roll No to Search: ")

  for student in students:
    if student["Roll No"] == roll_no:
      print("\nStudent Found")
      print(student)
      return
      
  print("❌ Student Not Found")



def update_student():
  roll_no = input("Enter Roll No to Update: ")

  for student in students:
    if student["Roll No"] == roll_no:
      student["Name"] = input("Enter New Name: ")
      student["Course"] = input("Enter New Course: ")
      student["Marks"] = input("Enter New Marks: ")
      print("✅ Student Updated Successfully")
      return
      
  print("❌ Student Not Found")



# Delete Student

def delete_student():
  roll_no = input("Enter Roll No to Delete: ")
  
  for student in students:
    if student["Roll No"] == roll_no:
      students.remove(student)
      print("✅ Student Deleted Successfully")
      return
      
  print("❌ Student Not Found")
