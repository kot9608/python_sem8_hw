def show_data() -> None:
    """Выводит информацию из справочника"""
    with open('book.txt', 'r', encoding='utf-8') as file:
        print(file.read())


def add_data() -> None:
    """Добавляет информацию в справочник."""
    fio = input('Введите ФИО: ')
    phone = input('Введите номер телефона: ')
    with open('book.txt', 'a', encoding='utf-8') as file:
        file.write(f'\n{fio} | {phone}')


def find_data() -> None:
    """Печатает результат поиска по справочнику."""
    with open('book.txt', 'r', encoding='utf-8') as file:
        data = file.read()
    print(data)
    data_to_find = input('Введите данные для поиска: ')
    print(search(data, data_to_find))


# def search(book: str, info: str) -> str:
#     """Находит в списке записи по определенному критерию поиска"""
#     book = book.split('\n')
#     s = [] # список для вывода значений
#     for contact in book:
#         if info in contact:
#             s.append(contact)
#         return 'Совпадений не найдено'
#     print(s)


def search(book: str, info: str) -> str:
    """Находит в списке записи по определенному критерию поиска"""
    book = book.split('\n')
    s = [] # список для вывода значений
    for contact in book:
        if info in contact:
            s.append(contact)
    if len(s)==1:
        return print(s)
    if len(s)>1:
        return (print(s), search2(s,info))
    else:
        return('Совпадений не найдено')
    
def search2 (book2: list, info2:str)-> str:
    """Функция используется для уточнения результатов поиска функции search"""
    sear=input('Введите уточнение поиска: ')
    s2 = [] # список для вывода значений
    for contact in book2:
        if sear in contact:
            s2.append(contact)
    if len(s2)>1:
        return (print(s2), search2(s2,info2))
    if len(s2)==1:
        return print(s2)
    else:
        return('Совпадений не найдено')