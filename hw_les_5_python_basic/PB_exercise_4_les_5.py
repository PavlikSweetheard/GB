"""

4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый
текстовый файл.


"""

with open('text.txt') as f:
    lines = f.readlines()

with open('text2.txt', 'w') as f2:
    for line in lines:
        print(line)
        if 'One' in line:
            line = line.replace('One', 'Один')
        elif 'Two' in line:
            line = line.replace('Two', 'Два')
        elif 'Three' in line:
            line = line.replace('Three', 'Три')
        elif 'Four' in line:
            line = line.replace('Four', 'Четыре')
        f2.write(line)
