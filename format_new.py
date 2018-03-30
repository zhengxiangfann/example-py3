

import decimal

na = "f"
na = f"abc{na}"
print(na)


value = decimal.Decimal("12.34567")
width=10
precision=4
p = f"result:{value:{width}.{precision}}"
print(p)

