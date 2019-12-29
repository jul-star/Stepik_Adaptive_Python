import unittest
from ex_2_6_Digital_Watches import Sec2Time
from unittest.mock import patch
from io import StringIO

class TestCase2_6_Digital_Watches(unittest.TestCase):
    def test_getInput_1(self):
        _user_input = ['3602']
        _Expected = 3602
        _Actual = -1
        with patch('builtins.input', side_effect = _user_input):
            _Actual = Sec2Time.getInput()
        self.assertEqual(_Expected, _Actual)

    def test_getInput_2(self):
        _user_input = ['129700']
        _Expected = 129700
        _Actual = -1
        with patch('builtins.input', side_effect = _user_input):
            _Actual = Sec2Time.getInput()
        self.assertEqual(_Expected, _Actual)

    def test_convert_1(self):
        _tic = 3602
        _Expected = '1:00:02'
        _Actual = Sec2Time.convert(_tic)
        self.assertEqual(_Expected, _Actual)

    def test_convert_2(self):
        _tic = 129700
        _Expected = '12:01:40'
        _Actual = Sec2Time.convert(_tic)
        self.assertEqual(_Expected, _Actual)

    def test_run_1(self):
        _user_input = ['3602']
        _Expected = '1:00:02\n'
        _Actual = None
        with patch('builtins.input', side_effect=_user_input):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                Sec2Time.run()
                _Actual = fake_out.getvalue()
        self.assertEqual(_Expected, _Actual)

    def test_run_2(self):
        _user_input = ['129700']
        _Expected = '12:01:40\n'
        _Actual = None
        with patch('builtins.input', side_effect=_user_input):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                Sec2Time.run()
                _Actual = fake_out.getvalue()
        self.assertEqual(_Expected, _Actual)

if __name__ == '__main__':
    unittest.main()
