# from abc import abstractmethod, ABC
#
#
# class Scratcher(ABC):
#     @staticmethod
#     @abstractmethod
#     def scratch():
#         pass
#
#
# class Animal(ABC):
#     def __init__(self, name, age, color):
#         # print('__init__ from animal was called!')
#         self._name = name
#         self.age = age
#         self.color = color
#
#     @property
#     def name(self):
#         return self._name
#
#     @name.setter
#     def name(self, new_value):
#         self._name = new_value
#
#     @staticmethod
#     @abstractmethod
#     def speak():
#         pass
#
#
# class Cat(Animal, Scratcher):
#     @staticmethod
#     def speak():
#         print('Miau, miau!')
#
#     @staticmethod
#     def scratch():
#         print(f'You have been scratched by a cat.')
#
#
# class Dog(Animal):
#     @staticmethod
#     def speak():
#         print('Ham, ham!')
#
#
# class Lion(Animal, Scratcher):
#     @staticmethod
#     def speak():
#         print('I have no idea :D')
#
#     @staticmethod
#     def scratch():
#         print(f'You have been scratched by a lion.')
#
#
# class Tiger(Animal, Scratcher):
#     @staticmethod
#     def speak():
#         print('I have no idea 2.')
#
#     @staticmethod
#     def scratch():
#         print(f'You have been scratched by a tiger.')
#
#
# # cat_1 = Cat('Julia', 12, 'white')
# # cat_1.speak()
# # # print(type(cat_1))
# #
# # cat_2 = Cat('Cat #2', 25, 'black')
# # cat_2.speak()
# # # print(type(cat_2))
# #
# # dog_1 = Dog('Rex', 12, 'green')
# # dog_1.speak()
# # # print(type(dog_1))
# #
# # dog_2 = Dog('Ben', 15, 'black')
# # dog_2.speak()
# # # print(type(dog_2))
#
# a = Animal('X', 10, 'c')

class Z:
    def do_something(self):
        print('Class Z')


class A(Z):
    def do_something(self):
        print('Class A')


class B:
    def do_something(self):
        print('Class B')


class C(A, B):
    def do_something(self):
        # super(B, self).do_something()
        # B.do_something(self)
        pass


c = C()
c.do_something()
