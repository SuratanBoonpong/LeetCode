class Solution:
    def removeDuplicates(self, s: str) -> str:
        inputList = [x for x in s]
        stack = []
        Str = ""
        for i in inputList:
            if len(stack) > 0 and stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
               
        return Str.join(stack)