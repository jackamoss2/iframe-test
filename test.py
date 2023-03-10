
def longestPalindrome(s):
    def checkNext (palindrome, iterations):
        try:
            if i - iterations < 0:
                return palindrome
            if s[i - iterations] == s[i] or s[i] == s[i + iterations] or s[i - iterations] == s[i + iterations]:
                if s[i - iterations] == s[i]:
                    palindrome = s[i - iterations] + palindrome
                if s[i] == s[i + iterations]:
                    palindrome = palindrome + s[i + iterations]
                if s[i - iterations] == s[i + iterations]:
                    palindrome = s[i - iterations] + palindrome + s[i + iterations]
                    iterations += 1
                    palindrome = checkNext(palindrome, iterations)
            return palindrome
        except:
            return palindrome

    bestPalindrome = ""

    for i in range(len(s)):
        palindrome = checkNext(s[i], 1)
        if len(palindrome) > len(bestPalindrome):
            bestPalindrome = palindrome
            
    return bestPalindrome

print(longestPalindrome('abbabababs'))