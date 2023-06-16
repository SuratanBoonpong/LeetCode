class Solution:
    def interpret(self, command: str) -> str:
        d = {"(al)":"al", "()":"o","G":"G"}
        temp = ""
        output = ""
        for i in range(len(command)):
            temp += command[i]
            if(temp in d):
                output += d[temp]
                temp = ""
        return output