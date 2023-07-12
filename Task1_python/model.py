import json
import datetime
import os
import view
import controller


# Функция Даты и Времени в данный момент
def DTofNote():
    # Вызов метода now из класса datetime
    # (так делаю потому что есть конфликт с микросекундами(!) в дате datetime.datetime.now())
    current_dateTime = datetime.datetime.now()
    abc = f"{str(current_dateTime.year)}-{str(current_dateTime.month)}-{str(current_dateTime.day)} " \
          f"{str(current_dateTime.hour)}:{str(current_dateTime.minute)}:{str(current_dateTime.second)}"
    # Перегоняю строку abc в секунды
    rez = datetime.datetime.strptime(abc, '%Y-%m-%d %H:%M:%S').timestamp()
    return rez  # отправляю секунды


# Функция генерация нового Id
def findId(dictJson):
    return len(dictJson) + 2  # не знаю почему 2
    # (но если будет 1 то произойдет наслаивание и дублирование последнего ключа)


# Добавляю элемент в заметки
def addNote(noteTitle, bodyTitle):
    newNote = dict()
    # записываю в файл данные
    dictJson = json.load(open("note.json"))  # перевожу Json в словарь
    id1 = findId(dictJson)  # создаю новый Id
    newNote[id1] = [noteTitle, bodyTitle, DTofNote()]
    dictJson.update(newNote)  # добавляю в словарь новый элемент

    json.dump(dictJson, open("note.json", 'w'), indent=2, ensure_ascii=False)  # перевожу словарь в Json
    # (ensure_ascii - позволяет записывать кирилицу)
    view.massegeAboutAdd()


# Чтение всего файла или по id
def readJson(nums):
    # Прочтение заметки
    with open("note.json") as file:
        view.formaMenu()
        data = json.load(file)  # передаем файловый объект (распаковка из json в словарь)
        if nums == "all":  # выводим на экран все заметки
            for key, value in data.items():
                print(f'{key}: {value[0]}')
                print(f'{value[1]}')
                date_time = datetime.datetime.fromtimestamp(value[2])
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
            view.errorId()
        view.formaMenu()


# функция сортировки
def sortJson():
    newDictSort = dict()
    with open("note.json", "r") as file1:
        dictJson = json.load(file1)
        qw = input("Сортировку проводить по id или по time? id/time: ")
        if qw == "time":  # сортировка по времени
            newDictSort = dict(sorted(dictJson.items(), key=lambda item: item[1][2]))
        elif qw == "id":  # сортировка по id
            newDictSort = dict(sorted(dictJson.items(), key=lambda item: int(item[0])))
        else:
            view.errorEnter()
    with open('note.json', 'w') as file:  # запись в Json нового словаря
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
            if key != num:
                newDickJson[key] = value
            else:  # если совпадение найдено то вводим корректировку в Заголовок и Тело заметки
                value[0], value[1], value[2] = newNoteTitle, newBodyTitle, DTofNote()
                newDickJson[key] = value
        with open('note.json', 'w') as file:
            json.dump(newDickJson, file, indent=2, ensure_ascii=False)
            view.goodCange()
    else:
        view.dontFindId()


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
            view.messegeAboutDalete()
    elif num == "all":
        with open("note.json", "w") as file1:
            json.dump(dict(), file1, indent=2, ensure_ascii=False)  # записываю в файл пустой словарь
            view.MessegeAboutAllDalete()
    else:
        view.errorEnterID()



