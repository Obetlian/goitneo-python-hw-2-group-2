from addressbook import AddressBook, Record
import functools

# Створюємо об'єкт адресної книги
book = AddressBook()

def error_catcher(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return str(e)
    return wrapper

@error_catcher
def add_contact(name, phone):
    record = Record(name)
    record.add_phone(phone)
    book.add_record(record)


if __name__ == "__main__":
    response = add_contact("John", "abcdefghij")  # це викличе помилку, тому що номер телефону не є числом
    print(response)  # повинно вивести помилку, яку перехоплює декоратор

