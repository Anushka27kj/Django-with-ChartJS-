from django.db import models

# Create your models here.
class club(models.Model):
    name = models.CharField(max_length=50, help_text="Enter name: ")
    money = models.FloatField(help_text="Enter money: ")

    def __str__(self):
        return self.name + '--' + str(self.money)
    