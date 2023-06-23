
def main_menu():
    print("Добро пожаловать в приложение заметки\n\
          Главное меню:\n\
          1 - Создать заметку\n\
          2 - Найти заметку\n\
          3 - Просмотреть все заметки\n\
          4 - Редактировать заметку\n\
          5 - Удалить заметку\n\
          0 - Выход")
    while True:
        chs = input("Введите номер комнады: ")
        if chs in ['0','1', '2', '3','4','5']:
            return chs
        else: print("Неверный номер команды")

def data_input(text):
    print(text)
    data = input()
    return data

def search_menu():
    print("Перед Вами меню поиска:\n\
          1 - Найти заметку по id\n\
          2 - Найти заметку по заголовку\n\
          0 - Вернуться в главное меню")
    while True:
        chs = input("Введите номер команды: ")
        if chs in ['0','1','2','3']:
            return chs
        else: print("Неверный номер команды")

def show_notes(arr):
    for item in arr:
        print(f"ID заметки: {item['id']}\n")
        print(f"Дата создания заметки: {item['date']}\n")
        print(f"Заголовок заметки: {item['title']}\n")
        print(f"Текст заметки: {item['text']}")
        print('--------------------------------------')
        

def update_menu():
    print("Что Вы хотите поменять в этой заметке?:\n\
          1 - Заголовок\n\
          2 - Текст\n")
    while True:
        chs = input("Введите номер комнады: ")
        if chs in ['1','2']:
            return chs
        else: print("Неверный номер команды")
