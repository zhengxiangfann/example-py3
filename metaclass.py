class Hello(object):
    def __init__(sel, func):
        self.func func

    def hello(self):
        print('ssssss')


def hello(cls):
    print('hhhh')

def __init__(cls, func):
    cls.func = func

class HelloMeta(type):
    def __new__(cls, name, bases, attrs):
        def __init__(cls, func):
            cls.func = func
        def hello(cls):
            print('hell')
        t = type.__new__(cls, name, bases, dict(attrs.viewitems() | [('hello', hello),('__init__', __init__ )]))
        return t

class New_Class(object):
    __metaclass__ = HelloMeta


hellometa = lambda name, parents, attrs:type(name,
                                            parents,
                                            dict(attrs.items() + [('__new__',classmethod(lambda cls, *args, **kargs:super(type(cls), cls).__new__(*args, **kargs))),
                                                                  ('hello', hello),
                                                                  ('__init__', __init__)
                                                                  ])
                                             )

class New_Hello2(object):
    __metaclass__ = hellometa


