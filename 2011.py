class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        a=operations.count("++X")
        b=operations.count("X++")
        c=operations.count("--X") 
        d=operations.count("X--")
        return a+b-c-d