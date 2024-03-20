
## 2. Автомобиль
'''
Описать класс Car
``` python
class Car:
  ...
  
car1 = Car()

а) У машины должны быть атрибуты
* "сколько бензина в баке" (gas)
* "вместимость бака" - сколько максимум вмещается бензина (capacity)
* "расход топлива на км" (gas_per_km)

б) метод "залить столько-то литров в бак"

``` python
car1.fill(5)  # залили 5 литров
```

должна учитываться вместительность бака
если пытаемся залить больше, чем вмещается, то заполняется полностью + print'ом выводится сообщение о лишних литрах

в) метод "проехать сколько-то км"

``` python
car1.ride(50)  # едем 50 км (если хватит топлива) 
```
выведите сообщение: "проехали ... километров"
в результате поездки тратится бензин
Машина едет пока хватает бензина

г) добавить атрибут с пробегом, который увеличивается в результате ride

'''

class Car:
  def __init__(self, capacity, gas_per_km):
    self.gas = 0
    self.capacity = capacity
    self.gas_per_km = gas_per_km
    self.mileage = 0
    
  def fill(self, value):
    gass_value = self.gas + value
    if (gass_value) > self.capacity:
      self.gas = self.capacity
      print(f"Залит полный бак {self.gas} литров. В бак не вместилось {gass_value - self.capacity} литров")
    else:
      self.gas = gass_value
      print(f"Залито {value} литров, в баке {self.gas} литров")
  
  def ride(self, way):
    gas_need = way * self.gas_per_km
    if gas_need > self.gas:
      thePathTraveled = self.gas/self.gas_per_km
      self.mileage += thePathTraveled
      print(f"Не удалось проехать полный путь, пройдено {round(thePathTraveled,2)} км , не хватило топлива на {round(way - thePathTraveled,2)} км")
      self.gas = 0
    else:
      self.gas -= gas_need
      self.mileage += way
      print(f"Пройдено {way} километров")
    
  
       
WW = Car(50,12.3)
WW.fill(70)
WW.ride(5)
print(WW.mileage)
WW.ride(3)
print(WW.mileage)
WW.fill(30)
WW.ride(1)
print(WW.mileage)