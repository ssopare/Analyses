from django.shortcuts import render
from .models import *

# Create your views here.
def get_with_gender(criterion):
    students = Student.objects.all()
    objects = [student for student in students if (student.gender).lower() == criterion.lower()]
    return  objects

def index(request):
    args = {'students':get_with_gender("feMALE")}
    students = Student.objects.all().order_by('id')
    checkGrade = Grade.objects.all().order_by('-id')

    subject = Subject.objects.all()
    grade = Grade.objects.distinct().values('grade__grade')

    #studentAggregate = Grade.objects.all()
    context = {
        'args':args,
        'students':students,
        'checkGrade':checkGrade,
        
        'subject':subject,
        'grade':grade,

        #'studentAggregate':studentAggregate
    
    }
    return render(request,'analysis/index.html',context)


from django.db.models import Count, Q, Sum


# core_data = Grade.objects.filter(subject__subjectType="core").aggregate(
# total_a1_current_year = Count(
#             "grade",
#             filter=Q(year=2022)& Q(grade__grade="A1"
#         ),
# total_b2_current_year = Count(
#             "grade",
#             filter=Q(year=2022)& Q(grade__grade="B2"
#         ),
# )

# total_a1_current_year = core_data.get("total_a1_current_year")
# total_b2_current_year = core_data.get("total_b2_current_year")