class Solution:
    def isPalindrome(self, x: int) -> bool:
        return(str(x) == str(x)[::-1])



class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return(False)
        else:
            if len(str(x))%2 == 0:
                return(str(x)[0:len(str(x))//2] == str(x)[len(str(x))//2:len(str(x))][::-1])
            else:
                return(str(x)[0:len(str(x))//2+1] == str(x)[len(str(x))//2:len(str(x))][::-1])

