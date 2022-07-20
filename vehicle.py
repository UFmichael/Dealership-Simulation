# a class to manage the vehicle commands and house the vehicle information
#Last Modified: 7/20/2022
class Vehicle():
  def __init__(self, brand, model, year, price, mileage):
    self.brand = brand
    self.model = model
    self.year = year
    self.price = price
    self.mileage = mileage

  def display(self): 
    print("The brand is a "+str(self.brand))
    print("The model is "+str(self.model))
    print("The year is "+str(self.year))
    print("The price is $"+str(self.price))
    print("The mileage is "+str(self.mileage)+" miles")
