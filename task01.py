def calc(o, first, second):
  if o == '+':
    return first + second
  elif o == '-':
    return first - second
  elif o == '*':
    return first * second
  else:
    return first / second


def calculator(expression):
  operators = ['+','-','*','/']
  stack = []
  for e in expression:
    if e in operators:
      first_operand = float(stack.pop())
      second_operand = float(stack.pop())
      result = calc(e, first_operand, second_operand)
      stack.append(result)
    else:
      stack.append(e)
  return stack.pop()

# assumindo que numeros negativos nao terao espaco entre o - e o modulo do numero
# exemplo: 10 -10 + resulta em 0
expression = input("Digite sua expressão: ").split(' ')
print(calculator(expression))
