# from dealership import Dealership
# from showroom import Showroom
from vehicle import Vehicle

in_dealership = True
valid_brand = True

print("Hello welcome to the dealership.\nWe have multipe vehicles available for viewing today.")
print("Which brand of vehicle would you be interested in viewing today?")
print("We have the following brands in stock today.")

while in_dealership:
  brand_list = Vehicle.get_vehicle_brand()
  
  while valid_brand:
    i = 1
    for x in brand_list:
      print(str(i)+". "+str(x))
      i += 1
    brand_num = int(input("Please enter a brand number.\n"))
    if brand_num == 1:
      valid_brand = False
    elif brand_num == 2:
      valid_brand = False
    elif brand_num == 3:
      valid_brand = False
    elif brand_num == 4:
      valid_brand = False
    else:
      print("It seems we don't have a brand of that number.\nPlease input a number corresponding to the brands we have.\n")
