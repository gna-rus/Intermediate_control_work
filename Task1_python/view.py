import json
import datetime
import os
import model
import controller


def menu():
    formaMenu()
    print("add - добавить элемент в заметки")
    print("read - прочесть заметку по id или все заметки")
    print("edit - редактировать заметку по id")
    print("sort - осуществить сортировку заметок")
    print("clear - удалить заметку по id или все заметки")
    print("exit - Выход")
    formaMenu()

# Функция Оглавления
def miniMenu():
    formaMenu()
    with open("note.json") as file:
        data = json.load(file)
        print("Оглавление: ")
        for key, value in data.items():
            print(f'{key} - {value[0]}')
    formaMenu()

def formaMenu():
    print("#" * 30)

def errorId():
    print("Error!!! Не корректный id")

def errorEnter():
    print("Невернный ввод")

def errorEnterID():
    print("Невернный ввод! Такой id не найден")

def massegeAboutAdd():
    print(f"Заметка доабвлена!")

def goodCange():
    print("Заметка изменена успешно!")

def dontFindId():
    print("Неверный ввод. Такой id не найден")

def messegeAboutDalete():
    print("Заметка удалена успешно!")

def MessegeAboutAllDalete():
    print("Все заметки удалены!")


