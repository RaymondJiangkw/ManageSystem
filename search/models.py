from django.db import models

# Create your models here.
class Lesson(models.Model):
    name = models.CharField(max_length = 51)
    teacher = models.CharField(max_length = 11)
    capacity = models.IntegerField(default = 0)
    classroom = models.CharField(max_length = 51)
    supplement = models.TextField()
    collage = models.CharField(max_length = 51)
    school = models.CharField(max_length = 51)
    lesson_id = models.CharField(max_length = 11)
    score = models.CharField(max_length = 5,default = "1.0")
    time = models.CharField(max_length = 51,default = "星期一第1节")
    weeks = models.CharField(max_length = 51,default = "第01-12周")
    def __str__(self):
        return self.name
