class Rectangle:
    """Represents a rectangle with a given width and height.
    
    Attributes:
    width (float): The width of the rectangle.
    height (float): The height of the rectangle.
    area (float): The computed area of the rectangle
    """
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive numbers")

        self.width = width
        self.height = height
        self.area = self.calculate_area()
        
    def calculate_area(self):
        """
        Calculates the area of the rectangle
        
        returns:
        float: The area of the rectangle
        """
        return self.width * self.height
    
    def __str__(self):
        """
        Returns:
        str: A formatted string showing the dimensions and area
        """
        return f'The rectangle with width {self.width}m and height {self.height}m has an area of {self.area}m²'
    
def display_values(*objs):
    """
    DIsplays the string representation of multiple objects
    args:
    *objs: A variable numbers of objects to display
    """
    for obj in objs:
        print(obj)
    
rectangle_1 = Rectangle(10, 15)
rectangle_2 = Rectangle(5, 20)

display_values(rectangle_1, rectangle_2)