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
    print("edit - редактирование заметки")
    print("clear - удалить все заметки")

# Функция Даты и Времени в данный момент
def DTofNote():
    vremya = datetime.datetime.now()  # Вызов метода now из класса datetime
    return vremya.strftime("%m/%d/%Y | %H:%M:%S")


def miniMenu():
    with open("note.json") as file:
        data = json.load(file)
        for key, value in data.items():
            print(f'{key} - {value[0]}')

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
    print(f"Заметка доабвлена!")


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

# Функция редактирования заметок
def editJson(num):
    newDickJson = dict() # словарь-буфер
    flag = False
    # проверка, есть ли вообще такое id в файле
    with open("note.json") as file:
        data = json.load(file)
        if num in data.keys():
            flag = True

    if flag == True:
        with open("note.json", "r") as file1:
            dictJson = json.load(file1)
            newNoteTitle = "Голова!!!"
            newBodyTitle = "Тело!!!!"
        # цикл для поиска id
        for key, value in dictJson.items():
            print(key, value)
            if key != num:
                newDickJson[key] = value
            else: # если совпадение найдено то вводим корректировку в Заголовок и Тело заметки
                value[0], value[1], value[2] = newNoteTitle, newBodyTitle, DTofNote()
                newDickJson[key] = value
        with open('note.json', 'w') as file:
            json.dump(newDickJson, file, indent=2, ensure_ascii=False)
    else:
        print("Неверный ввод. Такой id не найден")

menu()
print(DTofNote())  # Вывод времени на экран

# Меню ввода
newNote = dict()
comand = "read"
if comand == "add":
    noteTitle = "Голова"
    bodyTitle = "Тело"
    addNote(noteTitle, bodyTitle, DTofNote())
elif comand == "read":
    miniMenu()
    nums = input("Введите номер id (или all для вывода всех заметок) ")
    readJson(nums)
elif comand == "edit":
    miniMenu()
    nums = input("Введите номер id для редактирования  ")
    editJson(nums)

