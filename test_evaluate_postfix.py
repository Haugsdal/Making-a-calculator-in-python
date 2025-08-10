import evaluate_postfix

def test_evaluate_postfix():

    if evaluate_postfix.evaluate_postfix("12+") == 3:
        print("JADDA")
    else:
        print("Buuuuuuuuu")

    if evaluate_postfix.evaluate_postfix("467-*") == 4:
        print("JADDA")
    else:
        print("Buuuuuuuuu")