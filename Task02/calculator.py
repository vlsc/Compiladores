from token_type import TokenType

class Calculator:
    def __init__(self, tokenList):
        self.list = tokenList
        self.stack = []

    def calculate(self):
        for token in self.list:
            if type(token) == str:
                return self.list
            if token.type == TokenType.PLUS:
                second_operand = self.stack.pop()
                first_operand = self.stack.pop()
                
                result = self.sum(first_operand, second_operand)
                self.stack.append(result)
            elif token.type == TokenType.MINUS:
                second_operand = self.stack.pop()
                first_operand = self.stack.pop()
                
                result = self.sub(first_operand, second_operand)
                self.stack.append(result)
            elif token.type == TokenType.STAR:
                second_operand = self.stack.pop()
                first_operand = self.stack.pop()
                
                result = self.mul(first_operand, second_operand)
                self.stack.append(result)
            elif token.type == TokenType.SLASH:
                second_operand = self.stack.pop()
                first_operand = self.stack.pop()
                
                result = self.div(first_operand, second_operand)
                self.stack.append(result)
            elif token.type == TokenType.NUM:
                self.stack.append(float(token.lexeme))
        return f"Saída: {self.stack.pop()}"
    

    def sum(self, first_operand, second_operand):
        return first_operand + second_operand
    
    def sub(self, first_operand, second_operand):
        return first_operand - second_operand

    def mul(self, first_operand, second_operand):
        return first_operand * second_operand

    def div(self, first_operand, second_operand):
        return first_operand / second_operand