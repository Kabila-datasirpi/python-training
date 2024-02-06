from django.db import models
class employee (models.Model):
    eid = models.CharField(max_length = 20)
    ename = models.CharField(max_length = 100)
    econtact = models.CharField(max_length = 50)
class Meta:
    db_table = "employee"




