def read_files(filepath: str):
    with open(filepath,'r') as file:
        lines = file.readlines()

    return lines


lines = read_files()
print(lines)




