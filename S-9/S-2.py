def del_memb(data):
    ''' удаление по имени и фамилии'''
    member = ' '.join(map(str.lower, [input('Фамилия: '), input('Имя: ')]))
    for i, obj in enumerate(data):
        if obj.identifier() == member:
            data.pop(i)
            savedata(data,name) # перезаписываем файл c новыми данными
            print('удалено')
            return
        




def change(data, member):
    ''' изменение значения по полю или добавление нового'''
    for obj in data: 
        if  obj.identifier() == member:
            key = input('введите имя поля > ')
            if key not in obj.change():
                print('нет такого поля')
                if input(' создать поле? д\н > ').lower() == 'д':
                    key = input('введите имя поля > ')
                else:
                    return
            values = input('введите значение > ')
            obj.paramchan(key, values)
            break