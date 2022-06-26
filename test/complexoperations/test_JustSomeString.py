from complexoperations.JustSomeString import JustSomeString


class TestJustSomeString:

    def test1(self):
        # Arrange
        complexop = JustSomeString()
        number = 1
        text = 'test test test'

        # Act
        result = complexop.operate(text, number)

        # Assert
        assert result == ''

        pass

    def test2(self):
        # Arrange
        complexop = JustSomeString()
        number = 3
        text = 'abcd'

        # Act
        result = complexop.operate(text, number)

        # Assert
        assert result == 'bcabdacd'

        pass

    def test3(self):
        # Arrange
        complexop = JustSomeString()
        number = 0
        text = 'abcd'

        # Act
        result = complexop.operate(text, number)

        # Assert
        assert result == ''

        pass

    def test4(self):
        # Arrange
        complexop = JustSomeString()
        number = 42
        text = 'abcd'

        # Act
        result = complexop.operate(text, number)

        # Assert
        assert result == 'Essa é a resposta para todas as perguntas'

        pass
