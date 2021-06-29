sentence = input("Введите строку из нескольких слов : \n")

for num, el in enumerate(sentence.split(), 1):
    print(f"{num}) {el[:10]}")
