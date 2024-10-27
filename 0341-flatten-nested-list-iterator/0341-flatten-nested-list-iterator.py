# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = [iter(nestedList)]
        self.nextEl = None
    
    def next(self) -> int:
        result = self.nextEl
        self.nextEl = None
        return result
        
    
    def hasNext(self) -> bool:
        while self.stack:
            try:
                top = next(self.stack[-1])
                
                if top.isInteger():
                    self.nextEl = top.getInteger()
                    return True
                else:
                    self.stack.append(iter(top.getList()))
            except StopIteration:
                self.stack.pop()
        return False
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())