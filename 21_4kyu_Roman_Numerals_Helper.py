from termcolor import colored, cprint


class RomanNumerals:
    @staticmethod
    def to_roman(numerals):
        result = ""
        if numerals // 1000 > 0:
            for i in range(numerals // 1000):
                result += "M"
            numerals %= 1000
        if numerals // 500 > 0:
            if numerals // 100 == 9:
                result += "CM"
                numerals -= 400
            else:
                result += "D"
            numerals -= 500
        if numerals // 100 > 0:
            if numerals // 100 == 4:
                result += "CD"
            else:
                for i in range(numerals // 100):
                    result += "C"
            numerals %= 100
        if numerals // 50 > 0:
            if numerals // 10 == 9:
                result += "XC"
                numerals -= 40
            else:
                result += "L"
            numerals -= 50
        if numerals // 10 > 0:
            if numerals // 10 == 4:
                result += "XL"
            else:
                for i in range(numerals // 10):
                    result += "X"
            numerals %= 10
        if numerals // 5 > 0:
            if numerals // 1 == 9:
                result += "IX"
                numerals -= 4
            else:
                result += "V"
            numerals -= 5
        if numerals > 0:
            if numerals == 4:
                result += "IV"
            else:
                for i in range(numerals):
                    result += "I"
        return result

    @staticmethod
    def from_roman(roman_numerals):
        directory = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        for i in range(len(roman_numerals) - 1):
            if roman_numerals[i] != roman_numerals[i + 1] and directory[roman_numerals[i]] < directory[roman_numerals[i + 1]]:
                result += directory[roman_numerals[i + 1]] - directory[roman_numerals[i]]
                if i == len(roman_numerals) - 2:
                    return result
                else:
                    result -= directory[roman_numerals[i + 1]]
            else:
                result += directory[roman_numerals[i]]
        result += directory[roman_numerals[-1]]
        return result


print(RomanNumerals.to_roman(4))
print(RomanNumerals.from_roman("IV"))
print(RomanNumerals.to_roman(6))
print(RomanNumerals.from_roman("VI"))

c = RomanNumerals()
cprint("   to_roman", 'red')
print(str(1000) + "(M)", '-', c.to_roman(1000))
cprint("   to_roman", 'red')
print(str(1990) + "(MCMXC)", '-', c.to_roman(1990))
cprint("   from_roman", 'red')
print("XXI(21)", '-', c.from_roman("XXI"))
cprint("   from_roman", 'red')
print("MMVIII(2008)", '-', c.from_roman("MMVIII"))

cprint("\n   from_roman", 'blue')
print("CIX(109)", '-', c.from_roman("CIX"))
cprint("   from_roman", 'blue')
print("MCMXCIX(1999)", '-', c.from_roman("MCMXCIX"))
cprint("   from_roman", 'blue')
print("MCCLXVII(1267)", '-', c.from_roman("MCCLXVII"))
cprint("   from_roman", 'blue')
print("IV(4)", '-', c.from_roman("IV"))
