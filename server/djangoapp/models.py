from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class CarModel(models.Model):
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('HATCHBACK', 'Hatchback'),
    ]

    # One car make can have multiple car models.
    car_make = models.ForeignKey(
        CarMake,
        on_delete=models.CASCADE,
        related_name='car_models'
    )

    # ID of the dealership associated with the car.
    dealer_id = models.IntegerField(default=1)

    name = models.CharField(max_length=100)

    type = models.CharField(
        max_length=10,
        choices=CAR_TYPES,
        default='SUV'
    )

    year = models.IntegerField(
        default=2023,
        validators=[
            MaxValueValidator(2023),
            MinValueValidator(2015),
        ]
    )

    def __str__(self):
        return f"{self.car_make.name} - {self.name}"
