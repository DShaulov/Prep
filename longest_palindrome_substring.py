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
        return s == s[::-1]     

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