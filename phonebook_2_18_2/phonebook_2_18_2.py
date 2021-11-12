import json


def exit_():
    command_1 = input("Выход(Е/n): ")
    if command_1.lower() == "e":
        exit(0)


def add_new(telephone_number, first_name, last_name, city):
    full_name = first_name + " " + last_name
    entries = {telephone_number: {"first": first_name,
                                  "last": last_name,
                                  "full": full_name,
                                  "city": city}}
    return entries


def add_to_file(entries_, file):
    try:
        with open(file) as phonebook:
            data = json.load(phonebook)
    except json.decoder.JSONDecodeError:
        data = dict()
    data.update(entries_)
    with open(file, "w+") as phonebook:
        json.dump(data, phonebook, indent=4)
    return True


def search(search_by, file):
    with open(file) as phonebook:
        data_1 = json.load(phonebook)
        list_result = []
        for key_1 in data_1:
            if key_1 == search_by:
                list_result.append(f"{key_1}, {data_1[key_1]}")
            data_2 = data_1[key_1]
            for value in data_2.values():
                if value == search_by:
                    list_result.append(f"{key_1}, {data_1[key_1]}")
    return list_result


def delete(phone_number, file):
    key = phone_number
    with open(file, "r") as phonebook:
        data = json.load(phonebook)
    if data.get(key):
        del data[key]
    else:
        return False
    with open(file, "w") as phonebook:
        json.dump(data, phonebook, indent=4)
    return True


def always_dict(file):
    with open(file) as phonebook:
        data = json.load(phonebook)
    return data


def command():
    command_ = input("Какое действие ты хочешь сделать (запись-А, поиск-S, обновление для номера-U, удаление-D, "
                     "весь словарь-О, выход-Е: ")
    if command_.lower() == "a":
        add_new()
    elif command_.lower() == "s":
        search()
    elif command_.lower() == "u":
        add_new()
    elif command_.lower() == "o":
        always_dict()
    elif command_.lower() == "d":
        delete()
    exit_()


if __name__ == "__main__":
    # add_to_file({"47": "23"}, "Phonebook.json")
    command()
