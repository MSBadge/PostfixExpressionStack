
def postfix_evaluate(expression):
    # creat stack using list
    stack = []
    operators = {'+', '-', '*', '/'}

    tokens = expression.split()

    for token in tokens:
        if token in operators:
            # Pop two operands from the stack
            operand2 = stack.pop()
            operand1 = stack.pop()
            # Perform the operation
            if token == '+':
                result = operand1 + operand2
            elif token == '-':
                result = operand1 - operand2
            elif token == '*':
                result = operand1 * operand2
            elif token == '/':
                result = operand1 / operand2
            # Push the result back onto the stack
            stack.append(result)
        else:
            # Token is an operand, convert it to an integer and push it onto the stack
            stack.append(int(token))

    # The final result is the only element left on the stack
    return stack[0]

expression = input("Enter Expression: ")
result = postfix_evaluate(expression)

print("Evaluation Result: ",result)