# class Stack:
# 	def __init__(self):
# 		# Initialise the stack's data attributes
# 		pass
	
# 	def push(self, item):
# 		# Push an item to the stack
# 		pass

# 	def peek(self):
# 		# Return the element at the top of the stack
# 		# Return a string "Error" if stack is empty
# 		pass

# 	def pop(self):
# 		# Pop an item from the stack if non-empty
# 		pass

# 	def is_empty(self):
# 		# Return True if stack is empty, False otherwise
# 		pass

# 	def __str__(self):
# 		# Return a string containing elements of current stack in top-to-bottom order, separated by spaces
# 		# Example, if we push "2" and then "3" to the stack (and don't pop any elements), 
# 		# then the string returned should be "3 2"
# 		pass

# 	def __len__(self):
# 		# Return current number of elements in the stack
# 		pass

# class Stack:
#     def __init__(self):
#         self.stack = []

#     def push(self, item):
#         self.stack.append(item)

#     def peek(self):
#         if self.is_empty():
#             return "Error"
#         return self.stack[-1]

#     def pop(self):
#         if self.is_empty():
#             return "Error"
#         return self.stack.pop()

#     def is_empty(self):
#         return len(self.stack) == 0

#     def __str__(self):
#         return " ".join(str(item) for item in self.stack[::-1])

#     def __len__(self):
#         return len(self.stack)


class Stack:
    def __init__(self):
        self._data = []
        self._length = 0
        self._pointer = 0

    def is_empty(self):
        return self._length == 0

    def __len__(self):
        return self._length

    def pop(self):
        if self.is_empty():
            raise ValueError("Stack is Empty")
        self._length -= 1
        return self._data.pop()

    def peek(self):
        if self.is_empty():
            raise ValueError("Stack is Empty")
        return self._data[self._length-1]

    def push(self, item):
        self._data.append(item)
        self._length += 1

    def __str__(self):
        return ", ".join(map(str,self._data))