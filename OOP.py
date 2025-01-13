## class

class Microwave:
    def __init__(self, brand: str, power_rating: str) -> None:
        self.brand = brand
        self.power_rating = power_rating


Smeg = Microwave(brand= 'Smeg', power_rating= 'B')
print(Smeg.brand)
print(Smeg.power_rating)


bosch = Microwave(brand='Bosch', power_rating='C')
print(bosch.brand)
print(bosch.power_rating)



## Methods

class Microwave:
    def __init__(self, brand: str, power_rating: str) -> None:
        self.brand = brand
        self.power_rating = power_rating
        self.turned_on: bool = False
    
    def turn_on(self) -> None:
        if self.turned_on:
            print(f'Micrwave ({self.brand}) is already turned on.')
        else:
            self.turned_on = True
            print(f'Micrwave ({self.brand}) is now turned on.')
    

    def turn_off(self) -> None:
        if self.turned_on:
            self.turned_on =False
            print(f'Microwave ({self.brand}) is now turned off.')
        else:
            print(f'Micrwave ({self.brand}) is already turned off.')
    
    def run(self, seconds: int) -> None:
    
        if self.turned_on:
            print(f'Running ({self.brand}) for {seconds} seconds')
        else:
            print(f'A mystical force whispers: "Turn on your microwave bitch...')

    def __add__(self, other):
        return f'{self.brand} + {other.brand}'
    
    def __mul__(self, other):
        return f'{self.brand} * {other.brand}'
    
    def __str__(self) -> str:
        return f'{self.brand} (Rating: {self.power_rating})'

Smeg = Microwave(brand= 'Smeg', power_rating= 'B')
bosch = Microwave(brand= 'Bosch', power_rating= 'C')

## Dunder methods

print (Smeg + bosch)
print (Smeg * bosch)
print(Smeg)
print(bosch)
