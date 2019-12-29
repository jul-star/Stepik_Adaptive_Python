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
        _o = Calculator.getInput()

    @staticmethod
    def getInput() -> list:
        _n1 = float(input())
        _n2 = float(input())
        _operation = str(input().rstrip())
        _out = [_n1, _n2, _operation]
        return _out

    @staticmethod
    def calculate(operands: list) -> str:
        """
        Supported operations: +, -, /, *, mod, pow, div
        :param operands: list of operands
        :return: string
        """
        _out: str = None
        if operands[2] == 'mod':
            _out = Calculator.mod(int(operands[0]), int(operands[1]))
        elif operands[2] == '+':
            _out = Calculator.sum(operands[0], operands[1])
        elif operands[2] == '-':
            _out = Calculator.sub(operands[0], operands[1])
        elif operands[2] == '/':
            _out = Calculator.division(operands[0], operands[1])
        elif operands[2] == '*':
            _out = Calculator.mul(operands[0], operands[1])
        elif operands[2] == 'pow':
            _out = Calculator.pow(operands[0], operands[1])
        elif operands[2] == 'div':
            _out = Calculator.div(int(operands[0]), int(operands[1]))
        else:
            _out = 'Wrong input'
        return _out

    @staticmethod
    def mod(o1: int, o2: int) -> str:
        if o2 == 0:
            return 'Division by 0!'
        return str(o1 % o2)

    @staticmethod
    def sum(o1: float, o2: float) -> str:
        return str(o1 + o2)

    @staticmethod
    def sub(o1: float, o2: float) -> str:
        return str(o1 - o2)

    @staticmethod
    def division(o1: float, o2: float) -> str:
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
