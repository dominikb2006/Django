# s="GLOBAL VAR"
# def func():
#     s=50
#     print(s)
#     # print(locals())
#     print(globals()['s'])
#     return 1
# func()
# print(s)


# def hello(name="Dominik"):
#     return "hello "+name
#
# print(hello())
#
# mynewgreet = hello
#
# print(mynewgreet())


# def hello(name="Dominik"):
#     print("FUNKCJA HELLO() ZOSTALA URUCHOMIONA")
#
#     def greet():
#         return "TEN STRING JEST WEWNATRZ GREET()"
#
#     def welcome():
#         return "TEN STRIN JEST WEWNATRZ WELCOME()"
#
#     # print(greet())
#     # print(welcome())
#     # print("KONIEC HELLO()")
#     if name == "Dominik":
#         return greet
#     else:
#         return welcome
#
#
# x = hello()
# print(x())


# def hello():
#     return "Hi Dominik!"
#
#
# def other(func):
#     print("HELLO")
#     print(func)
#
#
# other(hello())


def new_decorator(func):
    def wrap_func():
        print("KODUJ TUTJA PRZED EXECUTION")
        func()
        print("FUNC() ZOSTALA WYWOLANA")

    return wrap_func


@new_decorator
def func_needs_decorator():
    print("TA FUNKCJA POTRZEBUJE DEKORATORA")

#func_needs_decorator = new_decorator(func_needs_decorator)

func_needs_decorator()
