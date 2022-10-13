from abc import abstractmethod, ABC


class Scratcher(ABC):
    @staticmethod
    @abstractmethod
    def scratch():
        pass


class Animal(ABC):
    def __init__(self, name, age, color):
        # print('__init__ from animal was called!')
        self._name = name
        self.age = age
        self.color = color

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_value):
        self._name = new_value

    @staticmethod
    @abstractmethod
    def speak():
        pass


class Cat(Animal, Scratcher):
    @staticmethod
    def speak():
        print('Miau, miau!')

    @staticmethod
    def scratch():
        print(f'You have been scratched by a cat.')


class Dog(Animal):
    @staticmethod
    def speak():
        print('Ham, ham!')


class Lion(Animal, Scratcher):
    @staticmethod
    def speak():
        print('I have no idea :D')

    @staticmethod
    def scratch():
        print(f'You have been scratched by a lion.')


class Tiger(Animal, Scratcher):
    @staticmethod
    def speak():
        print('I have no idea 2.')

    @staticmethod
    def scratch():
        print(f'You have been scratched by a tiger.')


cat_1 = Cat('Julia', 12, 'white')
# cat_1.speak()
# print(type(cat_1))

cat_2 = Cat('Cat #2', 25, 'black')
# cat_2.speak()
# print(type(cat_2))

dog_1 = Dog('Rex', 12, 'green')
# dog_1.speak()
# print(type(dog_1))

dog_2 = Dog('Ben', 15, 'black')


# dog_2.speak()
# print(type(dog_2))

# class A:
#     pass
#
#
# my_animals = [cat_1, dog_1, cat_2, dog_2, A()]
# for a in my_animals:
#     a.speak()


class A:
    def instance_method(self):
        pass

    @staticmethod
    def static_method():
        pass

    @classmethod
    def class_method(cls):
        return cls()


# a1 = A()
# a1.instance_method()

# A.static_method()
a1 = A.class_method()
print(a1, type(a1))
