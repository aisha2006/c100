class Car(object):
    def __init__(self,company,speedLimit,hp,model,color):
        self.company = company
        self.speedLimit = speedLimit
        self.hp = hp
        self.model = model
        self.color = color

    def start(self):
        print("The car has started")
    def stop(self):
        print("The car has stopped")
    def reverse(self):
        print("The car is going backwards")
    def changeGear(self,gearType):
        print("the car is going in " + gearType + " gear")    
    def accelerate(self,acc):
        print("the car has accelerating with "+ acc + "speed")
    
audi=Car("Audi",200,100,"a6","black")
audi.start()
audi.stop()
audi.changeGear("5")