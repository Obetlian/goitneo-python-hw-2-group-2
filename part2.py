from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        if len(value) == 10 and value.isdigit():
            super().__init__(value)
        else:
            raise ValueError("Phone number must be 10 digits")

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)

    def edit_phone(self, old_phone, new_phone):
        for index, p in enumerate(self.phones):
            if p.value == old_phone:
                self.phones[index] = Phone(new_phone)

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p.value
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name, None)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

class AssistantBot:
    def __init__(self):
        self.book = AddressBook()

    def hello(self):
        return "How can I help you?"

    def add_contact(self, name, phone):
        record = self.book.find(name)
        if not record:
            record = Record(name)
            self.book.add_record(record)
        record.add_phone(phone)
        return f"Контакт {name} збережено з номером {phone}."

    def find_contact(self, name):
        record = self.book.find(name)
        return str(record) if record else f"Контакт {name} не знайдено."

    def update_contact(self, name, new_phone):
        record = self.book.find(name)
        if record:
            # Assuming first phone number is the main one.
            record.edit_phone(record.phones[0].value, new_phone)
            return f"Номер {name} оновлено до {new_phone}."
        else:
            return f"Контакт {name} не знайдено."

    def list_contacts(self):
        return '\n'.join([str(record) for record in self.book.data.values()])

    def command_handler(self, command, *args):
        if command == "hello":
            return self.hello()
        elif command == "add" and len(args) == 2:
            return self.add_contact(args[0], args[1])
        elif command == "phone" and len(args) == 1:
            return self.find_contact(args[0])
        elif command == "change" and len(args) == 2:
            return self.update_contact(args[0], args[1])
        elif command == "all":
            return self.list_contacts()
        else:
            return "Невідома команда!"

    def run(self):
        print("Бот-помічник готовий до роботи!")
        while True:
            user_input = input("> ").strip().lower()
            if user_input in ['exit', 'close']:
                print("До побачення!")
                break
            command_parts = user_input.split()
            print(self.command_handler(command_parts[0], *command_parts[1:]))

if __name__ == "__main__":
    bot = AssistantBot()
    bot.run()
