class JustSomeString:
    def __init__(self) -> None:
        pass

    def operate(self, text: str, n: int = 1) -> int:
        '''
        Replicates the text for the n of times informed in the 'n'
        parameter and then removes the elements in multiple positions of the
        same parameter
        '''
        replicated = text * n
        cleaned = ''.join([e for i, e in enumerate(replicated) if i % n != 0])
        return cleaned
