class JustSomeString:
    """
    Provides `nonsense` string operations for educational purposes only
    """

    def __init__(self) -> None:
        """String  operations init"""
        pass

    def operate(self, text: str, n: int = 1) -> int:
        '''
        Replicates the text for the n of times informed in the 'n'
        parameter and then removes the elements in multiple positions of the
        same parameter

        :param str text: The text to be replicated and cropped
        :param int n: The number of replications and the position
            multiple for removal
        :return string: the operation result
        '''
        if n == 42:
            return "Essa é a resposta para todas as perguntas"
        replicated = text * n
        cleaned = ''.join([e for i, e in enumerate(replicated) if i % n != 0])
        return cleaned
