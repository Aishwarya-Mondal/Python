#private attribute

class Car:
    __maxspeed = 0
    __name = ""
    def __init(self):
        self.__maxspeed = 200
        self.__name ="supercar"
    def drive(self):
        print("driving")
        print(self.__maxspeed)
    def setspeed(self,speed):
        self.__maxspeed= speed
c = Car()
c.setspeed(120)
c.__maxspeed= 200
c.drive()
