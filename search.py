import json

with open("data.json", "r") as file:
    data = json.load(file)


def update_table_names(new_table_names):
    with open("data.json", "r+") as file:
        data = json.load(file)
        for table_name in new_table_names:
            if table_name not in data:
                data[table_name] = {}
        file.seek(0)
        json.dump(data, file, indent=4)
        file.truncate()


def update_column_names(table_name, new_column_names):
    with open("data.json", "r+") as file:
        data = json.load(file)
        if table_name in data:
            for column_name in new_column_names:
                if column_name not in data[table_name]:
                    data[table_name][column_name] = []
        file.seek(0)
        json.dump(data, file, indent=4)
        file.truncate()


def update_data(table_name, column_name, new_data):
    with open("data.json", "r+") as file:
        data = json.load(file)
        if table_name in data and column_name in data[table_name]:
            for item in new_data:
                if item not in data[table_name][column_name]:
                    data[table_name][column_name].append(item)
        file.seek(0)
        json.dump(data, file, indent=4)
        file.truncate()


def get_table_names(json_file_path):
    with open(json_file_path, "r") as file:
        data = json.load(file)
        table_names = list(data.keys())
    return table_names


def get_column_names(json_file_path, table_name):
    with open(json_file_path, "r") as file:
        data = json.load(file)
        if table_name in data:
            column_names = list(data[table_name].keys())
        else:
            column_names = []
    return column_names


def get_data(json_file_path, table_name, column_name):
    with open(json_file_path, "r") as file:
        data = json.load(file)
        if table_name in data and column_name in data[table_name]:
            column_data = data[table_name][column_name]
        else:
            column_data = []
    return column_data
