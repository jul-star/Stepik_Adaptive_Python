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
        _n1 = str(input())
        _n2 = str(input())
        _operation = str(input().rstrip())
        _out = [_n1, _n2, _operation]
        return _out

    @staticmethod
    def calculate1(operands: list) -> str:
        """
        Supported operations: +, -, /, *, mod, pow, div
        :param operands: list of operands
        :return: string
        """
        _out: str = str()
        _left: float = operands[0]
        _right: float = operands[1]
        if operands[2] == '%':
            _out = Calculator.mod(int(_left), int(_right))
        elif operands[2] == '+':
            _out = Calculator.sum(float(_left), float(_right))
        elif operands[2] == '-':
            _out = Calculator.sub(float(_left), float(_right))
        elif operands[2] == '/':
            _out = Calculator.division(float(_left), float(_right))
        elif operands[2] == '*':
            _out = Calculator.mul(float(_left), float(_right))
        elif operands[2] == '**':
            _out = Calculator.pow(float(_left), float(_right))
        elif operands[2] == '//':
            _out = Calculator.div(int(_left), int(_right))
        else:
            _out = 'Wrong input'
        return _out

    @staticmethod
    def calculate(operands: list) -> str:
        _template:str='{left}{sign}{right}'
        _evl = _template.format(left=operands[0],sign = operands[2],right=operands[1])
        _res = eval(_evl)
        return str(_res)

    @staticmethod
    def mod(o1: int, o2: int) -> str:
        if int(o2) == 0:
            return 'Division by 0!'
        return str(int(o1) % int(o2))

    @staticmethod
    def sum(o1: float, o2: float) -> str:
        return str(o1 + o2)

    @staticmethod
    def sub(o1: float, o2: float) -> str:
        return str(o1 - o2)

    @staticmethod
    def division(o1: float, o2: float) -> str:
        if float(o2) == 0:
            return 'Division by 0!'
        return str(o1 / o2)

    @staticmethod
    def mul(o1: float, o2: float) -> str:
        return str(o1 * o2)

    @staticmethod
    def pow(o1: float, o2: float) -> str:
        return str(o1 ** o2)

    @staticmethod
    def div(o1: int, o2: int) -> str:
        return str(o1 // o2)


if __name__ == "__main__":
    pass
