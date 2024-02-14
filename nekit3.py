import re

def lexer_analysis(code):
    keyword_set = {'int', 'float', 'char', 'for', 'if', 'else', 'main'}
    operator_set = {'+', '-', '*', '/', '{', '}', '(', ')', 'cin', 'cout', ';', ','}
    variables = set()
    numbers = set()
    errors = []

    tokens = re.findall('[A-Za-z_][A-Za-z0-9_]*|[-+*/cin{}cout;,()]|[0-9]+', code)

    for token in tokens:
        if token in keyword_set:
            # Check for formatting errors
            if token != 'main':
                errors.append(f"Error: Unexpected keyword '{token}' outside of main function.")
        elif token in operator_set:
            pass  # No error checking for operators in this example
        elif token.isdigit():
            numbers.add(token)
        else:
            # Check for variable naming errors
            if not re.match('^[A-Za-z_][A-Za-z0-9_]*$', token):
                errors.append(f"Error: Invalid variable name '{token}'.")
            variables.add(token)

    # Check for undeclared variables
    for variable in variables:
        if variable not in numbers:
            errors.append(f"Error: Variable '{variable}' used without declaration.")

    return variables, keyword_set, operator_set, numbers, errors


def write_to_file(variables, keyword_set, operator_set, numbers, errors, output_file):
    with open(output_file, 'w') as file:
        if errors:
            file.write('\n'.join(errors))
        else:
            file.write(f'Variables: {", ".join(variables)}\n')
            file.write(f'Keywords: {", ".join(keyword_set)}\n')
            file.write(f'Operators: {", ".join(operator_set)}\n')
            file.write(f'Numbers: {", ".join(numbers)}\n')


if __name__ == "__main__":
    with open('C:/Users/Anton/Desktop/lab1.txt', 'r') as input_file:
        code = input_file.read()

    variables, keyword_set, operator_set, numbers, errors = lexer_analysis(code)
    write_to_file(variables, keyword_set, operator_set, numbers, errors, 'C:/Users/Anton/Desktop/lab11.txt')
