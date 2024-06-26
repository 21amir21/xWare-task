from django.db import models


class Faculty(models.Model):
    F_name = models.CharField(max_length=255)

    def __str__(self):
        return self.F_name


class Department(models.Model):
    D_name = models.CharField(max_length=255)
    F_id = models.ForeignKey(Faculty, on_delete=models.PROTECT)


class Address(models.Model):
    Gvernorate = models.CharField(max_length=255)
    City = models.CharField(max_length=255)
    line_1 = models.CharField(max_length=255)
    line_2 = models.CharField(max_length=255, blank=True)  # to make it optional


class Student(models.Model):
    F_Name = models.CharField(max_length=255)
    L_Name = models.CharField(max_length=255)
    F_Phone = models.CharField(max_length=255)
    L_Phone = models.CharField(max_length=255)
    Birth_Date = models.DateField()
    image = models.ImageField()


class Student_Address(models.Model):
    A_id = models.ForeignKey(Address, on_delete=models.PROTECT)
    Stu_id = models.ForeignKey(Student, on_delete=models.PROTECT)


class Professor(models.Model):
    F_id = models.ForeignKey(Faculty, on_delete=models.PROTECT)
    D_id = models.ForeignKey(Department, on_delete=models.PROTECT)
    F_Name = models.CharField(max_length=255)
    L_Name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    Salary = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField()


class Subjects(models.Model):
    Sub_name = models.CharField(max_length=255)
    Sub_code = models.CharField(max_length=255, unique=True)  # to make it unique
    F_id = models.ForeignKey(Faculty, on_delete=models.PROTECT)


class Course(models.Model):
    Sub_id = models.ForeignKey(Subjects, on_delete=models.PROTECT)
    Duration = models.TimeField()
    P_id = models.ForeignKey(Professor, on_delete=models.PROTECT)


class Course_Enrolment(models.Model):
    C_id = models.ForeignKey(Course, on_delete=models.PROTECT)
    Stu_id = models.ForeignKey(Student, on_delete=models.PROTECT)


class Exams(models.Model):
    C_id = models.ForeignKey(Course, on_delete=models.PROTECT)
    Date = models.DateField()
    Time = models.TimeField()
    Duration = models.DurationField()
