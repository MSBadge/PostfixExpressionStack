stack = []
operators = {'+','-','*','/'}

while True:
     # Input of tokan form user
     user = input("Enter a Tokan: ")
     # when type 's' then stop the loop of Input
     if user.lower() == 's':
         break
     stack.append(user)

tokans = stack[0:]

# Operation perform on expression
for value in tokans:
    if value in operators:
        b = stack.pop()
        a = stack.pop()
        if value == '+':
            result = a + b
        elif value == '-':
            result = a - b
        elif value == '*':
            result = a * b
        elif value == '/':
            result = a / b
        stack.append(result)
    else:
        stack.append(int(value))
# Display the evaluation result
print("Evaluation Result: ",stack[-1])