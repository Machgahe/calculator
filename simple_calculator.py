from stack import Stack

class SimpleCalculator:
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
    
    def tokenize(self, input_string):
        tokens = []
        token = ""

        for char in input_string:
            if char == ' ':
                continue

            if char in ['(', ')', '+', '-', '*', '/']:
                if token:
                    tokens.append(token)
                    token = ""
                tokens.append(char)
            else:
                token += char

        if token:
            tokens.append(token)

        return tokens

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
            if tokens[i].isdigit() or self.is_float(tokens[i]):
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



# calculator = SimpleCalculator()
# answer = calculator.evaluate_expression("2 + 3") # answer should be 5.0
# answer = calculator.evaluate_expression("2 +") # answer should be "Error"
# history = calculator.get_history() # history should be [("2 +", "Error"), ("2 + 3", 5.0)]

# print(history)