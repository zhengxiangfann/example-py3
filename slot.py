import time
class BaseSlots(object):
    __slots__ = ['e', 'f', 'g']


class Slots(BaseSlots):
    __slots__ = ['a','b','c','d']
    def __init__(self,):
        self.a = self.b = self.c = self.d = self.e = self.f = self.g = 0


class BaseNoSlots(object):
    pass

class NoSlots(BaseNoSlots):
    def __init__(self):
        super(NoSlots, self).__init__()
        self.a = self.b = self.c = self.d = self.e = self.f = self.g = 0

def log_time(s):
    begin = time.time()
    for i in range(1000000):
        s.a, s.b, s.c, s.d, s.e, s.f, s.g
    return time.time() - begin

if __name__ == '__main__':
    print('Slots cost', log_time(Slots()))
    print('NoSlots cost', log_time(NoSlots()))



