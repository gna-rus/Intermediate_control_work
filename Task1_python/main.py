# Задание
# Реализовать консольное приложение заметки, с сохранением, чтением,
# добавлением, редактированием и удалением заметок. Заметка должна
# содержать идентификатор, заголовок, тело заметки и дату/время создания или
# последнего изменения заметки. Сохранение заметок необходимо сделать в
# формате json или csv формат (разделение полей рекомендуется делать через
# точку с запятой). Реализацию пользовательского интерфейса студент может
# делать как ему удобнее, можно делать как параметры запуска программы
# (команда, данные), можно делать как запрос команды с консоли и
# последующим вводом данных, как-то ещё, на усмотрение студента.

import json
import datetime

def menu():
    print("add - добавить элемент в заметки")
menu()
vremya = datetime.datetime.now() #Вызов метода now из класса datetime.
print(vremya) #Вывод времени на экран

# Формат заметки {id:[заголовок, тело, дата\время]}
# comand = input("Введите команду: ")
# noteTitle = input("Введите заголовок заметки: ")
# bodyTitle = input("Введите тело заметки: ")

newNote = dict()
comand = "add"
noteTitle = "Head"
bodyTitle = "Body"
newNote[noteTitle] = bodyTitle
# записываю в файл данные
with open("note.json", "w", encoding="utf-8") as note:
    json.dump(newNote, note, indent=2, sort_keys=True)
    # newJson = json.dumps(newNote)
    # note.write(newJson)
    # print(type(newJson))

# Прочтение заметки
with open("note.json") as file:
    data = json.load(file)                # передаем файловый объект
    for key, value in data.items():
        if type(value) == list:
            print(f'{key}: {", ".join(value)}')
        else:
            print(f'{key}: {value}')