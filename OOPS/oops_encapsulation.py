class Car:
    def __init__(self):
        self.__updateSoftware()
    def drive(self):
        print("driving")
    def __updateSoftware(self):  #private method
        print("updating software")

c= Car()
c.drive()