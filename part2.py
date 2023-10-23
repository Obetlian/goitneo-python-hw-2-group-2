# Fields

def create_name(value):
    return value

def create_phone(value):
    if not str(value).isdigit() or len(str(value)) != 10:
        raise ValueError("Phone number should have 10 digits.")
    return value

# Records

def create_record(name):
    return {"name": create_name(name), "phones": []}

def add_phone_to_record(record, phone):
    record["phones"].append(create_phone(phone))

def remove_phone_from_record(record, phone):
    record["phones"] = [p for p in record["phones"] if p != phone]

def edit_phone_in_record(record, old_phone, new_phone):
    new_phones = [create_phone(new_phone) if p == old_phone else p for p in record["phones"]]
    record["phones"] = new_phones

def find_phone_in_record(record, phone):
    return phone if phone in record["phones"] else None

def str_record(record):
    return f"Contact name: {record['name']}, phones: {'; '.join(record['phones'])}"

# AddressBook

address_book = {}

def add_record_to_book(record):
    address_book[record["name"]] = record

def find_record_in_book(name):
    return address_book.get(name)

def delete_record_from_book(name):
    if name in address_book:
        del address_book[name]

# Main

def main():
    john_record = create_record("John")
    add_phone_to_record(john_record, "1234567890")
    add_phone_to_record(john_record, "5555555555")
    add_record_to_book(john_record)

    jane_record = create_record("Jane")
    add_phone_to_record(jane_record, "9876543210")
    add_record_to_book(jane_record)

    print("All records in the address book:")
    for name, record in address_book.items():
        print(str_record(record))

    john = find_record_in_book("John")
    edit_phone_in_record(john, "1234567890", "1112223333")

    print("\nJohn's updated record:")
    print(str_record(john))

    found_phone = find_phone_in_record(john, "5555555555")
    print(f"\n{john['name']}'s found phone: {found_phone}")

    delete_record_from_book("Jane")
    print("\nAll records in the address book after deleting Jane:")
    for name, record in address_book.items():
        print(str_record(record))

if __name__ == "__main__":
    main()


