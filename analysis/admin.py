from django.contrib import admin
from .models import *

from import_export.admin import ImportExportModelAdmin


class GradeInline(admin.TabularInline):
    model = Grade
    extra = 1

class StudentAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    model = Student
    list_display = ['name', 'gender','department']
    inlines = [ GradeInline,]

class GradeAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['student', 'subject', 'grade']
    #model = Grade

# Register your models here.
admin.site.register(Department)
admin.site.register(Year)
admin.site.register(Student,StudentAdmin,)

#admin.site.register(Grade, GradeAdmin)

admin.site.register(Subject)
admin.site.register(Program)
admin.site.register(GradeValue)
admin.site.register(School)

admin.site.register(Grade, GradeAdmin)

