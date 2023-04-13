#Ramos, Jarren Leigh Midterm Exam Problem 1
import math

class Circle:
  def __init__(self, radius):
      self.radius = radius
      self.pi = math.pi
  def area(self):
      return self.pi * (self.radius ** 2)
  def perimeter(self):
      return 2 * self.pi * self.radius
  def display(self):
      print("The area of the circle is", self.area())
      print("The perimeter of the circle is", self.perimeter())

wheel = Circle(float(input("Enter the radius of the circle: ")))
wheel.display()

