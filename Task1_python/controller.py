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
import view
import model


#Начало программы
def start():
    sizeOfDictJson = os.path.getsize("note.json")  # определяю пустой файл или нет (в файле должно быть хотя бы "{}")
    if sizeOfDictJson == 0:
        with open("note.json", "w") as file1:
            json.dump(dict(), file1, indent=2, ensure_ascii=False)  # записываю в файл пустой словарь
    view.formaMenu()
    print(f"Дата: {datetime.datetime.fromtimestamp(model.DTofNote())}")  # Вывод времени на экран

    # Меню ввода
    comand = ""
    while (comand != "exit"):
        view.menu()
        comand = input("Введите команду: ")
        if comand == "add":
            noteTitle = input("Введите заголовок: ")
            bodyTitle = input("Заметка: ")
            model.addNote(noteTitle, bodyTitle)
            input()
        elif comand == "read":
            view.miniMenu()
            nums = input("Введите номер id (или all для вывода всех заметок) ")
            model.readJson(nums)
            input()
        elif comand == "edit":
            view.miniMenu()
            nums = input("Введите номер id для редактирования ")
            model.editJson(nums)
            input()
        elif comand == "sort":
            model.sortJson()
            input()
        elif comand == "clear":
            view.miniMenu()
            nums = input("Введите номер id (или all для удаления всех заметок) ")
            model.clearJson(nums)
            input()
        elif comand == "exit":
            print("До свидания!")
            break


