from collections.abc import Sequence
from collections.abc import Iterable
import sys
import platform 
import os

class D:
    def __init__(self) -> None:
        pass
    
    # if you define this method, it is still a valid Sequence
    # because even if you defint __container__ or __iter__ or __reversed__ 
    # this is still treated as a Squence because it falls back to below method 
    # ie __Getitem___ and __len__
    def __getitem__(self, index):
        pass

    def __len__(self):
        pass

    def count(self, value):
        pass


# if you impletement __iter__ and __next__ it becomes a Iterable.
# But not complex classes. It only works for simple ones.
class E:
    def __iter__(self):
        pass
    def __next__(self):
        pass


if __name__ == "__main__":

    print(sys.version)
    print(platform.version(), platform.architecture(), platform.processor())
    print(F"Version of Python: {platform.python_version()}")

    # Registering the class as a sequence
    Sequence.register(D)
    d = D()
    print(isinstance(d, Sequence))



    e = E()
    print("e is a Iterable class since we implemented __iter and __next", 
          isinstance(e, Iterable))