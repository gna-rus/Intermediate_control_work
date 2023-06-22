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
    formaMenu()
    print("add - добавить элемент в заметки")
    print("read - прочесть заметку по id или все заметки")
    print("edit - редактировать заметку по id")
    print("sort - осуществить сортировку заметок")
    print("clear - удалить заметку по id или все заметки")
    print("exit - Выход")
    formaMenu()

# Функция Даты и Времени в данный момент
def DTofNote():
    # Вызов метода now из класса datetime
    # (так делаю потому что есть конфликт с микросекундами(!) в дате datetime.datetime.now())
    current_dateTime = datetime.datetime.now()
    abc = f"{str(current_dateTime.year)}-{str(current_dateTime.month)}-{str(current_dateTime.day)} " \
          f"{str(current_dateTime.hour)}:{str(current_dateTime.minute)}:{str(current_dateTime.second)}"
    # Перегоняю строку abc в секунды
    rez = datetime.datetime.strptime(abc, '%Y-%m-%d %H:%M:%S').timestamp()
    return rez #отправляю секунды

# Функция Оглавления
def miniMenu():
    formaMenu()
    with open("note.json") as file:
        data = json.load(file)
        print("Оглавление: ")
        for key, value in data.items():
            print(f'{key} - {value[0]}')
    formaMenu()

# Функция генерация нового Id
def findId(dictJson):
    return len(dictJson) + 2 # я не знаю почему 2 (но если будет 1 то произойдет наслаивание и дублирование последнего ключа)

def formaMenu():
    print("#" * 30)

# Добавляю элемент в заметки
def addNote(noteTitle, bodyTitle):
    newNote = dict()
    # записываю в файл данные
    dictJson = json.load(open("note.json"))  # перевожу Json в словарь
    id1 = findId(dictJson) # создаю новый Id
    newNote[id1] = [noteTitle, bodyTitle, DTofNote()]
    dictJson.update(newNote)  # добавляю в словарь новый элемент

    json.dump(dictJson, open("note.json", 'w'), indent=2, ensure_ascii=False)  # перевожу словарь в Json
    # (ensure_ascii - позволяет записывать кирилицу)
    print(f"Заметка доабвлена!")


# Чтение всего файла или по id
def readJson(nums):
    # Прочтение заметки
    with open("note.json") as file:
        formaMenu()
        data = json.load(file)  # передаем файловый объект (распаковка из json в словарь)
        if nums == "all":  # выводим на экран все заметки
            for key, value in data.items():
                print(f'{key}: {value[0]}')
                print(f'{value[1]}')
                date_time = str(datetime.datetime.fromtimestamp(int(value[2])))
                print(f'{date_time}')
        elif nums in data.keys():  # выводим на экран заметки по id
            print(f'{int(nums)}: {data[nums][0]}')
            # далее код для многострочного вывода в командную строку
            count = 0
            for i in data[nums][1]:
                if (i == " ") and (count > 100):
                    count = 0
                    print()
                else:
                    count += 1
                    print(i, sep="", end="")
            print()
            date_time = datetime.datetime.fromtimestamp(data[nums][2])
            print(f'{date_time}')
        else:
            print("Error!!! Не корректный id")
        formaMenu()

# функция сортировки
def sortJson():
    newDictSort = dict()
    with open("note.json", "r") as file1:
        dictJson = json.load(file1)
        qw = input("Сортировку проводить по id или по time? id/time: ")
        if qw == "time": # сортировка по времени
            newDictSort = dict(sorted(dictJson.items(), key=lambda item: item[1][2]))
        elif qw == "id": # сортировка по id
            newDictSort = dict(sorted(dictJson.items(), key=lambda item: int(item[0])))
            print(newDictSort)
        else:
            print("Невернный ввод")
    with open('note.json', 'w') as file: # запись в Json нового словаря
        json.dump(newDictSort, file, indent=2, ensure_ascii=False)

# Функция редактирования заметок
def editJson(num):
    newDickJson = dict()  # словарь-буфер
    flag = False
    # проверка, есть ли вообще такое id в файле
    with open("note.json") as file:
        data = json.load(file)
        if num in data.keys():
            flag = True

    if flag == True:
        with open("note.json", "r") as file1:
            dictJson = json.load(file1)
            newNoteTitle = input("Введите новый заголовок: ")
            newBodyTitle = input("Заметка: ")
        # цикл для поиска id
        for key, value in dictJson.items():
            print(key, value)
            if key != num:
                newDickJson[key] = value
            else:  # если совпадение найдено то вводим корректировку в Заголовок и Тело заметки
                value[0], value[1], value[2] = newNoteTitle, newBodyTitle, DTofNote()
                newDickJson[key] = value
        with open('note.json', 'w') as file:
            json.dump(newDickJson, file, indent=2, ensure_ascii=False)
            print("Заметка изменена успешно!")
    else:
        print("Неверный ввод. Такой id не найден")


# Функция для удаления id или всех заметок
def clearJson(num):
    newDickJson = dict()  # словарь-буфер
    flag = False
    # проверка, есть ли вообще такое id в файле
    with open("note.json") as file:
        data = json.load(file)
        if num in data.keys():
            flag = True

    if flag == True and num != "all":
        with open("note.json", "r") as file1:
            dictJson = json.load(file1)
        # цикл для поиска id
        for key, value in dictJson.items():
            if key != num:
                newDickJson[key] = value
        with open('note.json', 'w') as file:
            json.dump(newDickJson, file, indent=2, ensure_ascii=False)
            print("Заметка удалена успешно!")
    elif num == "all":
        with open("note.json", "w") as file1:
            json.dump(dict(), file1, indent=2, ensure_ascii=False)  # записываю в файл пустой словарь
            print("Все заметки удалены!")
    else:
        print("Невернный ввод! Такой id не найден")

sizeOfDictJson = os.path.getsize("note.json")  # определяю пустой файл или нет (в файле должно быть хотя бы "{}")
if sizeOfDictJson == 0:
    with open("note.json", "w") as file1:
        json.dump(dict(), file1, indent=2, ensure_ascii=False)  # записываю в файл пустой словарь
formaMenu()
print(f"Дата: {datetime.datetime.fromtimestamp(DTofNote())}")  # Вывод времени на экран

# Меню ввода
comand = ""
while (comand != "exit"):
    menu()
    comand = input("Введите команду: ")
    if comand == "add":
        noteTitle = input("Введите заголовок: ")
        bodyTitle = input("Заметка: ")
        addNote(noteTitle, bodyTitle)
        input()
    elif comand == "read":
        miniMenu()
        nums = input("Введите номер id (или all для вывода всех заметок) ")
        readJson(nums)
        input()
    elif comand == "edit":
        miniMenu()
        nums = input("Введите номер id для редактирования ")
        editJson(nums)
        input()
    elif comand == "sort":
        sortJson()
        input()
    elif comand == "clear":
        miniMenu()
        nums = input("Введите номер id (или all для удаления всех заметок) ")
        clearJson(nums)
        input()
    elif comand == "exit":
        print("До свидания!")
        break

