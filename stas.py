import re

def lexical_analysis(source_code):
    intermediate_code = ""
    error_messages = []
    error_line = None

    keyword_pattern = re.compile(r'\b(int|for)\b')
    identifier_pattern = re.compile(r'\b[a-zA-Z_]\w*\b')
    operator_pattern = re.compile(r'[\+\-\*/=<>(){}]|(\+\+)|(\-\-)')
    number_pattern = re.compile(r'\b\d+\b')

    identifiers = set()
    keywords = {'int', 'for'}

    declared_variables = set()

    open_braces_count = 0
    open_parentheses_count = 0

    expected_indent = 0
    update_indent_next_line = False

    for line_number, line in enumerate(source_code.split('\n'), start=1):
        if line.strip():  # Проверяем, не пустая ли строка
            actual_indent = len(line) - len(line.lstrip(' '))

            # Уменьшаем табуляцию для строк, начинающихся с закрывающей фигурной скобки
            if line.lstrip().startswith('}'):
                expected_indent -= 4

            # Проверка соответствия текущей табуляции ожидаемому уровню
            if actual_indent != expected_indent:
                error_messages.append(
                    f'Error: Неверная табуляция на строке {line_number}. Ожидается {expected_indent} пробелов.')

            # Подготовка к обновлению ожидаемого уровня табуляции
            if '{' in line:
                update_indent_next_line = True
            elif '}' in line:
                update_indent_next_line = False

            # Обновляем табуляцию для следующей строки, если нужно
            if update_indent_next_line:
                expected_indent += 4
                update_indent_next_line = False

        # Если нужно обновить табуляцию для следующей строки
        if update_indent_next_line:
            expected_indent += 4
            update_indent_next_line = False

        tokens = re.findall(r'\b\w+\b|[^\w\s]', line)

        for i, token in enumerate(tokens):

            if token == 'int' and i < len(tokens) - 1 and tokens[i + 1] in keywords:
                error_messages.append(
                    f'Error: Использование ключевого слова "{tokens[i + 1]}" в качестве имени переменной после "int" на строке {line_number}.')
                error_line = line_number
                break
            if token in keywords:
                intermediate_code += f'keyword -> {token}\n'
            elif identifier_pattern.match(token):
                if i + 2 < len(tokens) and tokens[i + 1] == '+' and tokens[i + 2] == '+':
                    intermediate_code += f'increment -> {token}++\n'
                    tokens[i + 1], tokens[i + 2] = "", ""  # Удалить обработанные токены
                else:
                    if token not in declared_variables:
                        declared_variables.add(token)
                    intermediate_code += f'variable -> {token}\n'
            elif token == '+' and (i == 0 or tokens[i - 1] != '+' and tokens[i - 1] not in identifiers):
                intermediate_code += f'operator -> {token}\n'
            elif operator_pattern.match(token):
                intermediate_code += f'operator -> {token}\n'
            elif number_pattern.match(token):
                intermediate_code += f'number -> {token}\n'

        open_braces_count += line.count('{')
        open_braces_count -= line.count('}')
        open_parentheses_count += line.count('(')
        open_parentheses_count -= line.count(')')

        # Проверка наличия открывающей и закрывающей скобок у цикла
        if '(int' in line and not re.search(r'\bfor\b\s*\(', line):
            error_messages.append(
                f'Error: Отсутствие ключевого слова "for" перед открывающейся круглой скобкой на строке {line_number}.')
            error_line = line_number

    # Проверка наличия лишних скобок
    if open_braces_count > 0:
        error_messages.append(f'Error: Нету закрывающей фигурной скобки на строке {line_number + 1}.')
    elif open_braces_count < 0:
        error_messages.append(f'Error: Нету открывающей фигурной скобки на строке {line_number + 1}.')

    if open_parentheses_count > 0:
        error_messages.append(f'Error: Нету закрывающей круглой скобки на строке {line_number + 1}.')
    elif open_parentheses_count < 0:
        error_messages.append(f'Error: Нету открывающей круглой скобки на строке {line_number + 1}.')



    # Если нет ошибок, записываем идентификаторы в файл
    if not error_messages:
        with open('C:/Users/Anton/Desktop/lab11.txt', 'w') as file:
            file.write(intermediate_code)

    return error_messages, error_line

# Пример использования
source_code = '''
int main(){
    int x = 5;  
    for (int i = 0; i < 10; i++){
        x = i;
    }
}
'''

errors, error_line = lexical_analysis(source_code)
for error in errors:
    print(error)

if error_line:
    print(f'Ошибка обнаружена на строке {error_line}.')