import view
from datetime import datetime
import json

now = datetime.now()

def save_note(record):
    with open("data.json",) as file:
        data = json.load(file)
        data['notes'].append(record)
    with open("data.json", "w") as file:
        json.dump(data,file)    

def new_id():
    with open ("id.txt", 'r') as file:
        id = file.readline()
        new_id = int(id)+1
    with open ("id.txt", 'w') as file:
        file.write(str(new_id))
    return str(new_id)


def create_note():
    id = new_id()
    
    time = ("{}.{}.{}  {}:{}".format(now.day, now.month, now.year, now.hour, now.minute))
    title = view.data_input("Введите название заголовка:\n")
    text = view.data_input("Введите текст записки")
    data = {'id':id, 'date':time, 'title':title, 'text':text}
    save_note(data)
    print("Записка успешно сохранена!")

def search_note(data):
    search = view.data_input(f"Введите {data}: ")
    result = []
    with open ("data.json") as file:
        repos = json.load(file)
        for item in repos['notes']:
            if item[data] == search:
                result.append(item)
    if len(result) == 0:
        print("Заметка с заданными параметрами не найдена!")
    return result
def show_all():
    with open('data.json') as file:
        data  = json.load(file)
    view.show_notes(data['notes'])

def update_note(data, name):
    if name == 'title':
        data[0]['title'] = view.data_input("Введите новый заголовок")
    elif name == 'text':
        data[0]['text'] = view.data_input("Введите новый текст")
    data[0]['date'] = ("{}.{}.{}  {}:{}".format(now.day, now.month, now.year, now.hour, now.minute))
    with open ('data.json') as file:
        repos = json.load(file)
        arr = repos['notes']
        for i in range (len(arr)):
            if arr[i]['id'] == data[0]['id']:
                arr[i] = data[0]
    print("Заметка успешно изменена!")
    with open('data.json', 'w') as file:
        json.dump(repos,file)
            
def delete_note(data):
    with open ('data.json') as file:
        repos = json.load(file)
        arr = repos['notes']
        for i in range (len(arr)):
            if arr[i]['id'] == data[0]['id']:
                del(arr[i])
    print("Заметка успешно удалена!")
    with open('data.json', 'w') as file:
        json.dump(repos,file)
                
            
