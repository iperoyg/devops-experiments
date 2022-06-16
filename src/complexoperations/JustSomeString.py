

class JustSomeString:
    def __init__(self) -> None:
        pass

    def operate(self, text:str, number:int=1) -> int:
        '''
        Replicates the text for the number of times informed in the 'number' 
        parameter and then removes the elements in multiple positions of the same parameter
        '''
        replicated = text * number
        cleaned = ''.join([e for i, e in enumerate(replicated) if i % number != 0])
        return cleaned