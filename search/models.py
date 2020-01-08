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
    def __str__(self):
        return self.name
class Class_time(models.Model):
    day = models.IntegerField(default = 1)
    time = models.IntegerField(default = 1)
    system = models.IntegerField(default = 0)
    lesson = models.ForeignKey(Lesson,on_delete = models.CASCADE)
    interpretation = models.CharField(max_length = 101)
    def __str__(self):
        return "System %s, WeekDay: %s, TimeInterval: %s" % (self.get_system_id(),self.get_weekday(),self.interpretation)
    def get_weekday(self):
        return self.day;
    def get_time_interval(self):
        return self.time;
    def get_system_id(self):
        return self.system;
    #def get_time_description(self):
    #    return models.CharField"星期%s, 具体时间：%s" % (self.get_weekday(),self.interpretation)
