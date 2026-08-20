import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(
    page_title="Student Management System",
    page_icon="🎓",
    layout="wide"
)

# Initialize Session State for Student Records
if "students" not in st.session_state:
    st.session_state.students = []

# Title & Description
st.title("🎓 Student Management System")
st.markdown("Manage student records efficiently using the sidebar navigation.")
st.divider()

# Sidebar Navigation
st.sidebar.header("Navigation")
menu = st.sidebar.radio(
    "Select Action",
    ["View Students", "Add Student", "Search Student", "Update Student", "Delete Student"]
)

# ---------------------------------------------------------
# 1. VIEW STUDENTS
# ---------------------------------------------------------
if menu == "View Students":
    st.subheader("📋 Student Records")
    
    if not st.session_state.students:
        st.info("No student records found. Add students from the sidebar menu.")
    else:
        df = pd.DataFrame(st.session_state.students)
        
        # Display Summary Metrics
        col1, col2 = st.columns(2)
        col1.metric("Total Students", len(df))
        col2.metric("Courses Enrolled", df["Course"].nunique() if "Course" in df else 0)
        
        st.markdown("### Record List")
        st.dataframe(df, use_container_width=True, hide_index=True)

# ---------------------------------------------------------
# 2. ADD STUDENT
# ---------------------------------------------------------
elif menu == "Add Student":
    st.subheader("➕ Add New Student")
    
    with st.form("add_student_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        with col1:
            roll_no = st.text_input("Roll No")
            name = st.text_input("Full Name")
        with col2:
            course = st.text_input("Course")
            marks = st.number_input("Marks", min_value=0.0, max_value=100.0, step=0.5)
            
        submitted = st.form_submit_button("Add Student", use_container_width=True)
        
        if submitted:
            if not roll_no or not name or not course:
                st.warning("Please fill out all fields.")
            # Check for duplicate Roll No
            elif any(s["Roll No"] == roll_no for s in st.session_state.students):
                st.error(f"Student with Roll No '{roll_no}' already exists.")
            else:
                new_student = {
                    "Roll No": roll_no,
                    "Name": name,
                    "Course": course,
                    "Marks": marks
                }
                st.session_state.students.append(new_student)
                st.success(f"✅ Student '{name}' Added Successfully!")

# ---------------------------------------------------------
# 3. SEARCH STUDENT
# ---------------------------------------------------------
elif menu == "Search Student":
    st.subheader("🔍 Search Student")
    
    search_roll = st.text_input("Enter Roll No to Search")
    
    if st.button("Search", use_container_width=True):
        if search_roll:
            found = [s for s in st.session_state.students if s["Roll No"] == search_roll]
            if found:
                st.success("✅ Student Found!")
                df_found = pd.DataFrame(found)
                st.table(df_found)
            else:
                st.error("❌ Student Not Found.")
        else:
            st.warning("Please enter a Roll No.")

# ---------------------------------------------------------
# 4. UPDATE STUDENT
# ---------------------------------------------------------
elif menu == "Update Student":
    st.subheader("✏️ Update Student Record")
    
    update_roll = st.text_input("Enter Roll No to Update")
    
    if update_roll:
        student_idx = next((index for (index, d) in enumerate(st.session_state.students) if d["Roll No"] == update_roll), None)
        
        if student_idx is not None:
            current = st.session_state.students[student_idx]
            st.info(f"Updating Record for: {current['Name']}")
            
            with st.form("update_form"):
                col1, col2 = st.columns(2)
                with col1:
                    new_name = st.text_input("New Name", value=current["Name"])
                    new_course = st.text_input("New Course", value=current["Course"])
                with col2:
                    new_marks = st.number_input("New Marks", value=float(current["Marks"]), min_value=0.0, max_value=100.0, step=0.5)
                
                update_btn = st.form_submit_button("Update Record", use_container_width=True)
                
                if update_btn:
                    st.session_state.students[student_idx]["Name"] = new_name
                    st.session_state.students[student_idx]["Course"] = new_course
                    st.session_state.students[student_idx]["Marks"] = new_marks
                    st.success("✅ Student Updated Successfully!")
        else:
            st.error("❌ Student Not Found.")

# ---------------------------------------------------------
# 5. DELETE STUDENT
# ---------------------------------------------------------
elif menu == "Delete Student":
    st.subheader("🗑️ Delete Student Record")
    
    delete_roll = st.text_input("Enter Roll No to Delete")
    
    if st.button("Delete Record", type="primary", use_container_width=True):
        if delete_roll:
            initial_count = len(st.session_state.students)
            st.session_state.students = [s for s in st.session_state.students if s["Roll No"] != delete_roll]
            
            if len(st.session_state.students) < initial_count:
                st.success("✅ Student Deleted Successfully!")
            else:
                st.error("❌ Student Not Found.")
        else:
            st.warning("Please enter a Roll No.")
