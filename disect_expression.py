import re
import check_validity

def disect_expression(expression):

    half_split_expression=(re.split(r"([()])",expression))
    splitted_expression=[]

    for part in half_split_expression:

        if part!="":
            valid_list_item=check_validity.check_validity(part)

            if valid_list_item:
                splitted_expression.append(part)
            else:
                print("Program crashed due to code A.")
                break

    print("final list: ",splitted_expression)
    return splitted_expression
