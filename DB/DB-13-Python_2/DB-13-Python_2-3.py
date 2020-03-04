# class Animal():
#     def __init__(self):
#         print("Animal created")
#
#     def whoAmI(self):
#         print("Animal")
#
#     def eat(self):
#         print("Eating")
#
# class Dog(Animal):
#     def __init__(self):
#         # Animal.__init__(self)
#         print("Dog created")
#     def bark(self):
#         print("woof")
#     def eat(self):
#         print("dog eating")
# # mya=Animal()
# # mya.whoAmI()
# # mya.eat()
#
# myd=Dog()
# myd.bark()
# myd.eat()

class Book():
    def __init__(self,title,author,pages):
        self.title=title
        self.author=author
        self.pages=pages
    def __str__(self):
        return "Title: {}, Author: {}, Pages: {}".format(self.title,self.author,self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print("a book is destroyed")


b=Book("Python","jajajja",200)
print(b)
print(len(b))
del b


mylist=[1,2,3]
print(mylist)