#
# @lc app=leetcode id=225 lang=python3
#
# [225] Implement Stack using Queues
#
# https://leetcode.com/problems/implement-stack-using-queues/description/
#
# algorithms
# Easy (67.34%)
# Likes:    6500
# Dislikes: 1256
# Total Accepted:    917.8K
# Total Submissions: 1.4M
# Testcase Example:  '["MyStack","push","push","top","pop","empty"]\n[[],[1],[2],[],[],[]]'
#
# Implement a last-in-first-out (LIFO) stack using only two queues. The
# implemented stack should support all the functions of a normal stack (push,
# top, pop, and empty).
# 
# Implement the MyStack class:
# 
# 
# void push(int x) Pushes element x to the top of the stack.
# int pop() Removes the element on the top of the stack and returns it.
# int top() Returns the element on the top of the stack.
# boolean empty() Returns true if the stack is empty, false otherwise.
# 
# 
# Notes:
# 
# 
# You must use only standard operations of a queue, which means that only push
# to back, peek/pop from front, size and is empty operations are valid.
# Depending on your language, the queue may not be supported natively. You may
# simulate a queue using a list or deque (double-ended queue) as long as you
# use only a queue's standard operations.
# 
# 
# 
# Example 1:
# 
# 
# Input
# ["MyStack", "push", "push", "top", "pop", "empty"]
# [[], [1], [2], [], [], []]
# Output
# [null, null, null, 2, 2, false]
# 
# Explanation
# MyStack myStack = new MyStack();
# myStack.push(1);
# myStack.push(2);
# myStack.top(); // return 2
# myStack.pop(); // return 2
# myStack.empty(); // return False
# 
# 
# 
# Constraints:
# 
# 
# 1 <= x <= 9
# At most 100 calls will be made to push, pop, top, and empty.
# All the calls to pop and top are valid.
# 
# 
# 
# Follow-up: Can you implement the stack using only one queue?
# 
#

# @lc code=start
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class MyStack:
    def __init__(self):
        self.top_node = None  # Changed from self.top to avoid conflict
        self.height = 0

    def push(self, x: int) -> None:
        new_node = Node(x)
        if self.top_node is None:
            self.top_node = new_node
        else:
            new_node.next = self.top_node
            self.top_node = new_node
        self.height += 1

    def pop(self) -> int:
        if self.top_node is None:
            return None  # or raise an exception
        temp = self.top_node
        self.top_node = self.top_node.next
        temp.next = None
        self.height -= 1
        return temp.value  # Return the value, not the node

    def top(self) -> int:
        if self.top_node is None:
            return None  # or raise an exception
        return self.top_node.value  # Return the value, not the node

    def empty(self) -> bool:
        
        return self.height == 0  # Simplified




# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end

