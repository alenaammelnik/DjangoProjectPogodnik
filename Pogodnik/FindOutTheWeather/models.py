from django.db import models

class City (models.Model):
    name = models.CharField(max_length=100)

    def __str__(self): 
        return self.name

class Temperature(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    date = models.DateTimeField()
    value = models.DecimalField(max_digits= 5, decimal_places= 2)

    def __str__ (self):
        return f"{self.city.name} - {self.date}"
