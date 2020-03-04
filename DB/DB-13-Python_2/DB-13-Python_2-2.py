#
# print(type(1))
# print(type([]))
# print(type(()))
# print(type({}))
#
# class Sample():
#     pass
#
#
# # Instance of Sample
# x = Sample()
#
# print(type(x))

# class Dog():
#     def __init__(self, breed, name):
#         self.breed = breed
#         self.name = name
#
#     species = "mammal"
#
#
# sam = Dog(breed='Lab', name="Sam")
# frank = Dog(breed='Huskie', name="Frank")
#
# print(sam.breed, sam.name)
# print(frank.breed, frank.name)
# print(sam.species)


class Circle():
    pi = 3.14  # Math.Pi()

    def __init__(self, radius=1):
        self.radius = radius

    def area(self):
        return Circle.pi * self.radius ** 2

    def set_radious(self, new_r):
        self.radius = new_r


myC = Circle(3)
myC.radius = 100
myC.set_radious(200)
print(myC.radius)
print(myC.area)
print(myC.area())
