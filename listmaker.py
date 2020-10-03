

class MyList:
    ls = []

    def __init__(self):
        return

    def __str__(self):
        return str(self.ls)

    def getList(self):
        return self.ls

    def append(self, *args):
        for i in range(len(args)):
            self.ls.append(args[i])

    def remove(self, *args):
        for i in range(len(args)):
            self.ls.remove(args[i])


def list_state():
    print(ls, "\n")


def remove_state():
    print("Current list:")
    print(ls)
    return input("Remove element from list \ninput: ")
    

def make_file(file, data):
    f = open(f"{file}.txt", "w", encoding="utf-8")
    f.write(data, "\n")
    f.close()


welcome = "Welcome to the List Maker App!"
menu = """Please select one of the following options:
1) Make new list
2) View current list
3) Add to current list
4) Remove from current list
5) Export list to file
6) Exit

>> """
user_input_sequence = "Add to list - use '/quit' to stop adding ~\ninput: "

while (user_input := input(menu)) != "6":
    if user_input == "1":
        # Make list
        ls = MyList()
        print("New list created: ")
        list_state()

    elif user_input == "2":
        if 'ls' not in locals():
            print('~Error!~\nNo list!... Create one in main menu!\n')
            ls = MyList()
        else:
            # View current list
            print("Current list state: ")
            list_state()

    elif user_input == "3":
        # Add to current list
        if 'ls' not in locals():
            print('~Error!~\nNo list!... Create one in main menu!\n')
            ls = MyList()
        else:
            seq_list = []
            while (input_sequence := input(user_input_sequence)) != '/quit':
                seq_list.append(input_sequence)
            for i in range(len(seq_list)):
                ls.append(seq_list[i])

    elif user_input == "4":
        # Remove from current list
        while (input_sequence := remove_state()) != '/quit':
                ls.remove(input_sequence)

    elif user_input == "5":
        # TODO Export list to file
        make_file('poopy', ls)

print("Goodbye!~\n")
