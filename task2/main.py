def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    try:
        name, phone = args
    except ValueError:
        return "Incorrect contact information. Please try again. Should be 'add name phone'"
    else:
        if name in contacts:
            answer = input("This contact already exists. Do you want to rewrite this contact? Press 1 if yes, 0 if no\n")
            if answer == '0':
                return "Contact hasn't been modified"
            contacts[name] = phone
            return "Contact added."
    
def change_contact(args, contacts):
    try:
        name, phone = args
    except ValueError:
        return "Incorrect contact information. Please try again. Should be 'change name phone'"
    else:
        if name in contacts:
            contacts[name] = phone
            return "Contact updated."
        else:
            answer = input("This contact doesn't exist. Do you want to add this contact? Press 1 if yes, 0 if no\n")
            if answer == '0':
                return "Contact hasn't been added"
            contacts[name] = phone
            return "Contact added."
        
def show_phone(args, contacts):
    try:
        name = args[0]
    except ValueError:
        return "Incorrect contact information. Please try again. Should be 'phone name'"
    else:
        if name in contacts:
            return contacts[name]
        else:
            return "Contact not found."

def show_all(contacts):
    return contacts

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Goodbye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
