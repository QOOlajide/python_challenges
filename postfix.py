def evalPostfixNotation(tokens):
    stack = []
    #why? Well, typically stack problems are usually meant for matching values to other values and having a large stack of unattended problems. In this case, you have numbers and operands and incoming operators which are meant to perform operations using those operands.
    #Typically, here, I'd create a dictionary if I wanted to pair some things or even remember certain values. But I won't be doing that because the values I'd typically be storing will instantly be pushed to the stack once I perform the operation.
    for token in tokens:
    #since we've already established that a dictionary is not needed, we need to iterate over the values. We have strings which are guaranteed to be integers should we remove the string attribute from them. However, we need to check if we're pushing an actual integer. This mimics a common theme with stack problems: Instead of selectively handling values in the array, we'll push every number onto the stack.
        if len(token) > 1 or token.isdigit():
            #We use the or because both cases represent numeric instances
            stack.append(int(token))
        else:
            right = stack.pop()
            left = stack.pop()
            if token == "+":
                stack.append(int(left) + int(right))
                #unnecessary considering all the values inside the stack are integers
            elif token == "*":
                stack.append(left * right)
            elif token == "-":
                stack.append(left - right)
            else:
                stack.append(left / right)
    return stack[0]
