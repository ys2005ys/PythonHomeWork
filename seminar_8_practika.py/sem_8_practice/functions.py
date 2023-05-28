def show_data() -> None:
    """Выводит информацию из справочника"""
    with open('book.txt', 'r', encoding='utf-8') as book:
        print(book.read())


def add_data() -> None:
    """Добавляет информацию в справочник."""
    fio = input('Введите ФИО: ')
    phone_num = input('Введите номер телефона: ')
    with open('book.txt', 'a', encoding='utf-8') as book:
        book.write(f'\n{fio} | {phone_num}')


def find_data() -> None:
    """Печатает результат поиска по справочнику."""
    with open('book.txt', 'r', encoding='utf-8') as file:
        data = file.read()
    contact_to_find = input('Введите, что хотите найти: ')
    result = search(data, contact_to_find)
    print(result)


def search(book: str, info: str) -> list[str]:
    """Находит в списке записи по определенному критерию поиска"""
    book = book.split('\n')
    return list(filter(lambda contact: info.lower() in contact.lower(), book))
        

def edit_data() -> None:
    """Изменяет информацию о контакте в справочнике"""
    search_query = input('Введите ФИО контакта, информацию о котором нужно изменить: ')
    with open('book.txt', 'r', encoding='utf-8') as file:
        data = file.readlines()
    found = False
    for i in range(len(data)):
        if search_query in data[i]:
            found = True
        new_data = input('Введите новые данные через запятую (ФИО, номер телефона): ')
        updated_data = new_data.split(', ')
        data[i] = f'{updated_data[0]} | {updated_data[1]}\n'
        print('Информация о контакте изменена.')
        break

        if not found:
            print('Контакт не найден.')

    with open('book.txt', 'w', encoding='utf-8') as file:
        file.writelines(data)
        

def delete_data() -> None:
    """Удаляет информацию из справочника."""
    with open('book.txt', 'r', encoding='utf-8') as file:
        data = file.readlines()
    contact_to_delete = input('Введите ФИО контакта, который нужно удалить: ')
    for index, contact in enumerate(data):
        if contact_to_delete.lower() in contact.lower():
            del data[index]
    with open('book.txt', 'w', encoding='utf-8') as file:
        file.writelines(data)
    print(f'Контакт {contact_to_delete} успешно удален из справочника.')