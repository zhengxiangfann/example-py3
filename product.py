class Pro(object):
    def __init__(self, id, auth_id, category_id, brand_id, spu_id, title):
        self.id = id
        self.auth_id = auth_id
        self.category_id = category_id
        self.brand_id = brand_id
        self.spu_id = spu_id
        self.title = title

    def __repr__(self):
        return '{}(id={}, auth_id={}, category_id={}, brand_id={}, spu_id={}, title={})'.format(
            self.__class__.__name__, self.id, self.auth_id, self.category_id, self.brand_id, self.spu_id, self.title
        )

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return (self.id, self.auth_id, self.category_id, self.brand_id) == (
            other.id, other.auth_id, other.category_id,other.brand_id
        )

    def __lt__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return (self.id, self.auth_id, self.category_id, self.brand_id) < (
        other.id, other.auth_id, other.category_id, other.brand_id)

    def __hash__(self):
        #return hash((self.id, self.auth_id, self.category_id, self.brand_id, self.spu_id, self.title))
        return hash((self.id, self.auth_id, self.category_id, self.brand_id))

    def to_dict(self):
        self._a = 1
        return vars(self)


from datetime import datetime
from dataclasses import dataclass, field

#@dataclass(hash=True, order=True)
#class Product(object):
#    id:int
#    auth_id:int
#    brand_id:int
#    spu_id:int
#    title:str = field(hash=False, repr=False, compare=False)
#    item_id:int = field(hash=False, repr=False, compare=False)
#    n_comments:int = field(hash=False, repr=False,compare=False)



import attr

@attr.s(hash=True)
class Product1(object):
    id = attr.ib()
    auth_id = attr.ib()
    brand_id = attr.ib()
    spu_id = attr.ib()
    title = attr.ib(hash=False, repr=False, cmp=False)
    item_id= field(hash=False, repr=False, cmp=False, default=0)
    n_comments= field(hash=False, repr=False, cmp=False, default=0)

if __name__ == '__main__':
   # p1 = Pro(1,2, 3, 4, 5, 'test')
   # p2 = Pro(1,3, 3, 4, 5, 'test')
   # p3 = Pro(1,3, 3, 4, 5, 'test')
   # print({p3, p2})
    p1 = Product1(1, 2, 3, 4, 'test')
    print(p1)


