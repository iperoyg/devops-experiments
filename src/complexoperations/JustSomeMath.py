import math
import random


class JustSomeMath:
    """
    Provides `nonsense` math operations for educational purposes only
    """

    def __init__(self) -> None:
        """Math operations init"""
        pass

    def operate(self, number: int = 0) -> int:
        '''
        Does an exponentiation operation on the passed number
        using a random exponent

        :param int number: The number for the complex operation
        :return int: the operation result
        '''
        random_int = random.randint(0, number)
        return math.pow(number, random_int)
