phones = {}


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return 'Not enough arguments'
        except KeyError:
            return 'No such name in the phone book'
        except IndexError:
            return 'Please provide a name'

    return wrapper


@input_error
def add_contact(args):
    name, phone, *_ = args
    if name in phones:
        return f"Contact {name} already exists."

    phones[name] = phone
    return f"Contact {name} with phone {phone} was added."


@input_error
def change_contact(args):
    name, phone, *_ = args
    if name not in phones:
        return f"No such name in the phone book"
    phones[name] = phone
    return f"Contact {name} with phone {phone} was changed."


def show_contacts():
    for name, phone in phones.items():
        print(f"{name}: {phone}")


@input_error
def show_phone(args):
    name = args[0]
    return f"{name}: {phones[name]}"
