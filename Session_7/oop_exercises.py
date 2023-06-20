# Q1
# Create a class to represent She Codes Students. Attributes that you may want to
# include:
# - Name
# - Program attended ("Plus" or "Flash")
# - Year they attended

class SheCodesCohort:
    def __init__(self,name,program_attended,cohort_year):
        self.name = name
        self.program_attended = program_attended
        self.cohort_year = cohort_year

# Q2
# Add a __str__ method to your student class that returns a summary of the student's
# information.
    def __str__(self):
        return f"Student: {self.name}, Program: {self.program_attended}, Year: {self.cohort_year}"

student1 = SheCodesCohort("Rosie", "Plus", 2023)
# print(student1)

# Q3
# Write a class that represents a rectangle shape and has a method for each of the
# following:
# - Calculating the area.
# - Calculating the perimeter.
# - Calculating the length of the diagonal.
# - Determining whether or not the rectangle is a square
class RectangleShape:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    
    def area_calculation(self):
        return self.width * self.height
    
    def perimeter_calculation(self):
        return (self.width * 2) + (self.height * 2) 
    
    def diagonal_length(self):
        return ((self.width * 2) + (self.height * 2)) ** 0.5
    
    def square_check(self):
        return self.width == self.height

rectangle1 = RectangleShape(5,10)

# print(rectangle1.area_calculation())

# print(rectangle1.perimeter_calculation())

# print(rectangle1.diagonal_length())

# print(rectangle1.square_check())