class Rectangle:

    def __init__(self,sideA,sideB):
        self.sideA = sideA
        self.sideB = sideB
    
    def changeSides(self,sideA,sideB):
        self.sideA = float(sideA)
        self.sideB = float(sideB)

    def returnValueSides(self):
        return f"Side A of the floor is: {self.sideA} cm and the Side B of the floor is: {self.sideB} cm"

    def perimeter(self):
        perimeter = 2*self.sideA+2*self.sideB
        return perimeter

    def area(self):
        area = self.sideA*self.sideB
        return area



# Question for the user about the sides
sideA = input("Whats the sideA of the floor? Put in cm please: ")
sideB = input("Whats the sideB of the floor? Put in cm please: ")

# Create the object
floor = Rectangle(sideA,sideB)

# send to the class the newSides
floor.changeSides(sideA,sideB)

# Print the values
print(floor.returnValueSides())

# Baseboard quantity = perimeter
print(f"The quantity of baseboard you need is: {floor.perimeter()} cm")

# For calculate the quantity of floors, first you need to know the desired areaFloors, then, calcute.
areaFloors = input("Whats the area of the Floors that you want to buy? Put in cm^2 please: ")
print(f"The quantity of floors is: {floor.area()/float(areaFloors)}")