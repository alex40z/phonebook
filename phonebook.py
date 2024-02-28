def work_with_phonebook():
    choice = show_menu()
    phone_book = read_txt('phonebook.txt')
    while (choice != 7):
        if choice==1:
            phone_num = int(input('Номер строки:'))
            copy_phone(phone_book, phone_num, 'new_phonebook.txt')
        choice=show_menu()

def show_menu():
    print("\n Выберите необходимое действие:\n",
          "1. Скопировать строку в файл\n",
          "7. Закончить работу")
    choice = int(input())
    return choice

def read_txt(filename): 
    phone_book = []
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    with open(filename, 'r', encoding = 'utf-8') as phb:
        for line in phb:
            record = dict(zip(fields, line.split(',')))
            phone_book.append(record)	
    return phone_book

def copy_phone(phone_book, phone_num, filename):
    with open(filename, 'a', encoding = 'utf-8') as phcopy:
        s = ''
        for v in phone_book[phone_num].values():
            s = s + v + ','
        phcopy.write(f'{s[:-1]}\n')

work_with_phonebook()
