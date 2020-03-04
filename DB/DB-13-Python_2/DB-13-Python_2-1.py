# x = 25
#
#
# def func():
#     x = 50
#     return x
#
#
# # print(x)
# # print(func())
# func()
# print(x)

# # LOCAL
# lambda x: x ** 2
#
# name = "This is a global name!"
#
#
# def greet():
#     name = "Sammy"
#
#     def hello():
#         print("hello " + name)
#
#     hello()
#
#
# greet()
# print(name)

x = 50


def func():
    global x
    x = 1000
    # print("x is: ", x)
    # x = 1000
    # print("local x changed to: ", x)


print("before function call, x is:", x)
func()
print(x)
