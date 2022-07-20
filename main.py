#a program to use classes to create a dealership that shows cars in showroom
#last modified 7/20/2022

from vehicle import Vehicle
from showroom import Showroom
from dealership import Dealership

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

  #number of cars that can be fit in each room.
  roomspace = 5

  #showrooms start with no cars in this simulation
  cars = 0

  #number of showrooms in the dealership
  num_showrooms = 3

  car1 = Vehicle(info1[0], info1[1], info1[2], info1[3], info1[4])
  car2 = Vehicle(info2[0], info2[1], info2[2], info2[3], info2[4])
  car3 = Vehicle(info3[0], info3[1], info3[2], info3[3], info3[4])
  car4 = Vehicle(info4[0], info4[1], info4[2], info4[3], info4[4])
  car5 = Vehicle(info5[0], info5[1], info5[2], info5[3], info5[4])
  car6 = Vehicle(info6[0], info6[1], info6[2], info6[3], info6[4])
  car7 = Vehicle(info7[0], info7[1], info7[2], info7[3], info7[4])

  room1 = Showroom(roomspace, cars)
  room2 = Showroom(roomspace, cars)
  room3 = Showroom(roomspace, cars)

  dealership = Dealership(num_showrooms)

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
    if choice == "1":
      car1.display()
        
    if choice == "2":
      car2.display()
    if choice == "3":
      car3.display()
    if choice == "4":
      car4.display()
    if choice == "5":
      car5.display()
    if choice == "6":
      car6.display()
    if choice == "7":
      car7.display()
    
    print("Where would you like the car to be placed?")

    i = 1
    while i < 4:
      print("We have showroom " + str(i))
      i += 1

    validroom = True
    while validroom:
      roomchoice = input("Please pick a showroom number. (Enter 0 to exit the roomchoice.)\n")

      if roomchoice == "0":
        validroom = False
        in_dealership = False
      elif roomchoice == "1":
        if room1.space == room1.cars:
          print("The room is full please pick anotherone")
        elif room1.space > room1.cars:
          print("We have enough space. We will move the car there shortly. \nWe hope you enjoy looking at the car.")
          validroom = False
      elif roomchoice == "2":
        if room2.space == room2.cars:
          print("The room is full please pick anotherone")
        elif room2.space > room2.cars:
          print("We have enough space. We will move the car there shortly. \nI hope you enjoy viewing the car.")
          validroom = False
      elif roomchoice == "3":
        if room3.space == room3.cars:
          print("The room is full please pick anotherone")
        elif room3.space > room3.cars:
          print("We have enough space. We will move the car there shortly. \nI hope you enjoy viewing the car.")
          validroom = False
      else:
        print("That was not a valid option. Please input an integer.")
    
    print("Would you like to view another car?")
    valid = True
    while valid:
      leave = input("Enter 1 to pick another car or 0 to leave.\n")
      if leave == "1":
        print("\n")
        valid = False
      elif leave == "0":
        valid = False
      else:
        print("That was not a valid input.")
    
  print("Thank you for your time at our dealership. We hope you have a wonderful day!")
    

#runs the code
if __name__ == "__main__":
  main()
