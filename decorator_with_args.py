
def common(*args, **kw):
    a = args
    def _common(func):
        def _deco(*args, **kwargs):
            print('args', args, a)
            return func(*args, **kwargs)
        return _deco
    return _common


@common('c')
def test(p):
    print(p)

print(test)
print(test(1))
