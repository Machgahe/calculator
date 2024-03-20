from simple_calculator import SimpleCalculator
from stack import Stack
import re

class AdvancedCalculator(SimpleCalculator):
    def __init__(self):
        self.history = []

    def evaluate_expression(self, input_expression):
        """
        Evaluate the input expression and return the output as a float
        Return a string "Error" if the expression is invalid
        """
        tokens = self.tokenize(input_expression)
        if not self.check_brackets(tokens):
            return "Error"
        else:
            result = self.evaluate_list_tokens(tokens)
        self.history.insert(0, (input_expression, result))
        return result
    

    def tokenize(self, expression):
        elements = re.findall(r'\d+\.\d+|\d+|\S', expression)
        extracted = []

        for element in elements:
            if re.match(r'\d+\.\d+', element):
                extracted.append(float(element))
            elif re.match(r'\d+', element):
                extracted.append(int(element))
            else:
                extracted.append(element)

        return extracted


    def check_brackets(self, tokens):
        """
        Check if the input expression has balanced brackets
        """
        stack = Stack()
        for token in tokens:
            if token == "(":
                stack.push(token)
            elif token == ")":
                if stack.is_empty() or stack.peek() != "(":
                    return False
                stack.pop()
        if not stack.is_empty():
            return False
        
        return True

    def evaluate_list_tokens(self, tokens):
        """
        Evaluate the input list of tokens and return the output as a float
        """
        stack = Stack()
        i = 0
        while i < len(tokens):
            if isinstance(tokens[i], int) or self.is_float(tokens[i]):
                stack.push(float(tokens[i]))
            elif tokens[i] in ['+', '-', '*', '/']:
                operand1 = stack.pop()
                if i <len(tokens)-1 and (tokens[i+1].isdigit() or self.is_float(tokens[i+1])):
                    stack.push(float(tokens[i+1]))
                else:
                    return "Error"
                operand2 = stack.pop()
                result = self.evaluate_operator(tokens[i], operand1, operand2)
                i += 1
                stack.push(result)
            else:
                return "Error"
            i += 1
        if len(stack) == 1:
            return stack.pop()
        else:
            return "Error"

    def evaluate_operator(self, operator, operand1, operand2):
        """
        Evaluate the input operator and operands and return the output as a float
        """
        if operator == "+":
            return operand1 + operand2
        elif operator == "-":
            return operand1 - operand2
        elif operator == "*":
            return operand1 * operand2
        elif operator == "/":
            return operand1 / operand2
        else:
            return "Error"

    def is_float(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    def get_history(self):
        """
        Return a list of the most recent expressions that have been evaluated
        """
        return self.history

	
# from simple_calculator import SimpleCalculator
# from stack import Stack

# class AdvancedCalculator(SimpleCalculator):
#     def __init__(self):
#         super().__init__()
#         # Instantiate any additional data attributes

#     def evaluate_expression(self, input_expression):
#         # Evaluate the input expression and return the output as a float
#         # Return the string "Error" if the expression is invalid
#         list_tokens = self.tokenize(input_expression)
#         if list_tokens is None or not self.check_brackets(list_tokens):
#             return "Error"
#         else:
#             result = self.evaluate_list_tokens(list_tokens)
#         self.history.insert(0, (input_expression, result))
#         return result

#     def tokenize(self, expression):
#         # Tokenize the expression into a list of operands, operators, and parentheses
#         tokens = []
#         current_token = ""

#         for char in expression:
#             if char.isdigit() or char == '.':
#                 current_token += char
#             elif char in ['+', '-', '*', '/']:
#                 if current_token:
#                     tokens.append(current_token)
#                     current_token = ""
#                 tokens.append(char)
#             elif char in ['(', ')']:
#                 if current_token:
#                     tokens.append(current_token)
#                     current_token = ""
#                 tokens.append(char)
#             elif char != ' ':
#                 raise ValueError("Invalid character in expression")

#         if current_token:
#             tokens.append(current_token)

#         return tokens

#     def check_brackets(self, list_tokens):
#         # Check if brackets are valid, that is, all open brackets are closed by the same type of brackets
#         # Also, () should contain only () brackets
#         stack = Stack()
#         for token in list_tokens:
#             if token == "(":
#                 stack.push(token)
#             elif token == ")":
#                 if stack.is_empty() or stack.peek() != "(":
#                     return False
#                 stack.pop()
        
#         # Check if there are any remaining open brackets
#         if not stack.is_empty():
#             return False
        
#         return True

#     def evaluate_list_tokens(self, list_tokens):
#         # Evaluate the expression passed as a list of tokens
#         # Return the final answer as a float, and "Error" in case of division by zero and other errors
#         operators = {"+": lambda x, y: x + y, "-": lambda x, y: x - y, "*": lambda x, y: x * y, "/": lambda x, y: x / y}
#         stack = Stack()
#         for token in list_tokens:
#             if token == "(":
#                 stack.push(token)
#             elif token == ")":
#                 sub_expression = []
#                 while not stack.is_empty() and stack.peek() != "(":
#                     sub_expression.insert(0, stack.pop())
#                 if stack.is_empty() or stack.peek() != "(":
#                     return "Error"
#                 stack.pop()  # Discard the opening "("
#                 result = self.evaluate_list_tokens(sub_expression)
#                 stack.push(result)
#             elif token in operators:
# 	            if len(stack) < 2:
#                     return "Error"
#                 operand2 = float(stack.pop())
# 				operand1 = float(stack.pop())
#                 if token == "/" and operand2 == 0:
# 					return "Error"
# 				result = operators[token](operand1, operand2)
# 				stack.push(result)
#         	else:
# 				stack.push(token)
#         if len(stack) != 1 or isinstance(stack.peek(), str):
			
                    
    

#     def get_history(self):
#         # Return the history of expressions evaluated as a list of (expression, output) tuples
#         # The order should be such that the most recently evaluated expression appears first
#         return self.history

calculator = AdvancedCalculator()
answer = calculator.evaluate_expression("2 + (3 /4)") # answer should be 2.75
# answer = calculator.evaluate_expression("2 +") # answer should be "Error"
tokens = calculator.tokenize("2 + 3") # tokens should be [2, '+', 3]
# answer = calculator.evaluate_list_tokens([2, '+', 3]) # answer should be 5.0
correct_brackets = calculator.check_brackets(['(', 2, '*']) # should be False
history = calculator.get_history() # history should be [("2 +", "Error"), ("2 + (3 /4)", 2.75)]

print(answer)
print(tokens)
print(correct_brackets)
print(history)