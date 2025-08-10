def evaluate_postfix(expression:list[str])-> float:
    stack = []

    for item in expression:
        if item.isdigit():
            stack.append(item)
        else:
            value_one=stack.pop()
            value_two=stack.pop()

            if item=='+':
                stack.append(int(value_one)+int(value_two))
            elif item=='-':
                stack.append(int(value_one)-int(value_two))
            elif item=='*':
                stack.append(int(value_one)*int(value_two))
            elif item=='/':
                stack.append(int(value_one)//int(value_two))


    return stack.pop()