import re

OPER_PADDING = 1
PROBLEM_PADDING = 4

def arithmetic_arranger(problems: str, show_solution: bool = False):
  """
  Rules
  The function will return the correct conversion if the supplied problems are properly formatted, otherwise, it will return a string that describes an error that is meaningful to the user.

  Situations that will return an error:
  - If there are too many problems supplied to the function. The limit is five, anything more will return: Error: Too many problems.
  - The approperiate operators the function will accept are addition and subtraction. Multiplication and division will return an error. Other operators not mentioned in this bullet point will not need to be tested. The error returned will be: Error: Operator must be '+' or '-'.
  - Each number (operand) should only contain digits. Otherwise, the function will return: Error: Numbers must only contain digits.
  - Each operand (aka number on each side of the operator) has a max of four digits in width. Otherwise, the error string returned will be: Error: Numbers cannot be more than four digits.
  - If the user supplied the correct format of problems, the conversion you return will follow these rules:
  - There should be a single space between the operator and the longest of the two operands, the operator will be on the same line as the second operand, both operands will be in the same order as provided (the first will be the top one and the second will be the bottom).
  - Numbers should be right-aligned.
  - There should be four spaces between each problem.
  - There should be dashes at the bottom of each problem. The dashes should run along the entire length of each problem individually. (The example above shows what this should look like.)"""
  if len(problems) > 5:
    return 'Error: Too many problems.'

  top = ''
  middle = ''
  bottom = ''
  solution = ''
  
  for problem in problems:
    components = problem.split(' ')
    x = components[0]
    oper = components[1]
    y = components[2]
    max_len = maximum(len(x), len(y))
    msg = validate_oper(oper)
    if msg != None : return msg
    msg = validate_num(x)
    if msg != None : return msg
    msg = validate_num(y)
    if msg != None : return msg
    msg = validate_len(x)
    if msg != None : return msg
    msg = validate_len(y)
    if msg != None : return msg
    top += top_formatter(x, max_len)
    middle += middle_formatter(y, max_len, oper)
    bottom += line_formatter(max_len)
    solution += solution_formatter(x, y, oper, max_len)

  arranged_problems = top[4:]
  arranged_problems += '\n'+middle[4:]
  arranged_problems += '\n'+bottom[4:]
  arranged_problems += '\n'+solution[4:] if show_solution else ''

  return arranged_problems

def maximum(x: str, y: str):
  """Return the max of two values."""
  if x > y:
    return x
  else:
    return y
    
def validate_oper(oper: str):
  """Verify operator is + or -."""
  if not oper in '+-':
    return "Error: Operator must be '+' or '-'."

def validate_num(num: str):
  """Validate input is a number."""
  if not num.isnumeric():
    return 'Error: Numbers must only contain digits.'

def validate_len(num: str):
  """Validate number of problems is 4 or less."""
  if len(num) > 4:
    return 'Error: Numbers cannot be more than four digits.'

def top_formatter(num: str, max_len: int):
  """Format top row of output."""
  return (' ' * PROBLEM_PADDING) + ' ' + (' ' * (max_len + OPER_PADDING - len(num))) + num

def middle_formatter(num: str, max_len: int, oper: str):
  """Format middle row of output."""
  return (' ' * PROBLEM_PADDING) + oper + (' ' * (max_len + OPER_PADDING - len(num))) + num

def line_formatter(max_len: int):
  """Format line row of output."""
  return (' ' * PROBLEM_PADDING) + '-' * (max_len + OPER_PADDING + 1)

def solution_formatter(x: str, y: str, oper: str, max_len: int):
  """Format solution row of output."""
  num1 = int(x)
  num2 = int(y)
  total = -1
  if oper == '+':
      total = str(num1 + num2)
  elif oper == '-':
      total = str(num1 - num2)
  total_len = len(total)
  return (' ' * PROBLEM_PADDING) + ' ' * (max_len + OPER_PADDING + 1 - total_len) + total