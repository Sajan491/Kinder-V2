from django.contrib import admin
from second.models import Post, Tutorial, Profile, Result, StudentId, Attendance, Attend, Food, Course, Routine, Contacts, Absentday, Notice, Presentday, SID, School,Foods,ROUTINES

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
admin.site.register(Tutorial)

# Register your models here.
