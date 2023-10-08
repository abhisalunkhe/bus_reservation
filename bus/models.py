from django.db import models

# Create your models here.
class Bus(models.Model):
	name = models.CharField(max_length=100)
	image = models.ImageField(upload_to = 'Buses')
	route = models.CharField(max_length=100)
	distance = models.IntegerField()
	duration = models.CharField(max_length=100)
	bus_type = models.CharField(max_length=100)
	available_seats = models.IntegerField()

	class Meta:
		verbose_name_plural = 'Buses'

	def __str__(self):
		return self.name

class Reservation(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    adults = models.PositiveIntegerField()
    childrens = models.PositiveIntegerField()
    total_fare = models.DecimalField(max_digits=10, decimal_places=2)
    bus_name = models.CharField(max_length=100)
    route = models.CharField(max_length=100)
    bus_type = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)

    class Meta:
    	verbose_name_plural = 'Reservations'

    def __str__(self):
    	return self.email


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    class Meta:
        verbose_name_plural = 'Contacts'
        
    def __str__(self):
        return self.name