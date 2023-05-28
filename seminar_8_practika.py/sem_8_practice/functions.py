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
        

# def delete_data() -> None:
#     """Удаляет информацию из справочника."""
#     with open('book.txt', 'r', encoding='utf-8') as file:
#         data = file.readlines()
#     contact_to_delete = input('Введите ФИО контакта, которого хотите удалить: ')
#     indexes = search(data, contact_to_delete)

#     if len(indexes) == 0:
#         print('Контакт не найден')
#     elif len(indexes) == 1:
#         del data[indexes[0]]
    
        
# def update_data() -> None:
#     """Изменяет данные в справочнике"""
#     with open('book.txt', 'r+', encoding='utf-8') as book:
#         data = book.read()
#     contact_to_update = input('Введите номер контакта, который нужно изменить: ')
#     contacts = data.split('\n')
#     for i, contact in enumerate(contacts):
#         if str(i + 1) == contact_to_update:
#             new_fio = input('Введите новое ФИО: ')
#             new_phone_num = input('Введите новый номер телефона: ')
#             contacts[i] = f'{new_fio} | {new_phone_num}'
#             break
#         else:
#             print('Контакт не найден')
#     return

# def delete_data() -> None:
#     """Удаляет данные из справочника"""
#     with open('book.txt', 'r+', encoding='utf-8') as book:
#         data = book.read()
#     contact_to_delete = input('Введите номер контакта, который нужно удалить: ')
#     contacts = data.split('\n')
#     for i, contact in enumerate(contacts):
#         if str(i + 1) == contact_to_delete:
#             del contacts[i]
#             break
#         else:
#             print('Контакт не найден')
#     return 


# def update_data() -> None:
#     """Изменяет информацию в справочнике."""
#     with open('book.txt', 'r', encoding='utf-8') as book:
#         data = book.readlines()
#     print('Контакты:')
#     for i, contact in enumerate(data):
#         print(f'{i+1}. {contact.strip()}')

#     num = int(input('Введите номер контакта для изменения: '))
#     fio = input('Введите новое ФИО: ')
#     phone_num = input('Введите новый номер телефона: ')
#     data[num-1] = f'{fio} | {phone_num}\n'

#     with open('book.txt', 'w', encoding='utf-8') as book:
#         book.writelines(data)

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