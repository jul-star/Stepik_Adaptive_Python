import unittest
from ex_2_18_Calculator import Calculator
from unittest.mock import patch
from io import StringIO


class TestCase_2_18(unittest.TestCase):
    def setUp(self) -> None:
        self._user_input_N = ['5.0', '0.0', '%',
                              '-12.0', '-8.0', '*',
                              '5.0', '10.0', '/',
                              '5', '0', '/',
                              '5', '0', '//',
                              '5', '2', '**',
                              '10', '5', '-',
                              '10', '-5', '+',
                              '-12', '0', '*',
                              '5', '2', '/',
                              '10', '5', '/',
                              '5', '0', '**',
                              '4', '0.5', '**',
                              '10', '2', '%',
                              '10', '3', '%',
                              '10', '3', '//',
                              '10', '5', '//',
                              '1', '7', '//',
                              '1', '6', '**',
                              '8', '7', '%',
                              '0', '2', '//',
                              '4', '2', '//',
                              '-9', '4', '/',
                              '2', '3', '*',
                              '-5', '9', '%',
                              '2', '2', '**',
                              '-1', '8', '//',
                              '-1', '2', '-',
                              '4', '8', '*',
                              '-4', '3', '**',
                              '4', '6', '/',
                              '7', '5', '/',
                              '8', '1', '-',
                              '-9', '1', '%',
                              '4', '2', '%',
                              '-6', '3', '%',
                              '-3', '4', '**']

    def test_getInput(self):

        _Expected = [
            ['5.0', '0.0', '%'],
            ['-12.0', '-8.0', '*'],
            ['5.0', '10.0', '/'],
            ['5', '0', '/'],
            ['5', '0', '//'],
            ['5', '2', '**'],
            ['10', '5', '-'],
            ['10', '-5', '+'],
            ['-12', '0', '*'],
            ['5', '2', '/'],
            ['10', '5', '/'],
            ['5', '0', '**'],
            ['4', '0.5', '**'],
            ['10', '2', '%'],
            ['10', '3', '%'],
            ['10', '3', '//'],
            ['10', '5', '//'],
            ['1', '7', '//'],
            ['1', '6', '**'],
            ['8', '7', '%'],
            ['0', '2', '//'],
            ['4', '2', '//'],
            ['-9', '4', '/'],
            ['2', '3', '*'],
            ['-5', '9', '%'],
            ['2', '2', '**'],
            ['-1', '8', '//'],
            ['-1', '2', '-'],
            ['4', '8', '*'],
            ['-4', '3', '**'],
            ['4', '6', '/'],
            ['7', '5', '/'],
            ['8', '1', '-'],
            ['-9', '1', '%'],
            ['4', '2', '%'],
            ['-6', '3', '%'],
            ['-3', '4', '**']
        ]
        _Actual = []
        with patch('builtins.input', side_effect=self._user_input_N):
            for i in range(37):
                _Actual.append(Calculator.getInput())

        self.assertListEqual(_Expected, _Actual)

    def test_getInput_N(self):
        _user_input = ['5.51', '-1.23', 'mod']
        _Expected = ['5.51', '-1.23', 'mod']
        _Actual = None
        with patch('builtins.input', side_effect=_user_input):
            _Actual = Calculator.getInput()

        self.assertEqual(_Expected, _Actual)

    def test_calculate_1(self):
        _operands = [5.51, -1.23, '%']
        _Expected = '0'
        _Actual = Calculator.calculate(_operands)
        self.assertEqual(_Expected, _Actual)

    def test_calculate_2(self):
        _operands = [5.0, 0.0, '%']
        _Expected = 'Division by 0!'
        _Actual = Calculator.calculate(_operands)
        self.assertEqual(_Expected, _Actual)

    def test_calculate_3(self):
        _operands = [-12.0, -8.0, '*']
        _Expected = '96.0'
        _Actual = Calculator.calculate(_operands)
        self.assertEqual(_Expected, _Actual)

    def test_calculate_4(self):
        _operands = [5.0, 10.0, '/']
        _Expected = '0.5'
        _Actual = Calculator.calculate(_operands)
        self.assertEqual(_Expected, _Actual)

    def test_run_1(self):
        _user_input = ['5', '2', '%']
        _Expected = '1'
        _Actual = None
        with patch('builtins.input', side_effect=_user_input):
            with patch('sys.stdout', new=StringIO()) as _out:
                Calculator.run()
                _Actual = _out.getvalue().rstrip()

        self.assertEqual(_Expected, _Actual)

    def test_run_2(self):
        _user_input = ['5.0', '0.0', '%']
        _Expected = 'Division by 0!'
        _Actual = None
        with patch('builtins.input', side_effect=_user_input):
            with patch('sys.stdout', new=StringIO()) as _out:
                Calculator.run()
                _Actual = _out.getvalue().rstrip()

        self.assertEqual(_Expected, _Actual)

    def test_run_3(self):
        _user_input = ['12.0', '-8.0', '*']
        _Expected = '-96.0'
        _Actual = None
        with patch('builtins.input', side_effect=_user_input):
            with patch('sys.stdout', new=StringIO()) as _out:
                Calculator.run()
                _Actual = _out.getvalue().rstrip()

        self.assertEqual(_Expected, _Actual)

    def test_run_4(self):
        _user_input = ['5.0', '10.0', '/']
        _Expected = '0.5'
        _Actual = None
        with patch('builtins.input', side_effect=_user_input):
            with patch('sys.stdout', new=StringIO()) as _out:
                Calculator.run()
                _Actual = _out.getvalue().rstrip()

        self.assertEqual(_Expected, _Actual)

    def test_run_N(self):
        _Expected = ['Division by 0!', '96.0', '0.5', 'Division by 0!', 'Division by 0!', '25.0', '5.0', '5.0', '-0.0',
                     '2.5', '2.0', '1.0', '2.0', '0', '1', '3', '2', '0', '1.0', '1', '0', '2', '-2.25', '6.0', '4',
                     '4.0', '-1', '-3.0', '32.0', '-64.0', '0.6666666666666666', '1.4', '7.0', '0', '0', '0', '81.0']
        _Actual = []
        _tmp: str = str()
        with patch('builtins.input', side_effect=self._user_input_N):
            with patch('sys.stdout', new=StringIO()) as _out:
                for i in range(37):
                    Calculator.run()
                _tmp = _out.getvalue().rstrip()

        # print('tmp=', _tmp)
        _Actual = _tmp.split('\n')
        print('Actual = ', _Actual)
        self.assertListEqual(_Expected, _Actual)


if __name__ == '__main__':
    unittest.main()
