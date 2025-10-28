from django.db import models

class Pokemon(models.Model):
    name = models.CharField(max_length=100, null=False)
    type = models.CharField(max_length=40, null=False)
    weight = models.IntegerField(null=False)
    height = models.IntegerField(null=False)
    picture=models.ImageField(upload_to='pokemon_pictures/', null=True, blank=True)
    def __str__(self):
        return self.name
    
class Trainer (models.Model):
    name=models.CharField(max_length=20, null=False)
    last_name=models.CharField(max_length=20, null=False)
    years=models.IntegerField(null=False)
    level=models.IntegerField(null=False)
    datebirth=models.DateField(null=False)
    def __str__(self):
        return self.name