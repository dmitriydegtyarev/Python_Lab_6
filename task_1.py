def insert_element():

    usr_lst = input("Введіть будь ласка елементи списку через пробіл: ").split()
    target = input("Введіть елемент, після якого вставити новий: ")
    new_el = input("Введіть новий елемент для вставки: ")

    if target in usr_lst:
        index = usr_lst.index(target)
        usr_lst.insert(index + 1, new_el)
        print ("Оновлений список:",usr_lst)
    else:
        print("Елемент не знайдено!")

insert_element()