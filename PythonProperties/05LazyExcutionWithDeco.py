import time


def lazy_property(fn):
    """Decorator that makes a property lazy-evaluated.
    """
    attr_name = "_lazy_" + fn.__name__

    @property
    def _lazy_property(self):
        if not hasattr(self, attr_name):
            setattr(self, attr_name, fn(self))
        return getattr(self, attr_name)

    return _lazy_property


class Person:
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation

    @lazy_property
    def relatives(self):
        # Get all relatives
        print("setting relatives")
        time.sleep(4)
        relatives = "Ricky"
        print(f"{self.name} relatives is {relatives}")
        return relatives


p = Person("juan", "student")
x = 0
p.relatives

# p.relatives = 3

