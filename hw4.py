def print_boxed_message(msg1, msg2):
    box_length = len(msg1) if (len(msg1) > len(msg2)) else len(msg2)
    print("-" * (box_length + 20))
    print(f"Hello {msg1}")
    print(f"Welcome to Seoul, {msg2}!")
    print("-" * (box_length + 20))

name = input("Enter the name in English: ")
print_boxed_message(name, name)
