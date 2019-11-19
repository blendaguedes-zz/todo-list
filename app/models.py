from django.db import models

# Create your models here.


class Todo(models.Model):
  added_date = models.DateTimeField()
  text = models.CharField(max_length=200)
  done = models.BooleanField(default=False)
  done_date = models.DateTimeField(null=True)
