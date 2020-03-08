class BinaryTreeNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

    def dfs(self, root_node):
        max = 0
        stack = [root_node]
        second_largest = 0
        while stack:
            current = stack.pop()
            # print(current.value)
            if current.left:
                left_node = current.left
                stack.append(left_node)
            if current.right:
                right_node = current.right
                stack.append(right_node)
            # print("cuurent value {} max {} ".format(current.value, max))
            if current.value > max:
                # print(current.value)
                second_largest = max
                max = current.value

            if second_largest < current.value < max:
                second_largest = current.value

        return second_largest

    def bfs(self,root_node):
        _que = [root_node]
        max = 0
        second_largest = 0
        while _que:
            current = _que.pop(0)
            if current.left:
                left_node = current.left
                _que.append(left_node)
            if current.right:
                right_node = current.right
                _que.append(right_node)

            if current.value > max:
                # print(current.value)
                second_largest = max
                max = current.value

            if second_largest < current.value < max:
                second_largest = current.value

        return second_largest


_Node = BinaryTreeNode(0)
node_left = _Node.insert_left(1)
node_right = _Node.insert_right(2)
_ = node_left.insert_right(3)
_ = node_left.insert_left(5)
_ = node_right.insert_left(4)
_ = node_right.insert_right(6)
print(_Node.dfs(_Node))



