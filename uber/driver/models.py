from django.db import models

# Create your models here.
class Driver(models.Model):
    name = models.CharField(max_length =30)
    national_id = models.IntegerField(unique = True)
    driverLocation = models.ForeignKey('DriverLocation')
    car = models.ForeignKey('Car')

    def save_driver(self):
        '''Method to save a driver to the database.'''
        self.save()

    def delete_driver(self):
        '''Method to delete a driver from the database'''
        self.delete()
        
class DriverLocation(models.Model):
    longitude = models.IntegerField()
    latitude = models.IntegerField()

    def save_location(self):
        '''Method to save the driver's location '''
        self.save()

    def delete_location(self):
        '''Method to delete location of the driver'''
        self.delete()

class Car(models.Model):
    car_brand = models.CharField(max_length = 30)
    car_plate = models.CharField(max_length =10, unique= True)
    no_seats = models.IntegerField()

    def save_car(self):
        '''Method to save a car model to the database'''
        self.save()

    def delete_car(self):
        '''Method to delete a car model from the database'''
        self.delete()