from typing import Callable
from decimal import *


def zero_bisect(f: Callable[[float], float], a: float, b: float, precision: float) -> float:
    if f(a) * f(b) > 0:
        raise Exception("f(a) * f(b) > 0")
    while abs(b - a) > precision:
        x = (a + b) / 2
        if abs(f(x)) < precision:
            break
        elif f(a) * f(x) < 0:
            b = x
        else:
            a = x
    setcontext(Context(prec=60))
    return (Decimal(a) + Decimal(b)) / Decimal(2)


def g(x: float) -> float:
    return 2 ** x - 3


print(f'log_2 3: {zero_bisect(g, 0, 2, 0.000000000000001)}')
