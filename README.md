# College Management System

Try to create College management system in django which is used manage the students registered in the faculty.

## Models

The system should have these database models

- `Faculty` Table With These attributes:
  - `F_id:` Faculty id
  - `F_name:` Faculty Name
- `Department` Table With These attributes:
  - `D_id:` id
  - `D_Name` Name
  - `F_id` Faculty id
- `Address` Table With These attributes
  - `A_id` Address id
  - `Gvernorate` Gvernorate
  - `City` City
  - `line_1` Address Line 1 (Required)
  - `line_2` Address Line 2 (Optional)
- `Student_Address` Table With These attributes
  - `Stu_A_id` id
  - `A_id` Address id
  - `Stu_id` Student id
- `Student` Table With These attributes
  - `Stu_id` id
  - `F_Name` First Name
  - `L_Name` Last Name
  - `F_Phone` First Phone
  - `L_Phone` Last Phone
  - `Birth_Date` Birth Date
  - `image` Student Image
- `Professor` Table With These attributes
  - `P_id` id
  - `F_id` Faculty id
  - `D_id` Department id
  - `F_name` First Name
  - `L_Name` Last Name
  - `age` Age
  - `Salary` Salary
  - `image` Student Image
- `Subjects` Table With These attributes
  - `Sub_id` id
  - `Sub_name` Name
  - `Sub_code` Code (Unique)
  - `F_id` Faculty id
- `Course` Table With These attributes
  - `C_id` id
  - `Sub_id` Sub_id
  - `Duration` Duration
  - `P_id` Professor id
- `Course_Enrolment` Table With These attributes
  - `C_E_id` id
  - `C_id` Course id
  - `Stu_id` Student id
- `Exams` Table With These attributes
  - `E_id` id
  - `C_id` Course id
  - `Date` Exam Date
  - `Time` Exam Time
  - `Duration` Exam Duration

## URLs And Pages

- `http://127.0.0.1:8000/faculty/` Page Which Will Show Faculty Info
- `http://127.0.0.1:8000/faculty/create/` Page Which Will Have html form to create faculty Or To Edit The Faculty Info.
- `http://127.0.0.1:8000/departments/` Page Which Will Show departments Info
- `http://127.0.0.1:8000/departments/create/` Page Which Will Be Used To Create Department Or Edit Department
- `http://127.0.0.1:8000/subjects/` Page Which Will Show subjects Info
- `http://127.0.0.1:8000/subjects/create/` Page Which Will Be Used To Create Subjects Or Edit Subjects
- `http://127.0.0.1:8000/courses/` Page Which Will Show courses Info
- `http://127.0.0.1:8000/courses/create/` Page Which Will Be Used To Create Courses Or Edit Courses
- `http://127.0.0.1:8000/exams/` Page Which Will Show exams Info
- `http://127.0.0.1:8000/exams/create/` Page Which Will Be Used To Create Exams Or Edit Exams
- `http://127.0.0.1:8000/students/` Page Which Will Show students Info
- `http://127.0.0.1:8000/students/create/` Page Which Will Be Used To Create Students Or Edit Students
- `http://127.0.0.1:8000/professors/` Page Which Will Show professors Info
- `http://127.0.0.1:8000/professors/create/` Page Which Will Be Used To Create Professors Or Edit Professors

- `http://127.0.0.1:8000/departments/<department_id>/` Which Will Get The id From URL and search about this Department and show it's, Info Otherwise Show 404 Page.
- `http://127.0.0.1:8000/subjects/<subject_id>/` Which Will Get The id From URL and search about this Subject and show it's Info, Otherwise Show 404 Page.
- `http://127.0.0.1:8000/courses/<course_id>/` Which Will Get The id From URL and search about this Course And It's Related Subject Info and show it's Info Otherwise Show 404 Page.
- `http://127.0.0.1:8000/students/<student_id>/` Which Will Get The id From URL and search about this Student and show it's Info, Otherwise Show 404 Page.
- `http://127.0.0.1:8000/professors/<professor_id>/` Which Will Get The id From URL and search about this Professor and show it's Info, Otherwise Show 404 Page.

##
