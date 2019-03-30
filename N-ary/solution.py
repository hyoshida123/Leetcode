
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution(object):

    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        """
        if root is None:
            return []

        result = [root.val]

        if root.children is not None:
            for c in root.children:
                result.extend(self.preorder(c))

        return result
        """

        if root is None:
            return []

        preorder = []
        stack = [root]

        while len(stack) > 0:
            parent = stack.pop()
            while parent:
                preorder.append(parent.val)
                for i in range(len(parent.children) - 1, 0, -1):
                #for c in parent.children:
                    #stack.append(c)
                    stack.append(parent.children[i])
                parent = parent.children[0] if len(parent.children) else None

        return preorder
