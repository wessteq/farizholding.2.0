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


class Enrollment(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    course_time = models.CharField(max_length=100)
    course_day = models.CharField(max_length=123)
    course_duration = models.CharField(max_length=123)
    is_teens = models.BooleanField()
    price = models.DecimalField(max_digits=12,decimal_places=2,default=0.00)
    status = models.PositiveIntegerField(
        choices= (
            (1,'recruitment is open'),
            (2,'recruitment is closed'),
            (3,'recruitment is soon')

                 ),
        default = 3
    )
    create_date = models.DateField(auto_now_add=True)



    class Meta:
       verbose_name = 'Course '
       verbose_name_plural = 'Courses'

    def __str__(self):
            return str(self.course)