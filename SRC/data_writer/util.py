def info(s):
    print(f'\033[4mINFO: {s.__str__()}\033[0m')

def read_sql_file(file_name: str) -> str:
    with open(f'../SQL/{file_name}', 'r') as file:
        file_contents = file.read()

    return file_contents