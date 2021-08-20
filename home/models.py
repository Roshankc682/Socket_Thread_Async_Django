from django.db import models


class Student(models.Model):
    student_name = models.CharField(max_length=128)
    SN = models.CharField(max_length=300)
    student_email = models.EmailField(max_length=60)
    address = models.CharField(max_length=128)
    age = models.IntegerField()

    # This will return the email in template file
    def __str__(self):
        return self.student_name