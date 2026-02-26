from abc import ABC, abstractmethod

class MetodaNeniImplementovana(Exception):
    pass

def abstractmethod(func):
    def wrapper(*args, **kwargs):
        raise MetodaNeniImplementovana(f"Metoda musí být implementována v podtřídě.")
    return wrapper

class AbstractClass(ABC):
    @abstractmethod
    def my_method(self):
        pass

class MyClass(AbstractClass):
    def my_method(self):
        print("Implementace metody my_method")

if __name__ == "__main__":
    my_instance = MyClass()
    my_instance.my_method()

    ab_object = AbstractClass()
    ab_object.my_method()  