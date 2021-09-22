# -*- coding: utf-8 -*-
"""
Created on Sat May 22 01:06:01 2021

@author: EngrS
"""

class Vehicle:
    """This is a parent class we are passing no arguments and have default values for
    variables such as make , model , year and weight , in order to set the values we have 
    setter methods for individual as well as collective variables"""
    
    def __init__(self):
        self.Make = "Unknown"
        self.Model = "Unknwon"
        self.Year = 0
        self.Weight = 0
        self.NeedsMaintenance = False
        self.TripSinceMaintenance = 0
    #setters 
    
    def setMake(self , myMake):
        self.Make = myMake
        
    def setModel(self , myModel):
        self.Model = myModel
        
    def setYear(self , myYear):
        self.Year = myYear
        
    def setWeight(self , myWeight):
        self.Weight = myWeight
        
    def setTrips (self , myTrips):
        self.TripSinceMaintenance = myTrips
        
    def setSpecs(self , myMake , myModel , myYear , myWeight ):
        self.Make = myMake
        self.Model = myModel
        self.Year = myYear
        self.Weight = myWeight
    
                
    

class Cars(Vehicle):
    """This is inherited class which takes all the properties of the vehicle class
    but has additional parameter isDriving which shows the driving status , the class also
    contains driving,stopping and repair methods in order to maintain the drivind status and
    maintenance status"""
    
    def __init__ (self ,isDriving = True):
       Vehicle.__init__(self)
       print("****New car has been created****")
       self.isDriving = isDriving
       
       
    def Driving(self):
        if self.isDriving == False:
           if self.NeedsMaintenance == False:
                self.isDriving = True
                print("Driving.....")
           else:
                print("Can't drive in maintenance mode")
        else:
            print("The "+self.Make+" is already in driving mode")
            
            
    def Stop(self):
        if self.isDriving == True:
            self.isDriving = False
            self.TripSinceMaintenance += 1
            
        
            if self.TripSinceMaintenance <= 100 :                
                print("\n The "+self.Make+" "+ self.Model + " trip hase now increased to "+str(self.TripSinceMaintenance))
            
            else:
                self.NeedsMaintenance = True
                print("\n The "+self.Make+" "+ self.Model + " trip hase now increased to "+str(self.TripSinceMaintenance)\
                +" ,the vehicle needs maintenance")
        else:
            print("The "+self.Make+" is already stopped")
                        
        
        
            
    def Repair(self):
        print("The vehicle is being repaired , trips will be reset to zero")
        self.isDriving = False
        self.TripSinceMaintenance = 0
        self .NeedsMaintenance = False
            
    def __str__(self):
            return ("\n The car "+ self.Make +" its model number "+ self.Model + " prduced in the year "+ str(self.Year) +" weighs "\
                + str(self.Weight) +"kg, does it need maintenance?"+ str(self.NeedsMaintenance) \
                    +" ,it has made "+str(self.TripSinceMaintenance)+ " trip(s) Since the last maintenance.")


class Planes(Vehicle):
    """This is inherited class from Vehicle which takes all the properties of the vehicle class
but has additional parameter isFlying which shows the driving status , the class also
contains Flying,Landing and repair methods in order to maintain the flight status and
maintenance status"""
    
    def __init__ (self , Flying = True):
        Vehicle.__init__(self)
        print("****New plane has been created****")
        self.isFlying = Flying
        
    def Flying (self):
        if self.isFlying == False:
            if self.NeedsMaintenance == False:
                self.isFlying = True
                print ("The plane is now in flight mode")
            else:
                print("can't fly in maintenance mode , please repair first")
        else:
            print("it is already in flight mode")
            
            
    def Landing (self):
        if self.isFlying == True :
            self.isFlying = False
            self.TripSinceMaintenance += 1
            
            if self.TripSinceMaintenance <= 100:
                print ("The flight is now landing and number of trips has increased to "+str(self.TripSinceMaintenance))
            
            else:
                self.NeedsMaintenance = True
                print("The flgiht is now landing but you can not make next trip until repair")
                
    def Repair(self):
        if self.isFlying == False:
            print("The vehicle is being repaired , trips will be reset to zero")
            self.TripSinceMaintenance = 0
            self .NeedsMaintenance = False           
    
    def __str__(self):
        return ("\n The Flight made by "+ self.Make +" model number "+ self.Model + " prduced in the year "+ str(self.Year) +" weighs "\
            + str(self.Weight) +"kg, does it need maintenance?"+ str(self.NeedsMaintenance) \
                +" ,it has made "+str(self.TripSinceMaintenance)+ " trip(s) Since the last maintenance.")
            
mycar = Cars(True)
mycar.setSpecs("Audi", "A8", 2017 , 900)
print(mycar)
mycar.setTrips(99)
mycar.Driving()
print(mycar)
mycar.Stop()

mycar2 = Cars(True)
mycar2.setSpecs("BMW", "D Class", 2019 , 1200)
print(mycar2)
mycar2.setTrips(96)
mycar2.Driving()
print(mycar2)
mycar2.Stop()

mycar3 = Cars(True)
mycar3.setSpecs("BMW", "D Class", 2019 , 1200)
print(mycar3)
mycar3.setTrips(99)
mycar3.Driving()
mycar3.Stop()
#mycar3.Stop()
mycar3.Driving()
mycar3.Stop()
print(mycar3)
mycar3.Repair()
mycar3.Driving()
mycar3.Stop()

myflight = Planes(False)

myflight.setSpecs("Boing","737 Max", 2013, 1000)
myflight.setTrips(99)
myflight.Flying()
myflight.Landing()
myflight.Flying()
print(myflight)
myflight.Landing()
myflight.Flying()
myflight.Landing()
myflight.Repair()
myflight.Flying()
myflight.Landing()
print(myflight)