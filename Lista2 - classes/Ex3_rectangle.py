class Rectangle:

    def __init__(self,sideA,sideB):
        self.sideA = sideA
        self.sideB = sideB
    
    def changeSides(self,sideA,sideB):
        self.sideA = float(sideA)
        self.sideB = float(sideB)

    def returnValueSides(self):
        return f"Side A of the rectangle is: {self.sideA} cm and the Side B of the rectangle is: {self.sideB} cm"

    def perimeter(self):
        perimeter = 2*self.sideA+2*self.sideB
        return perimeter

    def area(self):
        area = self.sideA*self.sideB
        return area

# Create the object
rectangle1 = Rectangle(5,4)

# Question for the user about the sides
newSideA = input("Whats the new sideA of the Rectangle? Put in cm please: ")
newSideB = input("Whats the new sideB of the Rectangle? Put in cm please: ")

# send to the class the newSides
rectangle1.changeSides(newSideA,newSideB)

# Print the values
print(rectangle1.returnValueSides())
print(f"The perimeter of the rectangle is: {rectangle1.perimeter()} cm")
print(f"The area of the rectangle is: {rectangle1.area()} cm^2")