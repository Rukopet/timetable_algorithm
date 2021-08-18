class A:
    pass


class B(A):
    pass


class C:
    pass


a = A()
b = B()
c = C()

if issubclass(b.__class__, C) and 'a' not in vars(__builtins__): print("YES!")
