# Розширення декоратора input_error для обробки різних виняткових ситуацій
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Дайте мені ім'я та номер телефону, будь ласка."
        except KeyError:
            return "Введіть ім'я користувача."
        except IndexError:
            return "Команда або вхідні дані неповні."
    return inner

# Функції управління контактами з обробкою помилок

contacts = {}

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Контакт додано."

@input_error
def delete_contact(args, contacts):
    name = args[0]
    del contacts[name]
    return "Контакт видалено."

@input_error
def show_contact(args, contacts):
    name = args[0]
    return contacts[name]

# Тестуємо функції з обробкою помилок
print(add_contact(("John", "123456789"), contacts))  # "Контакт додано."
print(show_contact(("John",), contacts))             # "123456789"
print(delete_contact(("John",), contacts))           # "Контакт видалено."
print(delete_contact(("John",), contacts))           # "Введіть ім'я користувача."
print(show_contact((), contacts))                    # "Команда або вхідні дані неповні."
print(add_contact(("Anna",), contacts))              # "Дайте мені ім'я та номер телефону, будь ласка."
