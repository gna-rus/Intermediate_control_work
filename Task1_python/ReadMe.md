# Домашняя работа
## Исполнитель: Григорьев Николай

## Задание:
Реализовать консольное приложение заметки, с сохранением, чтением,
добавлением, редактированием и удалением заметок. Заметка должна
содержать идентификатор, заголовок, тело заметки и дату/время создания или
последнего изменения заметки. Сохранение заметок необходимо сделать в
формате json или csv формат (разделение полей рекомендуется делать через
точку с запятой). Реализацию пользовательского интерфейса студент может
делать как ему удобнее, можно делать как параметры запуска программы
(команда, данные), можно делать как запрос команды с консоли и
последующим вводом данных, как-то ещё, на усмотрение студента.


## Пояснительная записка:
1. Заметки храняться в формате json и каждая запись имеет структуру записи:
>"id": [
    "Заголовок",
    "Текст заметки",
    1987429991.0 
  ]

id имеет формат int;
Заголовок и Текст заметки - формат str;
1987429991.0 - это время, переконвертируемое из секунд в дату (в файле у некоторых заметок это число искуственно сгенерировано - это нужно было для тестов работы сортировки).

2. При запуске открывается меню которое включает в себя следующие команды для ввода:
add - добавить элемент в заметки (при этом в начале запросит ввести заголовок новой заметки а потом и сам текст)
read - прочесть заметку по id или все заметки (выводит отсортированные заголовки заметок, если ввести id то выведет текст отдельно взятой заметки, если all то выведет текст всех заметок
edit - редактировать заметку по id (выводит отсортированные заголовки заметок и их id, после ввода id программа запросит ввести новый заголовок и новый текст)
sort - осуществить сортировку заметок (проводит сортировку по id или по дате создания заметки (все даты переведены в секунды))
clear - удалить заметку по id или все заметки (удаляет отдельно взятую заметку по id или все скопом)
exit - Выход
