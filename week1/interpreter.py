def main():

    # Prompt user for an expression
    expression = input("expression: ")
    x, operator, y = expression.split(" ")
    x, y = float(x), float(y)


    # Evaluate the expression based on the operator using match statement
    match operator:
        case "+":
            print(x + y)
        case "-":
            print(x - y)
        case "*":
            print(x * y)
        case "/":
            print(x / y)

main()