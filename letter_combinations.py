from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        
        twoLetters = ["a", "b", "c"]
        threeLetters = ["d", "e", "f"]
        fourLetters = ["g", "h", "i"]
        fiveLetters = ["j", "k", "l"]
        sixLetters = ["m", "n", "o"]
        sevenLetters = ["p", "q", "r", "s"]
        eightLetters = ["t", "u", "v"]
        nineLetters = ["w", "x", "y", "z"]

        lettersDict = dict()
        lettersDict["2"] = twoLetters
        lettersDict["3"] = threeLetters
        lettersDict["4"] = fourLetters
        lettersDict["5"] = fiveLetters
        lettersDict["6"] = sixLetters
        lettersDict["7"] = sevenLetters
        lettersDict["8"] = eightLetters
        lettersDict["9"] = nineLetters



""" 
Edge Cases:
    len(digits) == 0

 """