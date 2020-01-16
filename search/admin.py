from django.contrib import admin
from .models import Lesson
# Register your models here.
class LessonAdmin(admin.ModelAdmin):
    list_display = ('name','lesson_id','teacher','time')
    list_filter = ['time','weeks','collage','school']
    search_fields = ['name','teacher','collage','school','lesson_id','time','weeks']
    fieldsets = [
        ("Basic Info",{'fields':["name","lesson_id","teacher","classroom","time","weeks","collage","school"]}),
        ("Supplement",{'fields':["capacity","score","supplement"],'classes':['collapse']}),
    ]
admin.site.register(Lesson,LessonAdmin)
