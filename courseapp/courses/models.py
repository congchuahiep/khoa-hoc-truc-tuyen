from django.db import models
from django.contrib.auth.models import AbstractUser

# User Models
class User(AbstractUser):
    pass


class BaseModel(models.Model):
    '''Base model class for other model inherited'''
    activate = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    # Meta class for config model behavior
    class Meta:
        # This model can't be a table
        abstract = True


class Category(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Course(BaseModel):
    subject = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to="courses/%Y/%m", null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return self.subject
    

class Lesson(BaseModel):
    subject = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to="lesson/%Y/%m", null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject
    
    class Meta:
        # force each course can't have two same subject name
        unique_together = ('subject', 'course')
    