# if __name__ == '__main__':
#     a = 2
#     print(type(a))
#     # print(a.lower())  # int object has no 'lower' behavior (method)
#
#     b = "my string"
#     print(type(b))
#     print(b.lower())
#
#     # print(type(int))
#     # print(type(str))
#     # print(type(type))


class Dog:
    legs_number = 4

    def __init__(self, name, age, color):
        self._name = name
        self.age = age
        self.color = color
        self.something_else = None

    def __str__(self):
        return self._name

    @staticmethod
    def bark():
        print('Ham, ham!')

    def set_age(self, new_age):
        self.age = new_age

    # def get_name(self):
    #     return self._name
    @property
    def name(self):
        return self._name

    # def set_name(self, new_name):
    #     permission_denied = True
    #
    #     if permission_denied:
    #         raise PermissionError('You do not have access to this method.')
    #
    #     self._name = new_name
    @name.setter
    def name(self, new_value):
        permission_denied = True

        if permission_denied:
            raise PermissionError('You do not have access to this method.')

        self._name = new_value

    def lose_leg(self):
        self.legs_number -= 1


# print(type(Dog))
# print(dir(Dog))

# my_dog = Dog('Rex', 12, 'black')
# my_dog.something_else = 123
# print('my_dog', my_dog.name, my_dog.age, my_dog.color, my_dog.something_else)
# print(my_dog)
# my_dog_str_representation = str(my_dog)
# print(my_dog_str_representation, type(my_dog_str_representation))

# your_dog = Dog('Ben', 25, 'white')
# print('your_dog', your_dog.name, your_dog.age, your_dog.color, your_dog.something_else)
# print(your_dog)

# print(type(Dog))
# print(type(my_dog))

# my_dog = Dog('Rex', 12, 'black')
# my_dog.something_else = 123
#
# your_dog = Dog('Ben', 25, 'white')
#
# dogs = [my_dog, your_dog]
# # dogs = [your_dog, my_dog]
#
# for dog in dogs:
#     # print(dog.something_else)
#     # if hasattr(dog, 'something_else'):
#     #     print(dog.something_else)
#     # else:
#     #     print(f'{dog} do not have "something_else" attribute')
#     # print(dog.something_else)
#     dog.bark()

# my_dog = Dog('Rex', 12, 'black')
# print(my_dog.age)
#
# # my_dog.age = 13
# # print(my_dog.age)
#
# # my_dog.gets_old()
# # print(my_dog.age)
#
# my_dog.set_age(79)
# print(my_dog.age)

# dog_1 = Dog('Rex', 12, 'black')
# # dog_1._name = 'Ben'  # do not use `_` variables. They are meant to be private.
# # print(dog_1.set_name('Ben'))
# dog_1.name = 'Ben'
# # print(dog_1.get_name())
# print(dog_1.name)
# # print(dog_1.__name)
# # print(dog_1._Dog__name)  # name mangling
# # print(dog_1)

dog_1 = Dog('Rex', 12, 'black')
# print(dog_1.name, dog_1.age, dog_1.color, dog_1.legs_number, dog_1.bark())
# print(dog_1.name, dog_1.age, dog_1.color, Dog.legs_number, Dog.bark())
print(dog_1.legs_number)

dog_2 = Dog('Ben', 35, 'white')
# print(dog_2.name, dog_2.age, dog_2.color, Dog.legs_number, Dog.bark())
dog_2.lose_leg()
# print(dog_2.name, dog_2.age, dog_2.color, dog_2.legs_number, dog_2.bark())
print(dog_2.legs_number)

Dog.legs_number = 5

dog_3 = Dog('X', 10, 'red')
print(dog_3.legs_number)

print(dog_1.legs_number)
print(dog_2.legs_number)
