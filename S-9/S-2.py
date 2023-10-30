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
    i_search_param = int(command) - 1    
    search = input("Введите данные для поиска:\n").title()
    contacts_list = read_file().rstrip().split("\n\n")
    # print(contacts_list)

    for contact_str in contacts_list:
        contacts_lst = contact_str.replace("\n", " ").split()
        # print(contacts_lst)
        if search in contacts_lst[i_search_param]:
            print("\n" + contact_str + "\n")
            surname = input("Введите новую Фамилию:\n")
            name = input("Введите новое Имя:\n")
            patronymic = input("Введите новое Отчество:\n")
            phone = input("Введите новый № телефона:\n")
            adress = input("Введите новый Адрес:\n")
            contacts_lst = f"{surname} {name} {patronymic} {phone}\n{adress}\n\n"
            contacts_list[i_search_param] += contacts_lst
            print('Данные изменены.')
            with open("phonebook.txt", "a+", encoding="UTF-8") as file:
                file.read()



Петров Иван Сергеевич 123456
Москва

Иванов Пётр Сергеевич 963852
Сочи

Егоров Александр Иванович 741789
Пятигорск

Михаил Андреевич Олегович 741852
Иваново

Михаил Олегович Андреевич 741854
Ивановка





def delete_data(filename):
print(«\nПП | ФИО | Телефон»)
with open(filename, «r», encoding=»utf-8″) as data:
tel_book = data.read()
print(tel_book)
print(«»)
index_delete_data = int(input(«Введите номер строки для удаления: «)) — 1
tel_book_lines = tel_book.split(«\n»)
del_tel_book_lines = tel_book_lines[index_delete_data]
tel_book_lines.pop(index_delete_data)
print(f»Удалена запись: {del_tel_book_lines}\n»)
with open(filename, «w», encoding=’utf-8′) as data:
data.write(«\n».join(tel_book_lines))

def main():
my_choice = -1
file_tel = «tel.txt»