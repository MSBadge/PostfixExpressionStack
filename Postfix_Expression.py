#  Postfix Expression Evaluator
stack = []
operators = {'+','-','*','/'}

#  Read postfix expression from user
expression = input("Enter Expression: ")

# Operations on stack
def operations(tokan, operation1, operation2):
    if tokan == '+':
        result = operation1 + operation2
    elif tokan == '-':
        result = operation1 - operation2
    elif tokan == '*':
        result = operation1 * operation2
    elif tokan == '/':
        result = operation1 / operation2
    stack.append(result)

# #  Postfix Expression Evaluator using stack
def postfix_evaluator(expression):
    tokens = expression.split()

    for token in tokens:
        if token in operators:
            # Push operands, pop for operators
            operation2 = stack.pop()
            operation1 = stack.pop()
            # function call of operations
            operations(token,operation1, operation2)
        else:
            stack.append(int(token))
    return stack[0]

result = postfix_evaluator(expression)
# Display the evaluation result
print("Evaluation Result: ",result)