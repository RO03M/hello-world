import string
import random
alphabetList = string.ascii_letters


def filename():
    name_file = []
    for name in range(0, 20):
        if name % 2 == 0:
            name_file.append(alphabetList[random.randint(0, len(alphabetList) - 1)])
        else:
            name_file.append(f"{random.randint(0, 9)}")
    name_file = "".join(name_file)
    return name_file + ".txt"


while True:
    try:
        fileCreated = filename()
        createFile = open(fileCreated, "x")
    except FileExistsError:
        continue
    except Exception as error:
        print(error.__class__)
    else:
        print(f"O arquivo '{fileCreated}' foi criado com sucesso!")
        break
