from token import Token
from token_type import TokenType
from regex import Regex

class Scanner:
    def __init__(self):
        self.tokenList = []

    def scan(self, expression):
        r = Regex()
        for e in expression:
            if r.is_number(e):
                self.tokenList.append(Token(TokenType.NUM, e))
            elif r.is_op(e):
                if r.is_sum(e):
                    self.tokenList.append(Token(TokenType.PLUS, e))
                elif r.is_sub(e):
                    self.tokenList.append(Token(TokenType.MINUS, e))
                elif r.is_div(e):
                    self.tokenList.append(Token(TokenType.SLASH, e))
                else:
                    self.tokenList.append(Token(TokenType.STAR, e))
            else:
                return f"Error: Unexpected character: {e}"
        
        return self.tokenList