from graphviz import Digraph

class Tree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def BiulTree(expression):
    def precedence(op):
        if op in ('+', '-'):
            return 1
        if op in ('*', '/'):
            return 2
        return 0

    def Operator(operators, operands):
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
                Operator(operators, operands)
            operators.append(char)
        elif char == '(':
            operators.append(char)
        elif char == ')':
            while operators[-1] != '(':
                Operator(operators, operands)
            operators.pop()
        i += 1

    while operators:
        Operator(operators, operands)

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

def VisTree(root):
    def addDeg(graph, node, counter):
        if node is None:
            return counter
        node_id = f"node{counter}"
        graph.node(node_id, str(node.value))
        current_counter = counter + 1
        if node.left:
            left_id = f"node{current_counter}"
            graph.edge(node_id, left_id)
            current_counter = addDeg(graph, node.left, current_counter)
        if node.right:
            right_id = f"node{current_counter}"
            graph.edge(node_id, right_id)
            current_counter = addDeg(graph, node.right, current_counter)
        return current_counter

    graph = Digraph(format="png")
    addDeg(graph, root, 0)
    return graph

expression = input("ВВедите выражение:")
tree = BiulTree(expression)
result = VisTree(tree)
print(f"Результат выражения: {result}")

graph = VisTree(tree)
graph.render("expression_tree", view=True)
