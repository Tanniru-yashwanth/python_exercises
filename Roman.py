class Roman:
    def __init__(self, integer):
        self.integer = integer
        self.numbers = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD',
                        500: 'D', 900: 'CM', 1000: 'M'}
        self.List = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

    def convert(self):
        a = ""
        for x in self.List:
            if self.integer != 0:
                quotient = self.integer / x

                if quotient != 0:
                    for y in range(int(quotient)):
                        a += self.numbers[x]
                        a += ""

                self.integer = self.integer % x
        return a


num = Roman(234)
b = num.convert()
print(b)
