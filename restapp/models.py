from django.db import models
class books (models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    
class Meta:
    db_table = "book"
# Create your models here.
