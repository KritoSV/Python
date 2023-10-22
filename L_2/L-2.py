# Создание и запись файла

colors = ['red', 'green', 'blue']
data = open('file.txt', 'a', encoding='utf-8') # здесь указываем режим в котором будем работать
data.writelines(colors) # разделителей не будет
data.close()

# Перезапись файла.

with open('file.txt', 'w') as data:
    data.write('line 1\n')
    data.write('line 3\n')

print(56)

# Чтение файла

path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()












