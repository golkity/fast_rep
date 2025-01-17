class Tree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def BiuldTree(expression):
    def precedence(op):
        if op in ('+', '-'):
            return 1
        if op in ('*', '/'):
            return 2
        return 0

    def Oper(operators, operands):
        right = operands.pop()
        left = operands.pop()
        operator = operators.pop()
        node = Tree(operator)
        node.left = left
        node.right = right
        operands.append(node)

    operators = []
    operands = []
    i = 0
    while i < len(expression):
        char = expression[i]
        if char.isdigit():
            num = 0
            while i < len(expression) and expression[i].isdigit():
                num = num * 10 + int(expression[i])
                i += 1
            operands.append(Tree(num))
            continue
        elif char in ('+', '-', '*', '/'):
            while (operators and precedence(operators[-1]) >= precedence(char)):
                Oper(operators, operands)
            operators.append(char)
        elif char == '(':
            operators.append(char)
        elif char == ')':
            while operators[-1] != '(':
                Oper(operators, operands)
            operators.pop()
        i += 1

    while operators:
        Oper(operators, operands)

    return operands[0]

def EvalTree(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return int(root.value)
    left_val = EvalTree(root.left)
    right_val = EvalTree(root.right)
    if root.value == '+':
        return left_val + right_val
    elif root.value == '-':
        return left_val - right_val
    elif root.value == '*':
        return left_val * right_val
    elif root.value == '/':
        return left_val / right_val

expression = input("Ввод вырожения:")
tree = BiuldTree(expression)
result = EvalTree(tree)
print(f"Результат выражения '{expression}' равен {result}")
