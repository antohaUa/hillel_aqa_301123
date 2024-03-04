class Something:

    def __init__(self):
        self.__cvv = 123

    @property
    def cvv(self):
        return self.__cvv

    @cvv.setter
    def cvv(self, cvv):
        self.__cvv = cvv
        return True


smth = Something()
print(smth.cvv)
smth.cvv = 809
print(smth.cvv)

