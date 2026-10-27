from .models import CarMake, CarModel


def initiate():
    car_make_data = [
        {
            "name": "NISSAN",
            "description": "Great cars. Japanese technology",
        },
        {
            "name": "Mercedes",
            "description": "Great cars. German technology",
        },
        {
            "name": "Audi",
            "description": "Great cars. German technology",
        },
        {
            "name": "Kia",
            "description": "Great cars. Korean technology",
        },
        {
            "name": "Toyota",
            "description": "Great cars. Japanese technology",
        },
    ]

    # Create makes and retain their database objects.
    car_make_instances = {}

    for data in car_make_data:
        make, created = CarMake.objects.get_or_create(
            name=data["name"],
            defaults={
                "description": data["description"],
            }
        )

        car_make_instances[data["name"]] = make

    # Model name, type, year, associated make.
    car_model_data = [
        ("Pathfinder", "SUV", 2023, "NISSAN"),
        ("Qashqai", "SUV", 2023, "NISSAN"),
        ("XTRAIL", "SUV", 2023, "NISSAN"),

        ("A-Class", "SUV", 2023, "Mercedes"),
        ("C-Class", "SUV", 2023, "Mercedes"),
        ("E-Class", "SUV", 2023, "Mercedes"),

        ("A4", "SUV", 2023, "Audi"),
        ("A5", "SUV", 2023, "Audi"),
        ("A6", "SUV", 2023, "Audi"),

        ("Sorrento", "SUV", 2023, "Kia"),
        ("Carnival", "SUV", 2023, "Kia"),
        ("Cerato", "SEDAN", 2023, "Kia"),

        ("Corolla", "SEDAN", 2023, "Toyota"),
        ("Camry", "SEDAN", 2023, "Toyota"),
        ("Kluger", "SUV", 2023, "Toyota"),
    ]

    for name, car_type, year, make_name in car_model_data:
        CarModel.objects.get_or_create(
            name=name,
            car_make=car_make_instances[make_name],
            defaults={
                "type": car_type,
                "year": year,
                "dealer_id": 1,
            }
        )

    print("Car makes and models populated successfully.")