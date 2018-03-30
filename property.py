class C(object):
    def __init__(self):
        self._x = None

    def getx(self):
        print('getx')
        return self._x

    def setx(self, value):
        print('set x')
        self._x = value

    def delx(self):
        print('delx')
        del self._x
    x = property(getx, setx, delx, 'ff')

class Parrot(object):
    def __init__(self):
        self._voltage = 100000

    @property
    def voltage(self):
        return self._voltage

    @property.setter
    def voltage(self, value):
        self._voltage = value

