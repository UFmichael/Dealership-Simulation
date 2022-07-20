# from dealership import Dealership
# from showroom import Showroom
from vehicle import Vehicle

def main(): 
  in_dealership = True

  #vehicle information
  info1 = ["Toyota", "GR86", 2022, 27715.15, 26]
  info2 = ["Toyota", "Tacoma SR5", 2022, 28815.78, 7]
  info3 = ["Toyota", "Corolla", 2022, 20815.23, 15]
  info4 = ["Tesla", "Model X", 2022, 114997.32, 12]
  info5 = ["Honda", "Civic Type R", 2022, 22350.21, 11]
  info6 = ["Ford", "Mustang Coupe", 2022, 27473.9, 29]
  info7 = ["Hyndai", "Palisade", 2022, 33600.01, 42]

  car1 = Vehicle(info1[0], info1[1], info1[2], info1[3], info1[4])
  car2 = Vehicle(info2[0], info2[1], info2[2], info2[3], info2[4])
  car3 = Vehicle(info3[0], info3[1], info3[2], info3[3], info3[4])
  car4 = Vehicle(info4[0], info4[1], info4[2], info4[3], info4[4])
  car5 = Vehicle(info5[0], info5[1], info5[2], info5[3], info5[4])
  car6 = Vehicle(info6[0], info6[1], info6[2], info6[3], info6[4])
  car7 = Vehicle(info7[0], info7[1], info7[2], info7[3], info7[4])

  print("Hello welcome to the dealership.\nWe have multipe vehicles available for viewing today.")
  #print("Which vehicle would you be interested in viewing today?")
  
  while in_dealership:
    i = 1 
    while i < 8:
      print("We have car " + str(i))
      i += 1
    
    print("Which car would you like to look at?")
    valid = True
    while valid:
      choice = input()
      if choice == "1":
        valid = False
      elif choice == "2":
        valid = False
      elif choice == "3":
        valid = False
      elif choice == "4":
        valid = False
      elif choice == "5":
        valid = False
      elif choice == "6":
        valid = False
      elif choice == "7":
        valid = False
      else:
        print("Please pick a valid car number. (Should be an integer.)")

    print("You have selected car " + choice)
    print("Where would you like the car to be placed?")
    print("We have ")  
    

#runs the code
if __name__ == "__main__":
  main()
