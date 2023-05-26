# Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, 
# и Вы должны реализовать функционал для изменения и удаления данных

def addLine(filename, name = "---", phoneNumber = "---", adress = "---"):
    with open(filename, 'a') as file:
        file.write(name + '\t' + phoneNumber + '\t' + adress + '\n')

def deleteLine(filename, lineNumber):
    with open(filename) as file:
        lines = file.readlines()

    if (lineNumber <= len(lines)):
        del lines[lineNumber - 1]
        with open(filename, "w") as file:
            for line in lines:
                file.write(line)
    else:
        print("Строки", lineNumber, "нету в файле.")
        print("В файле", len(lines), "строк(а/и).")

def changeLine(filename, lineNumber, name = "---", phoneNumber = "---", adress = "---"):
    with open(filename) as file:
        lines = file.readlines()

    if (lineNumber <= len(lines)):
        lines[lineNumber - 1] = f"{name}\t{phoneNumber}\t{adress}\n"
        with open(filename, "w") as file:
            for line in lines:
                file.write(line)
    else:
        print("Строки", lineNumber, "нету в файле.")
        print("В файле", len(lines), "строк(а/и).")

answer = input("Удалить, добавить или изменить строку?\n--> ")
if answer == "Удалить": deleteLine(input("Название файла: "), int(input("Номер строки: ")))
elif answer == "Добавить": addLine(input("Название файла: "), input("Имя: "), input("Номер: "), input("Адресс: "))
elif answer == "Изменить": changeLine(input("Название файла: "), int(input("Номер строки: ")), input("Имя: "), input("Номер: "), input("Адресс: "))
else: print("Не подходящий аргумент, попробуйте ввести 'Удалить', 'Добавить' или 'Изменить'")
