#Writing Multiple Lines to a File
lines = ["First line\n", "Second line\n", "Third line\n"]
with open("tom.txt", "w") as file:
    file.writelines(lines)