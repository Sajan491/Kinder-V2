from second.models import Post, Profile, Result, StudentId, Attendance, Attend, Food, Course, Routine, Contacts, Absentday, Notice, Presentday, SID, School, Foods, ROUTINES
from second.models import Post, Profile, Result, StudentId, Attendance, Attend, Food, Routine, Contacts, Absentday, Notice, Presentday, SID, School, Foods, ROUTINES, Assignments, Submissions, Grading
from django.contrib import admin
<< << << < HEAD
== == == =
>>>>>> > sajan

admin.site.register(StudentId)
admin.site.register(Attendance)
admin.site.register(Attend)
admin.site.register(Food)
admin.site.register(Foods)
admin.site.register(ROUTINES)
admin.site.register(Routine)
admin.site.register(Absentday)
admin.site.register(Presentday)
admin.site.register(SID)
admin.site.register(Result)
admin.site.register(School)
admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Notice)
admin.site.register(Contacts)
admin.site.register(Course)

admin.site.register(Assignments)
admin.site.register(Submissions)
admin.site.register(Grading)
# Register your models here.
