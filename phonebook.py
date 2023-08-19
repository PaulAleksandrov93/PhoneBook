import json
from typing import List, Dict

# Файл, в котором будем хранить данные
data_file = "phonebook.json"


def load_data() -> List[Dict]:
    """
    Загружает данные из файла JSON и возвращает список словарей (записей).
    
    Returns:
        List[Dict]: Список словарей, содержащих записи из файла.
    """
    try:
        with open(data_file, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_data(data: List[Dict]) -> None:
    """
    Сохраняет данные в файл JSON.

    Args:
        data (List[Dict]): Список словарей (записей) для сохранения.
    """
    with open(data_file, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def add_entry() -> None:
    """
    Добавляет новую запись в телефонную книгу.
    """
    phonebook = load_data()
    entry = {
        "last_name": input("Фамилия: "),
        "first_name": input("Имя: "),
        "middle_name": input("Отчество: "),
        "organization": input("Организация: "),
        "work_phone": input("Рабочий телефон: "),
        "personal_phone": input("Личный телефон: ")
    }
    phonebook.append(entry)
    save_data(phonebook)
    print("Запись добавлена")


def list_entries(page: int, entries_per_page: int) -> None:
    """
    Выводит список записей на указанной странице.

    Args:
        page (int): Номер страницы для вывода.
        entries_per_page (int): Количество записей на одной странице.
    """
    phonebook = load_data()
    start_idx = (page - 1) * entries_per_page
    end_idx = start_idx + entries_per_page
    entries_to_show = phonebook[start_idx:end_idx]
    for idx, entry in enumerate(entries_to_show, start=start_idx + 1):
        print(f"{idx}. {entry['last_name']} {entry['first_name']} {entry['middle_name']}")
        print(f"   Организация: {entry['organization']}")
        print(f"   Рабочий телефон: {entry['work_phone']}")
        print(f"   Личный телефон: {entry['personal_phone']}")
        print()


def edit_entry(idx: int) -> None:
    """
    Редактирует существующую запись по указанному индексу.

    Args:
        idx (int): Индекс записи для редактирования.
    """
    phonebook = load_data()
    if 1 <= idx <= len(phonebook):
        entry = phonebook[idx - 1]
        print(f"Редактирование записи {entry['last_name']} {entry['first_name']} {entry['middle_name']}:")
        entry["last_name"] = input("Фамилия: ")
        entry["first_name"] = input("Имя: ")
        entry["middle_name"] = input("Отчество: ")
        entry["organization"] = input("Организация: ")
        entry["work_phone"] = input("Рабочий телефон: ")
        entry["personal_phone"] = input("Личный телефон: ")
        save_data(phonebook)
        print("Запись обновлена")
    else:
        print("Неверный индекс записи")


def search_entries() -> None:
    """
    Выполняет поиск записей по введенной пользователем строке.
    """
    query = input("Введите строку для поиска: ").lower()
    phonebook = load_data()
    found_entries = []
    for entry in phonebook:
        if (
            query in entry["last_name"].lower()
            or query in entry["first_name"].lower()
            or query in entry["middle_name"].lower()
            or query in entry["organization"].lower()
            or query in entry["work_phone"].lower()
            or query in entry["personal_phone"].lower()
        ):
            found_entries.append(entry)
    if found_entries:
        print("Результаты поиска:")
        for idx, entry in enumerate(found_entries, start=1):
            print(f"{idx}. {entry['last_name']} {entry['first_name']} {entry['middle_name']}")
            print(f"   Организация: {entry['organization']}")
            print(f"   Рабочий телефон: {entry['work_phone']}")
            print(f"   Личный телефон: {entry['personal_phone']}")
            print()
    else:
        print("Записи не найдены")


def main() -> None:
    """
    Основная функция для взаимодействия с пользователем.
    """
    while True:
        print("1. Вывести записи")
        print("2. Добавить запись")
        print("3. Редактировать запись")
        print("4. Поиск записей")
        print("5. Выйти")
        choice = input("Выберите действие: ")
        if choice == "1":
            page = int(input("Введите номер страницы: "))
            entries_per_page = 5
            list_entries(page, entries_per_page)
        elif choice == "2":
            add_entry()
        elif choice == "3":
            idx = int(input("Введите индекс записи для редактирования: "))
            edit_entry(idx)
        elif choice == "4":
            search_entries()
        elif choice == "5":
            break
        else:
            print("Неверный выбор")


if __name__ == "__main__":
    main()