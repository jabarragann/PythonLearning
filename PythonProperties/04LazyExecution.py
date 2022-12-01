import time


def timer_func(func):
    # This function shows the execution time of
    # the function object passed
    def wrap_func(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print(f"Function {func.__name__!r} executed in {(t2-t1):.4f}s")
        return result

    return wrap_func


class LazyPerson:
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation
        self._relatives = None

    @property
    def relatives(self):
        if self._relatives is None:
            time.sleep(1)
            self._relatives = 1
        return self._relatives

    def __str__(self) -> str:
        return f"{self.name} is a {self.occupation}"


class Person:
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation
        self._relatives = self.get_relatives()

    def get_relatives(self):
        time.sleep(1)
        return 1

    def __str__(self) -> str:
        return f"{self.name} is a {self.occupation}"


@timer_func
def create_person():
    print(Person("juan", "student"))


@timer_func
def create_lazy_person():
    lazy = LazyPerson("juan2", "student2")
    print(lazy)
    return lazy


@timer_func
def get_relatives(person):
    print(person.relatives)


create_person()
lazy = create_lazy_person()

# timer_func(lazy.relatives)
get_relatives(lazy)

