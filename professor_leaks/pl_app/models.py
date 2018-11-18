from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Professor(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    college = models.ForeignKey(
        'College',
        on_delete=models.CASCADE
    )
    models.CharField(max_length=50)
    DEPT_CHOICES = (
        ('CSE', 'Computer Science'),
        ('MKT', 'Marketing'),
        ('COMM', 'Communication')
    )
    dept = models.CharField(
        max_length=30,
        choices=DEPT_CHOICES
    )

    def __str__(self):
        return self.fname + ' ' + self.lname

class College(models.Model):
    c_name = models.CharField(max_length=100)
    STATE_CHOICES = (
        ('CA', 'California'),
        ('GA', 'Georgia'),
        ('WA', 'Washinton')
    )
    state = models.CharField(
        max_length=30,
        choices=STATE_CHOICES,
        default='CA'
        )
    def __str__(self):
        return self.c_name

class Comment(models.Model):
    post = models.ForeignKey('Professor', on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    rate = models.IntegerField(
        validators=[MaxValueValidator(5), MinValueValidator(1)]
    )
