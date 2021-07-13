"""

2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.


"""

with open('test.txt') as f:
    lines = f.readlines()
    print(':', len(lines))
    for num_line, line in enumerate(lines, start=1):
        print('В {} -ой строке  {} слов'.format(num_line, len(line.split())))
