
class Common(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('args', args)
        return self.func(*args, **kwargs)

@Common
def test(p):
    print(p)


print(test)
print(test(0))
