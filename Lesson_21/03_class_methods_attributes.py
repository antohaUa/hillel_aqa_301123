class Coordinates:
    MIN_X = 0
    MIN_Y = 0
    MAX_X = 1920
    MAX_y = 1280

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def set_max_x(cls, x):
        cls.MAX_X = x

    def __getattribute__(self, attr):
        print(f'Looking for attribute {attr}')
        return super().__getattribute__(attr)

    def __setattr__(self, key, value):
        print('we are in setattr')
        super().__setattr__(key, value)

    def __getattr__(self, item):
        print('Call to non existing attributes')
        return 1000

    def __delattr__(self, item):
        print(f'Attribute {item=} was deleted')


pt1 = Coordinates(100, 200)
print(pt1.x)
pt1.x = 200
print(pt1.z)
del pt1.x
