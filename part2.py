from addressbook import AddressBook, Record
import functools

def error_catcher(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return str(e)
    return wrapper

class AssistantBot:
    def __init__(self):
        self.book = AddressBook()

    @error_catcher
    def add_contact(self, name, phone):
        record = Record(name)
        record.add_phone(phone)
        self.book.add_record(record)


if __name__ == "__main__":
    bot = AssistantBot()
    response = bot.add_contact("John", "abcdefghij")  # це викличе помилку, тому що номер телефону не є числом
    print(response)  # повинно вивести помилку, яку перехоплює декоратор

