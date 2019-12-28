# Digital watches
#
# Digital watches display time in the h:mm:ss format (from 0:00:00 to 23:59:59),
# i.e. first goes the number of hours, then goes the two-digit number of minutes,
# followed by the two-digit number of seconds.
# If necessary, number of minutes and seconds are filled by zeroes to a two-digit number.
#
# N seconds passed from the beginning of the day. Output what the watches will display.
#
# Input data format
#
# Given the natural number N on input, not exceeding 10^710
# 7
#   (10000000).

# Sample Input 1:
#
# 3602
# Sample Output 1:
#
# 1:00:02


class Sec2Time:
    @staticmethod
    def getInput() -> int:
        _tic = int(input())
        return _tic

    @staticmethod
    def convert(tic: int) -> str:
        _sec = tic % 60
        _min = int(tic / 60) % 60
        _hours = int(tic / 3600) % 24
        _sec_str = str(_sec)
        if _sec < 10:
            _sec_str = '0' + _sec_str
        _min_str = str(_min)
        if _min < 10:
            _min_str = '0' + _min_str
        _hours_str = str(_hours)
        _template = '{h}:{m}:{s}'
        _out = _template.format(h=_hours_str, m=_min_str, s=_sec_str)
        return _out

    @staticmethod
    def run():
        _tic = Sec2Time.getInput()
        _time = Sec2Time.convert(_tic)
        Sec2Time.Print(_time)

    @staticmethod
    def Print(tm: str) -> None:
        print(tm)


if __name__ == "__main__":
    Sec2Time.run()
