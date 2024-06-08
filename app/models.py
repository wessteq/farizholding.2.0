from django.db import models

class FAQ(models.Model):
    question = models.CharField(max_length=300)
    answer = models.CharField(max_length=300)
    def __str__(self):
        return self.question

class Course(models.Model):
    title = models.CharField(max_length=333)
    description = models.TextField()
    logo = models.ImageField(upload_to='images/course')
    def __str__(self):
        return self.title
class Meta:
    verbose_name = 'Course on site'
    vervbose_name_plural = 'Courses on site'



