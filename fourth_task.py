from venv.commands_bot import (
    parse_input, add_contact,
    change_contact, show_all,
    show_phone)


def main():
    # Створюємо порожній словник для контактів
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        # Отримує дані від користувача
        user_input = input("Enter a command: ")
        # Парсить дані введені користувачем на команду та аргументи
        command, args = parse_input(user_input)

        match command:
            # Якщо ввели команду "close" або "exit", програма завершує роботу
            case "close":
                print("Good bye!")
                break
            case "exit":
                print("Good bye!")
                break
            # Якщо ввели команду "hallo", виводяться привітання
            case "hello":
                print("How can I help you?")
            # Якщо ввели команду "add", додається контакт
            case "add":
                print(add_contact(args, contacts))
            # Якщо ввели команду "change", змінюєтьса існуючий номер
            case "change":
                print(change_contact(args, contacts))
            # Якщо ввели команду "phone", виводяться номер телефону
            case "phone":
                print(show_phone(args, contacts))
            # Якщо ввели команду "all", виводяться всі контакти
            case "all":
                print(show_all(contacts))
            # Якщо команда не розпізнана, виводить повідомлення про помилку
            case _:
                print("Invalid command.")

if __name__ == "__main__":
    # Запускаємо головну функцію
    main()