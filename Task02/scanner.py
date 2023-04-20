from token import Token
from token_type import TokenType

class Scanner:
    def __init__(self):
        self.tokenList = []
        self.operators = ['+', '-', '*', '/']
    

    def scan(self, expression):
        for e in expression:
            if e in self.operators:
                    if e == '+':
                        self.tokenList.append(Token(TokenType.PLUS, e))
                    elif e == '-':
                        self.tokenList.append(Token(TokenType.MINUS, e))
                    elif e == '*':
                        self.tokenList.append(Token(TokenType.STAR, e))
                    else:
                        self.tokenList.append(Token(TokenType.SLASH, e))
            else:
                try:
                    float(e)
                    self.tokenList.append(Token(TokenType.NUM, e))
                except:
                    return f"Error: Unexpected character: {e}"
        
        return self.tokenList