class Solution:
    def longestPalindrome(self, s: str) -> str:
        if (len(s) == 1):
            return s
        longestLen = 0
        longestPalindrome = ""
        for i in range(len(s)):
            for j in range(i+1, len(s) + 1):
                if (j - i <= longestLen):
                    continue
                else:
                    if self.isPalindrome(s[i:j]):
                        longestLen = j - i
                        longestPalindrome = s[i:j]
        return longestPalindrome
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = -1
        stringLength = len(s)
        for i in range(stringLength):
            if s[left] == s[right]:
                if (left + abs(right) == stringLength or left + abs(right) == stringLength - 1):
                    return True
                left += 1
                right -= 1    
        return False

if __name__ == "__main__":
    sol = Solution()
    print(sol.longestPalindrome("abcdedtqf"))
    print(sol.longestPalindrome("abcdedtqftyuuyt"))
    print(sol.longestPalindrome("ibvjkmpyzsifuxcabqqpahjdeuzaybqsrsmbfplxycsafogotliyvhxjtkrbzqxlyfwujzhkdafhebvsdhkkdbhlhmaoxmbkqiwiusngkbdhlvxdyvnjrzvxmukvdfobzlmvnbnilnsyrgoygfdzjlymhprcpxsnxpcafctikxxybcusgjwmfklkffehbvlhvxfiddznwumxosomfbgxoruoqrhezgsgidgcfzbtdftjxeahriirqgxbhicoxavquhbkaomrroghdnfkknyigsluqebaqrtcwgmlnvmxoagisdmsokeznjsnwpxygjjptvyjjkbmkxvlivinmpnpxgmmorkasebngirckqcawgevljplkkgextudqaodwqmfljljhrujoerycoojwwgtklypicgkyaboqjfivbeqdlonxeidgxsyzugkntoevwfuxovazcyayvwbcqswzhytlmtmrtwpikgacnpkbwgfmpavzyjoxughwhvlsxsgttbcyrlkaarngeoaldsdtjncivhcfsaohmdhgbwkuemcembmlwbwquxfaiukoqvzmgoeppieztdacvwngbkcxknbytvztodbfnjhbtwpjlzuajnlzfmmujhcggpdcwdquutdiubgcvnxvgspmfumeqrofewynizvynavjzkbpkuxxvkjujectdyfwygnfsukvzflcuxxzvxzravzznpxttduajhbsyiywpqunnarabcroljwcbdydagachbobkcvudkoddldaucwruobfylfhyvjuynjrosxczgjwudpxaqwnboxgxybnngxxhibesiaxkicinikzzmonftqkcudlzfzutplbycejmkpxcygsafzkgudy"))
    print(sol.isPalindrome("abcba"))
    print(sol.isPalindrome("abcbc"))
    print(sol.isPalindrome("abba"))
    print(sol.isPalindrome("abab"))
    print(sol.isPalindrome("bb"))