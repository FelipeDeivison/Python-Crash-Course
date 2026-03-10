def car_infos(fabricante, modelo, **outras):
    car = {
        'fabricante': fabricante,
        'modelo': modelo,
    }

    car.update(outras)
    return car

print(car_infos('sabaru', 'outback', cor ='Blue', ano='1999'))

