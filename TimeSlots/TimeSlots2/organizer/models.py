from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField('Title', max_length=180)
    description = models.TextField('Description', max_length=256)

    def str(self):
        return self.title
