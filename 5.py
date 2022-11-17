class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = ""
        for i in range(len(s)):
            string = self.solve(s,i,i)
            if(len(string)>len(start)):
                start = string
            string = self.solve(s,i,i+1)
            if(len(string)>len(start)):
                start = string
        return start
    def solve(self,Text:str,left:int,right:int) -> str:
        while left>=0 and right<len(Text) and Text[left] == Text[right]:
            left -= 1
            right += 1
        return Text[left+1:right]
                