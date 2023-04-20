from token_type import TokenType
from scanner import Scanner
from calculator import Calculator


s = Scanner()
tokensList = s.scan(input("digite sua expressão: ").split(' '))

c = Calculator(tokensList)

print(c.calculate())
