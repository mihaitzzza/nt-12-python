# class A:
#     def do_something(self):
#         print('Class A')
#
#
# class B:
#     def do_something(self):
#         print('Class B')
#
#
# class C(A, B):
#     def do_something(self):
#         # A.do_something(self)
#         B.do_something(self)
#
#
# c = C()
# c.do_something()


# class A:
#     def f(self):
#         print('Class A')
#
#
# class B(A):
#     def f(self):
#         print('Class B')
#
#
# class C(B):
#     def f(self):
#         super(B, self).f()
#
#
# c = C()
# c.f()

class A:
    def __init__(self, first_name):
        self.first_name = first_name


class B:
    def __init__(self, last_name):
        self.last_name = last_name


class C(A, B):
    def __init__(self, first_name, last_name):
        A.__init__(self, first_name)
        B.__init__(self, last_name)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


c = C('Ion', 'Popescu')
print(c)
