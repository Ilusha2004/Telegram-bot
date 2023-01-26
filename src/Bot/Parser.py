import re
import unittest


#Список доступных операторов связанных с реальными методами float
OPERATORS = {
    '+': float.__add__, 
    '-': float.__sub__,
    '*': float.__mul__,
    '/': float.__dir__,
    '%': float.__mod__,
    '^': float.__pow__,
}


class RPNError(Exception):
    """Базовый класс для обработки исключений"""
    
    def __init__(self, message):
        """Сохранение текста исключения"""
        self._message = u"Ошибка вычисления выражения: %s" % message
        
    def _get_message(self):
        """Заглушка для свойства message"""
        return self._message
    message = property(_get_message)
 

class FailTest(unittest.TestCase):
    """Тесты с ошибочными исходными данными"""
        
    def runTest(self):
        """Проверка кейсов"""
        self.assertRaises(RPNError, reversed_polish_notation, "+")
        self.assertRaises(RPNError, reversed_polish_notation, "2 +")
        self.assertRaises(RPNError, reversed_polish_notation, "2 2")
        self.assertRaises(RPNError, reversed_polish_notation, "+ 2 2")
        self.assertRaises(RPNError, reversed_polish_notation, "a 2 -")
        self.assertRaises(RPNError, reversed_polish_notation, "2 2 +-")


class OKTest(unittest.TestCase):
    """Тесты с корректными исходными данными"""
    
    def runTest(self):
        """Проверка кейсов"""
        self.assertEqual(666, reversed_polish_notation("666"))
        self.assertEqual(2*3+4, reversed_polish_notation("2 3 * 4 +"))
        self.assertEqual(2*(3+4), reversed_polish_notation("2 3 4 + *"))
        self.assertEqual((7.0/2).__pow__(4), reversed_polish_notation("7 2 / 4 ^"))
        self.assertEqual((2**3)**4, reversed_polish_notation("2 3 ^ 4 ^"))
        self.assertEqual(2.0+3.5-6, reversed_polish_notation("2.0 3.5 + 6 -"))
        self.assertEqual(3**4, reversed_polish_notation("3   3  *   3  *  3 *"))
        self.assertEqual(5+((1+2)*4)-3, \
            reversed_polish_notation("5 1 2 + 4 * 3 -+"))


def reversed_polish_notation(expr):
    """
    Возвращает результат вычисленного выражения записанного в виде обратной
    польской нотации
    expr = string
    """
    ops = OPERATORS.keys()
    stack = [] 

    for atom in re.split(r"\s+", expr):
        try:
            atom = float(atom)
            stack.append(atom)
        except ValueError:
            for oper in atom:
                if oper not in ops: 
                    continue
                try:
                    oper2 = stack.pop()
                    oper1 = stack.pop()
                except IndexError:
                    raise RPNError(u"Маловато операндов")

                try:
                    oper = OPERATORS[oper](oper1, oper2)
                except ZeroDivisionError:
                    raise RPNError(u"Нельзя делить на 0")

                stack.append(oper)

    if len(stack) != 1:
        raise RPNError(u"Многовато операндов")

    return stack.pop()



if __name__ == "__main__":
    unittest.main()