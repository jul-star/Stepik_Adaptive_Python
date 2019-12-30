# Write a simple calculator that reads the three input lines: the first number,
# the second number and the operation, after which it applies the operation to the entered numbers
# ("first number" "operation" "second number")
# and outputs the result to the screen. Note that the numbers can be real.
#
# Supported operations: +, -, /, *, mod, pow, div; where
# mod — taking the residue,
# pow — exponentiation,
# div — integer division.
#
# If a user performs the division and the second number is 0,
# it is necessary to output the line "Division by 0!".
#
# Sample Input 1:
# 5.0
# 0.0
# mod
# Sample Output 1:
# Division by 0!
#
# Sample Input 2:
# -12.0
# -8.0
# *
# Sample Output 2:
# 96.0

# Sample Input 3:
# 5.0
# 10.0
# /
# Sample Output 3:
# 0.5


class Calculator:
    @staticmethod
    def run() -> None:
        _operands = Calculator.getInput()
        _out = Calculator.calculate(_operands)
        Calculator.Print(_out)

    @staticmethod
    def Print(out: str) -> None:
        print(out)

    @staticmethod
    def getInput() -> list:
        _n1 = str(input().strip())
        _n2 = str(input().strip())
        _operation = str(input().strip())
        _out = [_n1, _n2, _operation]
        return _out

    @staticmethod
    def calculate(operands: list) -> str:
        _template: str = '({left}) {sign} ({right})'
        (_left, _right, _sign) = (float(operands[0]), float(operands[1]), str(operands[2]))
        if _sign in ['%', '//']:
            _left = int(_left)
            _right = int(_right)
        if _sign == 'mod':
            _sign = '%'
        if _sign == 'pow':
            _sign = '**'
        if _sign == 'div':
            _sign = '//'

        _evl = _template.format(left=_left, sign=_sign, right=_right)
        try:
            return str(eval(_evl))
        except ZeroDivisionError:
            return 'Division by 0!'


if __name__ == "__main__":
    Calculator.run()
