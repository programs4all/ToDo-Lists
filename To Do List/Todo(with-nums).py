def load_todo():
    rf = open("TODO.txt", "r+")
    data = []
    while True:
        line = rf.readline()
        if line == "":
            break
        data.append(line.strip("\n"))
    rf.close()
    print(data)
    return data


def display_todo(data):
    print("----------------------TODO LIST---------------------")
    print("|Q| to quit |del| to delete |add| just start typing!")
    cnt = 1
    for line in data:
        print(f"{cnt}:  {line}")
        cnt += 1


# note: somewhat wasteful, looping through all items and rewriting to del one item
def remove_todo(n, data):
    wf = open("TODO.txt", "w")
    del_val = data[n]
    for line in data:
        if line != del_val:
            line = f"{line}\n"
            wf.write(line)
    print(f"deleted: '{del_val}'")
    wf.close()


def add_todo(string, data):
    wf = open("TODO.txt", "w")
    for line in data:
        line = f"{line}\n"
        wf.write(line)
    string = f"{string}\n"
    wf.write(string)
    wf.close()


# ----------------------------------------GUI--------------------------------------
while True:
    td = load_todo()
    length = len(td)
    display_todo(td)

    entry = input()

    if entry == "Q":
        sure = input("Are you sure you want to exit?").lower()
        if sure.startswith("y"):
            break

    elif entry == "del":
        num = input("Well done what number did you get done?")
        if num == '':
            remove_todo(length - 1, load_todo())
        else:
            error = "------------ERROR------------"
            try:
                num = int(num)

            except ValueError as err:
                print("\n", error)
                print("Please return a number: ", err)
                print(error, "\n")

            else:
                num -= 1
                if num < length:
                    remove_todo(num, load_todo())
                else:
                    print("\n")
                    print(error)
                    print("your entry was out of range")
                    print(error, "\n")

    elif not entry.startswith(" "):
        add_todo(entry.capitalize(), load_todo())

print("exited")
