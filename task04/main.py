from input_parser import parse_input
import phone_base


def main():
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ").strip().lower()
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            result = phone_base.add_contact(args)
            print(result)
        elif command == "change":
            result = phone_base.change_contact(args)
            print(result)
        elif command == "phone":
            result = phone_base.show_phone(args)
            print(result)
        elif command == "all":
            phone_base.show_contacts()
        else:
            print("Invalid command.")


if __name__ == '__main__':
    main()
