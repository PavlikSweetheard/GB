from sys import argv


def zarplata(work_hours, rate, bonus, NDFL):
    return NDFL/100 * (work_hours * rate + bonus)


script_name, work_hours, rate, bonus, NDFL = map(float, argv[1:])

print("Salary = ", zarplata(int(work_hours), int(rate), int(bonus)))
