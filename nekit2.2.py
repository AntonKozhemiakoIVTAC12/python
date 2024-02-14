import ast
import re


file_path = 'C:/Users/Anton/Desktop/lab1.txt'
opers = ['<', '>', '+', '/', '-', '*', '=', ".", ",", ":=", "<=", ">=", "<>"]
for_list = []
fk_list = []
fc_list = []
fs_list = []
new_line = []
result = ''
for_flag = False
cin_tab = 0
count_tab = 0
list_of_variables = []
error = ''
with open(file_path, 'r') as file:
    for line in file:
        new_line = line.strip().split(' ')
        count_tab = len(line) - len(line.strip())
        if for_flag:
            count_tab += 4
            cin_tab += -4
        if new_line[0] == 'for':
            result += '' '|-->for\n'

            for_list = [elem.replace('){','')for elem in new_line]
            fk_list = [elem.replace(';','')for elem in new_line]

            result += f'     |-->{new_line[3]}\n         |-->{fk_list[4]}\n         |-->{new_line[5]}\n     |-->{new_line[6]}\n         |-->{new_line[5]}\n         |-->{fk_list[7]}\n' \
                      f''+'     '
            #result += f'identifier: {new_line[1]} operator: {new_line[2]} value: {new_line[3]} key word: {new_line[4]} value: {new_line[5]} key word: {new_line[6]}\n' + ' ' * count_tab + ' ' * 4
            if for_list[8].endswith('++'):
                result += f'|-->++\n'
            result +=  f'         |-->{for_list[5]}'
            for_flag = True


        elif new_line[0] == 'int' and new_line[1] == 'main':
            continue
        elif len(new_line) == 4 and new_line[0] == 'int':
            fs_list = [elem.replace(';', '') for elem in new_line]
            if new_line[1] not in list_of_variables:
                list_of_variables.append(new_line[1])

            result += f'|-->{new_line[2]}\n     |-->{new_line[1]}\n     |-->{fs_list[3]}\n'


        elif len(new_line) == 3 and new_line[1].find('=') != -1:
            ind = new_line[0].find('=')
            fc_list = [elem.replace(';','')for elem in new_line]
            if new_line[0] not in list_of_variables:
                error = f'Переменная {new_line[0]} не объявлена'
                break
            else:
                result += ' ' * count_tab + ' ' * 4 + f'\n         |-->{new_line[1]}\n             |-->{new_line[0]}\n             |-->{fc_list[2]}\n'
                # result += ' ' * count_tab + ' ' * 4 + f'|--> identifier: {new_line[0]} operator: {new_line[1]} value: {new_line[2][:-1]} operator: ;\n



            for_flag = False
with open("output.txt", "w") as output_file:
    if error != '':
        output_file.write(error)
    else:
        output_file.write(result)