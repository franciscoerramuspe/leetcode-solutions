'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

we need two arrays: a stack and a min array
for getMin, we would get the last element of min array
when we pop, we pop from both arrays
when we push, we have to push to both arrays:
    for the stack array we push the value we received
    for the min array we push the value we received if it is smaller than the prvious min else we push the prev min again


'''
class MinStack:
    def __init__(self):
        self.stack=[]
        self.minS=[]
    
    def push(self, val):
        self.stack.append(val)
        if not self.minS or self.minS[-1]>val:
                self.minS.append(val)
        else:
            self.minS.append(self.minS[-1])
    
    def pop(self):
        self.stack.pop()
        self.minS.pop()
    
    def top(self):
        return self.stack[-1]
    
    def getMin(self):
        return self.minS[-1]

stack=MinStack()
stack.push(5)
stack.push(3)
print(stack.getMin())
stack.push(4)
stack.push(0)
print(stack.getMin())
stack.pop()
print(stack.getMin())
print(stack.top())
