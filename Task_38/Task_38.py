import datetime

phone_book = {}
path: str= 'PhoneNumbers.txt'
dict_Snowden = {}

def open_file():
    phone_book.clear()
    with open(path, 'r', encoding='UTF-8') as file:
        f = file.readlines()

    # f = [fi.strip().split(':') for fi in f]
    for contact in f:
        c = contact.strip().split(':')
        phone_book[int(c[0])] = {'name': c[1], 'phone': c[2], 'comment': c[3]}
    print('\nContacts received')
def show_contacts(book: dict[int, dict]):
    print('\n' + '_' * 200)
    for i,cnt in book.items():
        print(f'{i:>3}. {cnt.get("name"):<30}{cnt.get("phone"):<10}{cnt.get("comment"):<15}')
    print('_'*200 + '\n')
def add_contact():
    uid = max(list(phone_book.keys())) +1
    name = input('Contact name: ')
    phone = input('Contact phone: ')
    comment = input('Contact comment: ')
    phone_book[uid] = {'name': name, 'phone': phone, 'comment': comment}
    print(f'\nContact {name} complete add')
    print('_' * 200 + '\n')
def save_file():
    data = []
    for i, contacts in phone_book.items():
        new = ':'.join([str(i), contacts.get('name'), contacts.get('phone'), contacts.get('comment')])
        data.append(new)
    data = '\n'.join(data)
    with open(path, 'w', encoding='UTF-8') as file:
        file.write(data)
    print("Complete load")
    print('_' * 200 + '\n')
def сontact_search():
    result = {}
    word = input("Enter the search word: ")
    for i, contact in phone_book.items():
        if word.lower() in " ".join(list(contact.values())).lower():
            result[i] = contact
    return result
def remove():
    result = сontact_search()
    show_contacts(result)
    index = int(input("Enter id contact: "))
    del_cnt = phone_book.pop(index)
    print(f'\nContact {del_cnt.get("name")} delete')
    print('_' * 200 + '\n')
def edit_contact(): # Редактор контакта: поиск контакта, ввод id, замена имени/телефона/коммента. Если пропуск, контакт не изменяется
    result = сontact_search()
    show_contacts(result)
    uid = int(input("Enter a id to change: "))
    edit_name = input(f"Enter a new name, old - {list(phone_book[uid].values())[0]}: ") or list(phone_book[uid].values())[0]
    edit_phone = input(f"Enter a new phone, old - {list(phone_book[uid].values())[1]}: ") or list(phone_book[uid].values())[1]
    edit_comment = input(f"Enter a new status, old - {list(phone_book[uid].values())[2]}: ") or list(phone_book[uid].values())[2]
    phone_book[uid] = {'name': edit_name, 'phone': edit_phone, 'comment': edit_comment}

def big_brother(function_name): #Добавляет действия пользователя в словарь dict_Snowden
    data_v = datetime.datetime.now()
    dict_Snowden.setdefault(str(datetime.date.today()), []).append(f'{data_v.strftime("%H:%M")} - {function_name}')
    return dict_Snowden
def save_big_brother(): #Сохраняет в файл file_for_kgb.txt
    with open('file for kgb.txt', "a", encoding='UTF-8') as f_KGB:
        f_KGB.write(f'\n{str(datetime.date.today())} ____ {" ----> ".join(dict_Snowden[str(datetime.date.today())])}')
    print("The file was successfully sent to Lubyanka")

def menu() -> int:
    main_menu = '''Main menu:
    1. Open file
    2. Save file
    3. Show contacts    
    4. Create contact
    5. Сontact_search
    6. Edit contact
    7. Delete contact
    8. Exit'''

    print(main_menu)
    while True:
        select = input('Select a menu item: ')
        if select.isdigit() and 0 < int(select) < 9:
            return int(select)
        print('Input error, please enter a NUMBER from 1 to 8')
open_file()
big_brother("open_file")

while True:
    select = menu()
    match select:
        case 1:
            open_file()
            big_brother("open_file")
        case 2:
            save_file()
            big_brother("save_file")
        case 3:
            show_contacts(phone_book)
            big_brother("show_contacts")
        case 4:
            add_contact()
            save_file()
            big_brother("add_contact")
            save_big_brother()
        case 5:
            result = сontact_search()
            show_contacts(result)
            big_brother("show_contact")
        case 6:
            edit_contact()
            save_file()
            big_brother("edit_contact")
            save_big_brother()
        case 7:
            remove()
            big_brother("remove_contact")
        case 8:
            print("Finally you left")
            big_brother("exit")
            save_big_brother()

            break
    #print('_' * 200 + '\n')

