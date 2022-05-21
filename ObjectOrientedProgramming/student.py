import animal
import animal_type


class Student(animal.Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super(animal_type.HUMAN)
