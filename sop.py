import sys

assuat_left='left'
assuat_right='right'



class ExpressionEvaluator:
    def __init__(self):
        self.operators = {
            
            '+': (1, assuat_left, self.add),
            '-': (1, assuat_left, self.subtract),
            '*': (2, assuat_left, self.multiply),
            '/': (2, assuat_left, self.divide),
            '%': (2, assuat_left, self.modulo),
            '^': (3, assuat_right, self.power),
            'and': (4, assuat_left, self.logical_and),
            'or': (5, assuat_left, self.logical_or),
            'not': (6, assuat_right, self.logical_not),
            'xor':(5,assuat_left,self.logical_xor),
            '==': (7, assuat_left, self.equal),
            '!=': (7, assuat_left, self.not_equal),
            '<': (8, assuat_left, self.less_than),
            '<=': (8, assuat_left, self.less_than_equal),
            '>': (8, assuat_left, self.greater_than),
            '>=': (8, assuat_left, self.greater_than_equal),
            
        }

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        return x / y

    def modulo(self, x, y):
        return x % y

    def power(self, x, y):
        return x ** y

    def logical_and(self, x, y):
        return x and y

    def logical_or(self, x, y):
        return x or y

    def logical_not(self, x):
        return not x

    def equal(self, x, y):
        return x == y
    def logical_xor(self, x, y):
        return (x or y) and not (x and y)

    def not_equal(self, x, y):
        return x != y

    def less_than(self, x, y):
        return x < y

    def less_than_equal(self, x, y):
        return x <= y

    def greater_than(self, x, y):
        return x > y

    def greater_than_equal(self, x, y):
        return x >= y

    def add_operator(self, symbol, precedence, associativity, function):
        self.operators[symbol] = (precedence, associativity, function)
    
    def tokenize_expression(self, expression):
        tokens = []
        current_token = ""
    
        for char in expression:
            if char.isalnum():
                current_token += char
            elif char in self.operators or char in '()':
                if current_token:
                    tokens.append(current_token)
                    current_token = ""
                tokens.append(char)
        
        if current_token:
            tokens.append(current_token)
    
        return tokens
    
    def shunting_yard(self, tokens):
        output = []
        operators = []

        for token in tokens:
            if token.isdigit():
                output.append(float(token))
            elif token in self.operators:
                while (
                    operators
                    and operators[-1] in self.operators
                    and (
                        (self.operators[token][0] < self.operators[operators[-1]][0])
                        or (
                            self.operators[token][0] == self.operators[operators[-1]][0]
                            and self.operators[token][1] == assuat_left
                        )
                    )
                ):
                    output.append(operators.pop())
                operators.append(token)
            elif token == '(':
                operators.append(token)
            elif token == ')':
                while operators and operators[-1] != '(':
                    output.append(operators.pop())
                operators.pop()

        while operators:
            output.append(operators.pop())

        return output

    def evaluate_rpn(self, rpn):
        stack = []

        for token in rpn:
            if isinstance(token, float):
                stack.append(token)
            elif token in self.operators:
                _, _, op = self.operators[token]
                if token == 'not':
                    stack[-1] = op(stack[-1])
                else:
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(op(a, b))

        return stack[0]

    def evaluate_expression(self, expression):
        tokens = self.tokenize_expression(expression)
        postfix_tokens = self.shunting_yard(tokens)
        result = self.evaluate_rpn(postfix_tokens)
        return result

def switch_case(value):
        global assuat_left
        global assuat_right
        evaluator = ExpressionEvaluator()
        while True:
            if value == 1:
                print("Arithmetic Expression Evaluation:")
                arithmetic_expression = input("Enter arithmetic expression: ")
                assuat_left=input("Enter associativity rule: ")
                if assuat_left=='left':
                    assuat_right='right'
                elif assuat_left=='right':
                    assuat_right='left'
                while True:
                    
                        
                    customize = input("Do you want to customize operator precedence and associativity? (y/n): ").lower()
                    if customize == 'n':
                        break
                    elif customize == 'y':
                        symbol = input("Enter operator symbol: ")
                        precedence = int(input("Enter operator precedence: "))
                        if symbol=='^' or symbol =='not':
                            associativity=assuat_right
                        else: associativity=assuat_left
                        #associativity = input("Enter operator associativity (left/right): ").lower()
                        # Modify the operator if it exists, or add a new one
                        if symbol in evaluator.operators:
                            _, _, function = evaluator.operators[symbol]
                        else:
                            print("Operator not found. Adding a new one.")
                            function = lambda x, y: None  # You can define a default function for the new operator
            
                        evaluator.add_operator(symbol, precedence, associativity, function)
                    else:
                        print("Invalid input. Please enter 'y' or 'n'.")
                
                print("\nEntered Expressions:")
                print("Arithmetic: ", arithmetic_expression)
                result_arithmetic = evaluator.evaluate_expression(arithmetic_expression)
                print(f"Arithmetic Result: {result_arithmetic}")
                main();
            elif value == 2:
                print("\nLogical Expression Evaluation:")
                logical_expression = input("Enter logical expression: ")
                assuat_left=input("Enter associativity rule: ")
                while True:
                    customize = input("Do you want to customize operator precedence and associativity? (y/n): ").lower()
                    if customize == 'n':
                        break
                    elif customize == 'y':
                        symbol = input("Enter operator symbol: ")
                        precedence = int(input("Enter operator precedence: "))
                        if symbol=='^' or symbol =='not':
                            associativity=assuat_right
                        else: associativity=assuat_left
                        #associativity = input("Enter operator associativity (left/right): ").lower()
            
                        # Modify the operator if it exists, or add a new one
                        if symbol in evaluator.operators:
                            _, _, function = evaluator.operators[symbol]
                        else:
                            print("Operator not found. Adding a new one.")
                            function = lambda x, y: None  # You can define a default function for the new operator
            
                        evaluator.add_operator(symbol, precedence, associativity, function)
                    else:
                        print("Invalid input. Please enter 'y' or 'n'.")
                
                 
                print("\nEntered Expressions:")
                print("Logical: ", logical_expression)
                result_logical = evaluator.evaluate_expression(logical_expression)
                print(f"Logical Result: {result_logical}")
                main();
            elif value == 3:
                print("\nRelational Expression Evaluation:")
                relational_expression = input("Enter relational expression: ")
                assuat_left=input("Enter associativity rule: ")
                while True:
                    customize = input("Do you want to customize operator precedence and associativity? (y/n): ").lower()
                    if customize == 'n':
                        break
                    elif customize == 'y':
                        symbol = input("Enter operator symbol: ")
                        precedence = int(input("Enter operator precedence: "))
                        if symbol=='^' or symbol =='not':
                            associativity=assuat_right
                        else: associativity=assuat_left
                       # associativity = input("Enter operator associativity (left/right): ").lower()
            
                        # Modify the operator if it exists, or add a new one
                        if symbol in evaluator.operators:
                            _, _, function = evaluator.operators[symbol]
                        else:
                            print("Operator not found. Adding a new one.")
                            function = lambda x, y: None  # You can define a default function for the new operator
            
                        evaluator.add_operator(symbol, precedence, associativity, function)
                    else:
                        print("Invalid input. Please enter 'y' or 'n'.")
                
             
                # Print the entered expressions and rules
                print("\nEntered Expressions:")
                print("Relational: ", relational_expression)
                result_relational = evaluator.evaluate_expression(relational_expression)
                print(f"Relational Result: {result_relational}")
                main();
            elif value == 4:
                print("Your Exit the program :(");
                sys.exit()
                break;
            else:
                print("Invalid case. Please choose a valid case.")


def main():
    x = int(input("1-Arithmetic Expression Evaluation\n2-Logical Expression Evaluation\n3-Relational Expression Evaluation\n4-Exit\nchoose type of expression evaluation:"))
    switch_case(x);
    
if __name__ == "__main__":
    main()
