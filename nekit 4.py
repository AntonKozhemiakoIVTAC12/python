opers = ['<', '>', '+', '/', '-', '*', '=', ".", ",", ":=", "<=", ">=", "<>"]
new_line = []
result = ''
for_flag = False
in_for_block = False
count_tab = 0
list_of_variables = []
error = ''
begEnd = 0
forDo = 0
real_deep = 0
file_path = 'output1.txt'
cycle_body = False
iterator = False
lvl = 0

with open(file_path, 'r') as file:
    lines = file.readlines()
    for i, line in enumerate(lines):
        lines[i] = lines[i].replace('|-->', ' ').strip()
        new_line = line.strip().split(' ')
        count_tab = len(line) - len(line.strip())
        if for_flag:
            count_tab += 4
        if in_for_block:
            # Если мы уже внутри блока, пропускаем строки до тех пор, пока не встретим конец блока
            if line.strip() == '|-->Body':
                cycle_body = True
                in_for_block = False
            continue
        if iterator:
            lvl += 1
            if lvl == 4:
                lvl = 0
                iterator = False
            continue

        if new_line[0].startswith('|-->') and any(new_line[0].endswith(op) for op in opers):
            iter_var = lines[i + 1].strip().rstrip(',;')
            start_val = lines[i + 2].strip().rstrip(',;')
            result += f'\t{iter_var} = {start_val}\n'
        elif new_line[0] == '|-->for':
            iter_var = lines[i + 4].strip().rstrip(',;')
            start_val = lines[i + 7].strip().rstrip(',;')
            end_val = lines[i + 5].strip().rstrip(',;')
            result += f"for {iter_var} in range({start_val}): \n" + '' * count_tab + '' * 4
            for_flag = True
            in_for_block = True

        elif cycle_body:
            if new_line[0].startswith('|-->') and any(new_line[0].endswith(op) for op in opers):
                iter_var = lines[i + 1].strip().rstrip(',;')
                start_val = lines[i + 2].strip().rstrip(',;')
                if start_val.replace('|-->', '').strip() in opers:
                    oper = start_val
                    lines[i + 3] = iter_var
                    end_val = lines[i + 4].strip().rstrip(',;')
                    result += f'\t\t{iter_var} = {iter_var} {oper} {end_val};\n'
                    iterator = True
                else:
                    result += f'\t\t{iter_var} = {start_val};\n'

    result = result.replace('|-->', '').strip()
    result = result.replace(f'{" " * count_tab}', '').strip()
    with open("output2.txt", "w") as output_file:
        if error != '':
            output_file.write(error)
        else:
            output_file.write(result)
