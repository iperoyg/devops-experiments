import math
import random


class JustSomeMath:

    def __init__(self) -> None:
        pass

    def operate(self, number: int = 0) -> int:
        '''
        Does an exponentiation operation on the passed number
        using a random exponent
        '''
        random_int = random.randint(0, number)
        return math.pow(number, random_int)
