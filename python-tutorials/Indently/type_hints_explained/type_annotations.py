text: str = '100'


class Fruit:
    def __init__(self):
        print('Hello')


banana: Fruit = Fruit()
banana = 100


def func(param: list[str]):
    print(param)
    return 'Ira was here'


foo = ["Bob", "Carol", "Ted", "Alice"]
func(foo)
func(100)
