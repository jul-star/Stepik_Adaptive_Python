import unittest
from ex_2_18_Calculator import Calculator
from unittest.mock import patch
from io import StringIO

class TestCase_2_18(unittest.TestCase):
    def test_getInput(self):
        _user_input = ['5.51', '-1.23', 'mod']
        _Expected = [5.51, -1.23, 'mod']
        _Actual = None
        with patch('builtins.input', side_effect=_user_input):
            _Actual = Calculator.getInput()

        self.assertEqual(_Expected, _Actual)

    def test_calculate(self):
        _operands = [5.51, -1.23, 'mod']
        _Expected = ''
        _Actual = Calculator.calculate(_operands)
        self.assertEqual(_Expected, _Actual)

    def test_mod_1(self):
        _operands = [5.51, -1.23]
        _Expected = ''
        _Actual = Calculator.mod(_operands[0], _operands[1])
        self.assertEqual(_Expected, _Actual)

    def test_mod_2(self):
        _operands = [5.51, -0.23]
        _Expected = 'Division by 0!'
        _Actual = Calculator.mod(_operands[0], _operands[1])
        self.assertEqual(_Expected, _Actual)

    def test_sum_2(self):
        _operands = [5.51, -0.23]
        _Expected = '5.28!'
        _Actual = Calculator.sum(_operands[0], _operands[1])
        self.assertEqual(_Expected, _Actual)

    def test_division(self):
        _operands = [5.51, -0.23]
        _Expected = '-23.956521739130434'
        _Actual = Calculator.division(_operands[0], _operands[1])
        self.assertEqual(_Expected, _Actual)

    def test_mul(self):
        _operands = [5.51, -0.23]
        _Expected = '-1.2673'
        _Actual = Calculator.division(_operands[0], _operands[1])
        self.assertEqual(_Expected, _Actual)

    def test_pow(self):
        _operands = [5.51, -0.23]
        _Expected = '0.6753596850257031'
        _Actual = Calculator.pow(_operands[0], _operands[1])
        self.assertEqual(_Expected, _Actual)

    def test_div(self):
        _operands = [5.51, -0.23]
        _Expected = '-24.0'
        _Actual = Calculator.div(_operands[0], _operands[1])
        self.assertEqual(_Expected, _Actual)

    def test_run(self):
        _user_input = ['5', '2', 'mod']
        _Expected = '1'
        _Actual = None
        with patch('builtins.input', side_effect = _user_input):
            with patch('sys.stdout', new = StringIO()) as _out:
                Calculator.run()
                _Actual = _out.getvalue()

        self.assertEqual(_Expected, _Actual)


if __name__ == '__main__':
    unittest.main()
