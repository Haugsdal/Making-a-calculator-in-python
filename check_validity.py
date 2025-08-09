def check_validity(mini_expression):
    #Check to see if the expression contains characters that are allowed and convert it to int if everything is valid

    divided_mini_expression=[*mini_expression]
    #print("divided expression:", divided_mini_expression)
    new_expression=""
    allowed_operators=["+","-","*","/","(",")"]

    for character in divided_mini_expression:
        if character.isdigit() or character in allowed_operators:
            new_expression+=character
        else:
            print("Program crashed due to invalid character.")
            break

    return True
