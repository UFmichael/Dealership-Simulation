# a class to manage the vehicle commands and house the vehicle information
#Last Modified: 7/19/2022
class Vehicle():
  
  #get's the brand lists
  def get_vehicle_brand():
    vehicle_brand_list = ["Toyota", "Mazda", "Mustang", "Honda"]
    return vehicle_brand_list

  #get the models after a brand is chosen
  def get_brand_models(x):
    if x == 1: #toyota
      vehicle_model_list = ["GR86", "Tacoma SR5", "Corolla"]
    elif x == 2: #mazda
      vehicle_model_list = []
    elif x == 3: #mustang
      vehicle_model_list = []
    elif x == 4: #honda
      vehicle_model_list = []
    else:
      vehicle_model_list = [0]

  #gets the model information of the vehicle chosen
  def get_vehicle_info(brand, model):
    
    #toyota
    if brand == 1:
      if model == 1:
        info = ["Toyota", "GR86", 2022, 27715.15, 26]
      elif model == 2:
        info = ["Toyota", "Tacoma SR5", 2022, 28815.78, 7]
      elif model == 3:
        info = ["Toyota", "Corolla", 2022, 20815.23, 15]
      else:
        info = [0]
    
    #Mazda
    if brand == 2:
      if model == 1:
        info = []
      elif model == 2:
        info = []
      elif model == 3:
        info = [] 
      else:
        info [0]
    
    #mustang
    if brand == 3:
      if model == 1:
        info = []
      elif model == 2:
        info = []
      elif model == 3:
        info = []
      else:
        info [0]
    
    #honda
    if brand == 4:
      if model == 1:
        info = []
      elif model == 2:
        info = []
      elif model == 3:
        info = []
      else:
        info [0]
    
    else:
      info = [0]
  
    return info 

