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
    print("read - прочитать все заметки")
    print("clear - удалить все заметки")

# Функция генерация нового Id
def findId(nums):
    with open("note.json", "r", encoding="utf-8") as note:
        if nums == 0:
            return 1
        else:
            nums = json.load(note)
            print(nums)
            return nums+1

# Добавляю элемент в заметки
def addNote(noteTitle, bodyTitle, timeJson):
    newNote = dict()

    # записываю в файл данные
    with open("note.json", "a", encoding="utf-8") as note:
        newNote[1] = [noteTitle, bodyTitle, timeJson]
        json.dump(newNote, note, indent=2, sort_keys=True)

menu()
vremya = datetime.datetime.now()  # Вызов метода now из класса datetime.
timeJson = vremya.strftime("%m/%d/%Y | %H:%M:%S")
print(timeJson)  # Вывод времени на экран

# Формат заметки {id:[заголовок, тело, дата\время]}

# comand = input("Введите команду: ")
# noteTitle = input("Введите заголовок заметки: ")
# bodyTitle = input("Введите тело заметки: ")

# Меню ввода
newNote = dict()
comand = "add"
if comand == "add":
    noteTitle = "Head"
    bodyTitle = "Body"
    addNote(noteTitle, bodyTitle, timeJson)

    # newJson = json.dumps(newNote)
    # note.write(newJson)
    # print(type(newJson))

# Прочтение заметки
with open("note.json") as file:
    data = json.load(file)  # передаем файловый объект
    for key, value in data.items():
        if type(value) == list:
            print(f'{key}: {", ".join(value)}')
        else:
            print(f'{key}: {value}')
