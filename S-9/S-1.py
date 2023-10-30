# Создать телефонный справочник с 
# возможностью импорта и экспорта данных в 
# формате .txt. Фамилия, имя, отчество, номер 
# телефона - данные, которые должны находиться 
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в 
# текстовом файле
# 3.Пользователь может ввести одну из 
# характеристик для поиска определенной 
# записи(Например имя или фамилию человека)
# 4. Использование функций. 
# Ваша программа не должна быть линейной


# # 1. Создать файл для записи телефонной книги:        ++++++++++
# - открытие_файла_на_дозапись.
# - удаление записи из файла.
# # 1.1 Подготовка меню для пользователя.               ++++++++++
# # 2. Запись данных в файл по новому контакту:         ++++++++++
# - ввод_данных_пользователя.                           ++++++++++
# - подготовка_данных_для_записи_в_файл.                ++++++++++
# - открытие_файлов_в_режиме_дозаписи.                  ++++++++++       
# - запись_новой_строки_с_данными.                      ++++++++++
# # 3. Чтение данных из файла                           ++++++++++
# - открытие_файла_в_режиме_чтения.                     ++++++++++
# - считать_все_данные_и_вывести_их_на_экран.           ++++++++++
# # 4 Поиск записей по параметрам                       ++++++++++
# и вывод соответствующих данных:                       ++++++++++
# - открыть_файл_в_режиме_чтения.                       ++++++++++
# - считать_все_данные_из_файла_и                       ++++++++++
# сохранить_их_в_программе.                             ++++++++++
# - сделать_выборку_нужной_записи - сам_поиск.          ++++++++++
# - показать_результат_поиска.                          ++++++++++

def input_name():
    return input("Введите Имя контакта:\n")

def input_surname():
    return input("Введите Фамилию контакта:\n")

def input_patronymic():
    return input("Введите Отчество контакта:\n")

def input_phone():
    return input("Введите № телефона контакта:\n")

def input_adress():
    return input("Введите адрес контакта:\n")


def input_data():

    surname = input_surname()
    name = input_name()
    patronymic = input_patronymic()
    phone = input_phone()
    adress = input_adress()
    str_contact = f"{surname} {name} {patronymic} {phone}\n{adress}\n\n"
    print(str_contact[:-2])
    with open("phonebook.txt", "r", encoding="UTF-8") as file:
        contacts_list = read_file().rstrip().split("\n\n")
        for contact in contacts_list:
            contact = contact.replace("\n", " ").split(' ')
            if contact[3] == phone:
                return print(f"{contact[3]} Такой контакт уже имеется!")
    with open("phonebook.txt", "a", encoding="UTF-8") as file:
        file.write(str_contact)


def read_file():
    with open("phonebook.txt", "r", encoding="UTF-8") as file:
        return file.read()


def print_data():
    print(read_file())


def search_contact(command = None):
    if command != None:
        isreturn = True
    if command == None:
        print("Выберите параметр поиска:\n"
            "1. Фамилия\n"
            "2. Имя\n"
            "3. Отчество\n"
            "4. Телефон\n"
            "5. Адрес")
        command = input("Введите № варианта: ")
        while command not in ("1", "2", "3", "4", "5"):
            print("Не существующий вариант\n"
                "Попробуйте снова.")
            command = input("Введите № варианта: ")
        print()    
    search = input("Введите данные для поиска:\n").title()
    contacts_list = read_file().rstrip().split("\n\n")
    i_search_param = int(command) - 1
    # print(contacts_list)
    list_number = []
    for contact_str in contacts_list:
        contacts_lst = contact_str.replace("\n", " ").split()
        # print(contacts_lst)
        if search in contacts_lst[i_search_param]:
            list_number.append(contact_str)
            print(contact_str + "\n")
    if isreturn:
        return list_number
            


def change_contact():
    with open("phonebook.txt", "a+", encoding="UTF-8"):
        print("Выберите параметр поиска:\n"
        "1. Фамилия\n"
        "2. Имя\n"
        "3. Отчество\n"
        "4. Телефон\n"
        "5. Адрес")
        find_change_contact = input("Введите № варианта: ")
    while find_change_contact not in ("1", "2", "3", "4", "5"):
        print("Не существующий вариант\n"
            "Попробуйте снова.")
        find_change_contact = input("Введите № варианта: ")
    find_change_contact = search_contact(find_change_contact)
    print(find_change_contact)
    number_num = len(find_change_contact)
    if number_num > 1:
        print("Выберите контакт для изменения:  ")
        for i in range(number_num):
            print(f"{i + 1}. {find_change_contact[i]}\n")
        chng_contact = input("Введите № варианта: ")
        while not (1 <= int(chng_contact) <= number_num):
            print("Не существующий вариант\n"
                "Попробуйте снова.")
            chng_contact = input("Введите № варианта: ")
    else: chng_contact = "1"
    find_contact = find_change_contact[int(chng_contact) - 1]
    print("Выберите параметр изменения:\n"
        "1. Фамилия\n"
        "2. Имя\n"
        "3. Отчество\n"
        "4. Телефон\n"
        "5. Адрес"
        "6. Удаление контакта")
    config_contact = input("Введите № варианта: ")
    while config_contact not in ("1", "2", "3", "4", "5", "6"):
        print("Не существующий вариант\n"
            "Попробуйте снова.")
        config_contact = input("Введите № варианта: ")
    new_contact = list.copy(find_contact.replace("\n", " ").split())
    if config_contact != "6":
        new_contact[int(config_contact) - 1] = input("Введите новое значение:\n")
        new_contact = f"{new_contact[0]} {new_contact[1]} {new_contact[2]} {new_contact[3]}\n{new_contact[4]}\n\n"
        with open("phonebook.txt", "a+", encoding="UTF-8") as file:
            # read_file().replace(find_contact, new_contact)
            file.write(read_file().replace(find_contact, new_contact))
    else: pass
                


def interface():
    with open("phonebook.txt", "a", encoding="UTF-8"):
        pass
    command = ""
    while command != "5":
        print("Выберите варианты работы с телефонной книгой:\n"
            "1. Запись данных\n"
            "2. Вывод контактов на экран\n"
            "3. Поиск данных\n"
            "4. Изменение данных\n"
            "5. Выход")
        command = input("Введите № варианта: ")
        while command not in ("1", "2", "3", "4"):
            print("Не существующий вариант\n"
                "Попробуйте снова.")
            command = input("Введите № варианта: ")
        print()
        match command:
            case "1":
                input_data()
            case "2":
                print_data()
            case "3":
                search_contact()
            case "4":
                change_contact()
            case "5":
                print("Досвидания!")
    


interface()