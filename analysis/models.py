from django.db import models

# Create your models here.

def getCurrentYear():
    from datetime import datetime
    return datetime.now().year

# First class model
class School(models.Model):
    name = models.CharField(max_length=50,null=True)
    school_code = models.CharField(max_length=8,null=True)

    def __str__(self):
        return self.name


# First class model
class Department(models.Model):
    name = models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.name


# First class model
class Year(models.Model):
    year = models.IntegerField(default=getCurrentYear())

    def __str__(self):
        return self.year


# First class model
subject_types = (('core','core'),('elective','elective'))
class Subject(models.Model):
    name = models.CharField(max_length=50,null=True)
    subjectType = models.CharField(max_length=50,null=True,choices=subject_types)
    ems = models.BooleanField(default=False)

    def __str__(self):
        return "{} ({})".format(self.name,self.subjectType)



genders = (('Male','Male'),('Female','Female'),) 
# Second class model
class Student(models.Model):
    school = models.ForeignKey(School,null=True,blank=True,on_delete=models.SET_NULL)
    department =  models.ForeignKey(Department,null=True,blank=True,on_delete=models.SET_NULL,related_name="students")
    name = models.CharField(max_length=50,null=True)
    gender = models.CharField(max_length=10,null=True,choices=genders)
    year = models.IntegerField(default=getCurrentYear())
    student_number = models.CharField(max_length=4,null=True)



    def __str__(self):
        return self.name

# Second class model
class Program(models.Model):
    name = models.CharField(max_length=50,null=True)
    department =  models.ForeignKey(Department,null=True,blank=True,on_delete=models.SET_NULL,related_name="programmes")


    def __str__(self):
        return self.name

class GradeValue(models.Model):
    grade = models.CharField(max_length=10,null=True)
    value = models.IntegerField(default=0)

    def __str__(self):
        return self.grade


# Third class model
class Grade(models.Model):
    student =  models.ForeignKey(Student,null=True,blank=True,on_delete=models.SET_NULL,related_name="grades")
    subject = models.ForeignKey(Subject,null=True,blank=True,on_delete=models.SET_NULL)
    grade = models.ForeignKey(GradeValue,null=True,blank=True,on_delete=models.SET_NULL,related_name="student_grades")
    

    def __str__(self):
        return self.student.name





