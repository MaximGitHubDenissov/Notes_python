import models as md
import view 

def main_menu_button():
    while True:
        chs = view.main_menu()
        if chs == '1':
             md.create_note()
        elif chs == '2':
            search_menu_button()
        elif chs == '3':
            md.show_all()
        elif chs == '4':
            result = md.search_note("id")
            if len(result)>0:
                update_menu_button(result)
        elif chs == '5':
            result = md.search_note("id")
            if len(result)>0:
                view.show_notes(result)
                md.delete_note(result)
        elif chs == '0':
            print("Спасибо за использование приложения заметки! Возвращайтесь снова")
            break




def search_menu_button():
    while True:
        chs = view.search_menu()
        if chs == '1':
            result = md.search_note("id")
            if len(result)>0:
                view.show_notes(result)
        elif chs == '2':
            result = md.search_note("title")
            if len(result)>0:
                view.show_notes(result)

        elif chs == '0':
            break

def update_menu_button(result):
        chs = view.update_menu()
        if chs == '1':
            md.update_note(result, 'title')
        elif chs == '2':
            md.update_note(result, 'text')        

main_menu_button()