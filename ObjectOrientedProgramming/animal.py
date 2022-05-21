import animal_type


class Animal:
    def __init__(self, animal):
        self.animal = animal

    def move(self):
        print(self.animal + " moved")

