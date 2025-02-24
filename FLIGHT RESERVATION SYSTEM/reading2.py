#Reading File Line by Line
with open("rudra.txt", "r") as file:
    for line in file:
        print(line.strip())