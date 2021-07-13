"""

3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.


"""

salaries = []
with open("text.txt") as m_f:
    lines = m_f.readlines()
    print(lines)
    for line in lines:
        name, salary = line.split(' - ')
        salaries.append(int(salary))
        if int(salary) < 20000:
            print('name', name)
print('средняя = ', sum(salaries) / len(salaries))
