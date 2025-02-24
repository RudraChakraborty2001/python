#Reading File into a List
with open("tom.txt", "r") as file:
    lines = file.readlines()
    print(lines)