class Solution:
    def intToRoman(self, num: int) -> str:
        numInRoman = ""
        timesDividedBy1000 = num // 1000
        num -= (timesDividedBy1000 * 1000)
        timesDividedBy500 = num // 500
        num -= (timesDividedBy500 * 500)
        timesDividedBy100 = num // 100
        num -= (timesDividedBy100 * 100)
        timesDividedBy50 = num // 50
        num -= (timesDividedBy50 * 50)
        timesDividedBy10 = num // 10
        num -= (timesDividedBy10 * 10)
        timesDividedBy5 = num // 5
        num -= (timesDividedBy5 * 5)
        timesDividedBy1 = num

        numInRoman = numInRoman + ("M" * timesDividedBy1000)

        if (timesDividedBy500 * 500) + (timesDividedBy100 * 100) == 900:
            numInRoman = numInRoman + ("CM")
        elif (timesDividedBy500 * 500) + (timesDividedBy100 * 100) == 400:
            numInRoman = numInRoman + ("CD")
        else:
            numInRoman = numInRoman + ("D" * timesDividedBy500)
            numInRoman = numInRoman + ("C" * timesDividedBy100)
        
        if (timesDividedBy50 * 50) + (timesDividedBy10 * 10) == 90:
            numInRoman = numInRoman + ("XC")
        elif (timesDividedBy50 * 50) + (timesDividedBy10 * 10) == 40:
            numInRoman = numInRoman + ("XL")
        else:
            numInRoman = numInRoman + ("L" * timesDividedBy50)
            numInRoman = numInRoman + ("X" * timesDividedBy10)

        if (timesDividedBy5 * 5) + (timesDividedBy1) == 9:
            numInRoman = numInRoman + ("IX")
        elif (timesDividedBy5 * 5) + (timesDividedBy1) == 4:
            numInRoman = numInRoman + ("IV")
        else:
            numInRoman = numInRoman + ("V" * timesDividedBy5)
            numInRoman = numInRoman + ("I" * timesDividedBy1)
        
        return numInRoman

sol = Solution()
print(sol.intToRoman(9))
print(sol.intToRoman(3))
print(sol.intToRoman(58))
print(sol.intToRoman(1994))
