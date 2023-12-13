import Note


def create_note(number):
    title = check_len_text_input(
        input('Введите Название заметки: '), number)
    body = check_len_text_input(
        input('Введите Описание заметки: '), number)
    return Note.Note(title=title, body=body)


def menu():
    print("\nЭто программа 'Заметки'. Здесь вы можете:\n\n1 - показать все имеющиеся заметки\n2 - добавить заметку\n3 - удалить заметку\n4 - редактировать заметку\n5 - найти замету по дате\n6 - показать заметку по id\n7 - выход\n\nВведите номер функции: ")


def check_len_text_input(text, n):
    while len(text) <= n:
        print(f'Текст должен быть больше {n} символов\n')
        text = input('Введите тескт: ')
    else:
        return text


def goodbuy():
    print("Досвидания, ждем вас снова.")