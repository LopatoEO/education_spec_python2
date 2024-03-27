from dataclasses import dataclass, fields
import json

@dataclass
class Car:
    kmage: int
    model: str
    generation: str 
    price: int
    year: int
    transmission: str
    body: str
    drive: str
    color: str
    volume: float
    power: int
    fuel: str

    def match(self, filter_dict):
        print(filter_dict)
        match self.__dict__:
            case {'generation': filter_dict.generation}:
                return(True)
            case _:
                return(False)
                
            
    def get_dict(self):
        return {'kmage': self.kmage, 'model': self.model, 'generation': self.generation,
                    'price':  self.price, 'year': self.year, 'transmission': self.transmission,
                    'body': self.body, 'drive': self.drive, 'color': self.color,
                    'volume': self.volume, 'power': self.power, 'fuel': self.fuel}

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
c = {'generation': 'Volkswagen Tiguan II Рестайлинг'}
d = json.load(f)
car = classFromArgs(Car, d)
finder = classFromArgs(CarFinder, c)
print(finder)
print(car)
print(car.match(finder))

