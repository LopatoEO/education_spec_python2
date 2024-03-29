from collections.abc import Iterable
from dataclasses import dataclass, fields
import json


class Car:
    def __init__(self, kmage=None, model=None, generation=None, price=None, 
        year=None, transmission=None, body=None, drive=None, color=None, volume=None,
        power=None, fuel=None,) -> None:
        if kmage != None:
            self.kmage = kmage
        if model != None:
            self.model = model
        if generation != None:
            self.generation = generation
        if price != None:
            self.price = price
        if model != None:
            self.model = model
        if model != None:
            self.model = model
        if model != None:
            self.model = model
        self.model = model
        self.generation = generation
        self.price = price
        self.year = year
        self.transmission = transmission
        self.body = body
        self.drive = drive
        self.color = color
        self.volume = volume
        self.power = power
        self.fuel = fuel

    def match(self, filter_dict):
        match self:
            case ("Tom" | "Tomas" as kmage, 37 | 38 as model): 
                return(True)
            case _:
                return(False)
                

@dataclass
class CarFinder:
    kmage: int = None
    model: str = None
    generation: str = None
    price: int = None
    year: int = None
    transmission: str = None
    body: str = None
    drive: str = None
    color: str = None
    volume: float = None
    power: int = None
    fuel: str = None     


        

def classFromArgs(className, argDict):
    fieldSet = {f.name for f in fields(className) if f.init}
    filteredArgDict = {k : v for k, v in argDict.items() if k in fieldSet}
    return className(**filteredArgDict)

f = open('car_base.json', encoding='utf-8')
c = {'generation': 'Volkswagen Tiguan II Рестайлинг', 'kmage': 0}
d = json.load(f)
car = classFromArgs(Car, d)
finder = classFromArgs(CarFinder, c)
print(finder)
print(car)
print(car.match(finder))

