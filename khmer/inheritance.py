"""
inheritace {subclass = child class and superclass = parent}
"""
class Animal:
    def __init__(self,name):
        self.name = name 
    def speak(self):
        return f"{self.name} can make a sound"
class dog(Animal):
    def __init__(self,name,breed):
        super().
my_dog = dog("Buddy","gold")
