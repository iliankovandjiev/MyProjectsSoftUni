sequence_of_parentheses = [par for par in input()]
open_parentheses = []


for parentheses in sequence_of_parentheses:

    if parentheses in '{[(':
        open_parentheses.append(parentheses)

    else:

        if open_parentheses:
            close_parentheses = open_parentheses.pop()
            if (close_parentheses + parentheses) not in '(){}[]':
                print("NO")
                exit()
        else:
            print("NO")
            exit()

print("YES")