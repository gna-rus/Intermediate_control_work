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
import os


def menu():
    print("add - добавить элемент в заметки")
    print("read - прочитать все заметки")
    print("clear - удалить все заметки")


# Функция генерация нового Id
def findId(dictJson):
    return len(dictJson) + 1


# Добавляю элемент в заметки
def addNote(noteTitle, bodyTitle, timeJson):
    newNote = dict()
    sizeOfDictJson = os.path.getsize("note.json")  # определяю пустой файл или нет (в файле должно быть хотя бы "{}")
    # записываю в файл данные
    dictJson = json.load(open("note.json"))  # перевожу Json в словарь
    id1 = findId(dictJson)
    newNote[id1] = [noteTitle, bodyTitle, timeJson]
    dictJson.update(newNote)  # добавляю в словарь новый элемент

    json.dump(dictJson, open("note.json", 'w'), indent=2, ensure_ascii=False)  # перевожу словарь в Json
    # (ensure_ascii - позволяет записывать кирилицу)


# Чтение всего файла или по id
def readJson(nums):
    # Прочтение заметки
    with open("note.json") as file:
        data = json.load(file)  # передаем файловый объект
        if nums == "all":  # выводим на экран все заметки
            for key, value in data.items():
                print(f'{key}: {value[0]}')
                print(f'{value[1]}')
                print(f'{value[2:]}')
        elif nums in data.keys():  # выводим на экран заметки по id
            print(f'{int(nums)}: {data[nums][0]}')
            print(f'{data[nums][1]}')
            print(f'{data[nums][2:]}')
        else:
            print("Error!!! Не корректный id")


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
    noteTitle = "Голова"
    bodyTitle = "Тело"
    addNote(noteTitle, bodyTitle, timeJson)
elif comand == "read":
    nums = input("Введите номер id (или all для всех заметок) ")
    readJson(nums)

    # newJson = json.dumps(newNote)
    # note.write(newJson)
    # print(type(newJson))
