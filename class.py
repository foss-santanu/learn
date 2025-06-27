from math import pi

## Exception class for unknown shapes
class UnknownShapeException(Exception): 
    __name__ = "UnknownShapeException"
    __message__ = None  ## This is class attribute
    
    def __init__(self, message="Exception raised", *args):
        super().__init__(*args)
        self.__message__ = message
        
    def __str__(self):
        return self.__name__+": "+self.__message__
    
## Class structure to work with shapes
class Shape: 
    __name__ = None ## This is class attribute
    
    def __init__(self, **dimensions):
        self.__name__ = "Unknown"
        self.__set_dimension__(**dimensions)
        
    def __set_dimension__(self, **dimensions): 
        raise UnknownShapeException("No shape defined")
    
    def circumference(self): 
        raise UnknownShapeException("No shape defined")
    
    def area(self): 
        raise UnknownShapeException("No shape defined")
    
    def canContain(self, shape): 
        area1 = self.area()
        area2 = shape.area()
        if area1 > area2: 
            return True
        else: 
            return False
        
class Circle(Shape): 
    __radius__ = None ## This is class attribute
    
    def __init__(self, **dimensions):
        self.__name__ = "Circle"
        dimWithDefault = {"radius": 0} | dimensions
        self.__set_dimension__(**dimWithDefault)
        
    def __set_dimension__(self, **dimensions): 
        self.__radius__ = dimensions.get("radius")
        
    def circumference(self):
        return 2*pi*self.__radius__
    
    def area(self):
        return pi*self.__radius__**2
    
    def __str__(self):
        return f"{self.__name__} with radius {self.__radius__}"
    
class Rectangle(Shape): 
    __side_a__ = None ## This is class attribute
    __side_b__ = None ## This is class attribute
    
    def __init__(self, **dimensions):
        self.__name__ = "Rectangle"
        dimWithDefault = {"side_a": 0, "side_b": 0} | dimensions
        self.__set_dimension__(**dimWithDefault)
        
    def __set_dimension__(self, **dimensions): 
        self.__side_a__ = dimensions.get("side_a")
        self.__side_b__ = dimensions.get("side_b")
        
    def circumference(self):
        return (2*self.__side_a__ + 2*self.__side_b__)
    
    def area(self):
        return self.__side_a__*self.__side_b__
    
    def __str__(self):
        return f"{self.__name__} with a={self.__side_a__} and b={self.__side_b__}"
    

## Code block to initialize and test the classes
try:
    circle = Circle()
    print(circle)
    
    rect = Rectangle()
    print(rect)
    print(rect.canContain(circle))
    
    rect2 = Rectangle(side_a=3,side_b=5)
    print(rect2)
    
    circle2 = Circle(radius=2)
    print(circle2)
    print(f"area={circle2.area()}")
    
    print(f"Can circle2 contain rect? {circle2.canContain(rect)}")
    print(rect)
    ## Check for class attributes
    print(f"Rectangle class attribute a={Rectangle.__side_a__}, b={Rectangle.__side_b__}")
    
    any = Shape()
    print(any)
except UnknownShapeException as e: 
    print(e)