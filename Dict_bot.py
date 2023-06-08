import ast

dict_command = dict()

# dict_command["Привет"] = "Приветствую"

def write_data(dict_command):
    with open("bot_data.txt","w") as file:
        file.write((str)(dict_command))

def read_data():
    with open("bot_data.txt", "r") as file:
        dict_command = ast.literal_eval(file.read())
    return dict_command
dict_command = read_data()
# dict_command["Как дела?"] = "Хорошо, а у тебя?"
# write_data(dict_command)
# print(read_data()["Привет"])