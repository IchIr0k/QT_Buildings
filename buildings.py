from cls_structure import Structure
from cls_sale import Sale
import sqlite3

structure_db = Structure()
sale_db = Sale()
def view_all():
    con = sqlite3.connect("Building_.db")
    cur = con.cursor()

    print("\n--- Таблица Structure ---")
    for row in cur.execute("SELECT * FROM Structure"):
        print(row)

    print("\n--- Таблица Sale ---")
    for row in cur.execute("""
        SELECT Sale.id, Structure.type_of_structure, Sale.num_of_rooms, Sale.Footage, Sale.price
        FROM Sale
        JOIN Structure ON Sale.type_of_structure = Structure.id_building
    """):
        print(row)

    con.close()

view_all()

def show_menu():
    print("\n--- МЕНЮ ---")
    print("1. Добавить тип строения")
    print("2. Добавить запись в Sale")
    print("3. Удалить запись из Structure")
    print("4. Удалить запись из Sale")
    print("5. Просмотреть таблицу Structure")
    print("6. Просмотреть таблицу Sale")
    print("7. Выйти")

def add_structure():
    type_build = input("Введите тип строения: ")
    structure_db.insert(type_build)
    print("Добавлено.")

def add_sale():
    type_of_structured = input("Введите тип строения (должен быть добавлен заранее): ")
    result = structure_db.search(type_of_structured)
    if result:
        type_of_structure = result[0][0]
        try:
            num_of_rooms = int(input("Количество комнат: "))
            footage = float(input("Метраж: "))
            price = float(input("Цена: "))
            sale_db.insert(type_of_structure, num_of_rooms, footage, price)
            print("Добавлено.")
        except ValueError:
            print("Ошибка: неверный формат чисел.")
    else:
        print("Такой тип строения не найден. Добавьте его сначала в Structure.")

def delete_structure():
    try:
        id_build = int(input("Введите ID строения для удаления: "))
        structure_db.cur.execute("DELETE FROM Structure WHERE id_building = ?", (id_build,))
        structure_db.con.commit()
        print("Удалено.")
    except ValueError:
        print("Ошибка: неверный ID.")

def delete_sale():
    try:
        id_sale = int(input("Введите ID записи из Sale для удаления: "))
        sale_db.cur.execute("DELETE FROM Sale WHERE id = ?", (id_sale,))
        sale_db.con.commit()
        print("Удалено.")
    except ValueError:
        print("Ошибка: неверный ID.")

def view_structure():
    rows = structure_db.view()
    print("\n--- Таблица Structure ---")
    for row in rows:
        print(row)

def view_sale():
    rows = sale_db.view_with_type()
    print("\n--- Таблица Sale ---")
    for row in rows:
        print(row)

def main():
    while True:
        show_menu()
        choice = input("Выберите действие: ")

        if choice == "1":
            add_structure()
        elif choice == "2":
            add_sale()
        elif choice == "3":
            delete_structure()
        elif choice == "4":
            delete_sale()
        elif choice == "5":
            view_structure()
        elif choice == "6":
            view_sale()
        elif choice == "7":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Повторите.")

if __name__ == "__main__":
    main()
