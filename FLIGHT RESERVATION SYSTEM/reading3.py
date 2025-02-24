#Reading Specific Number of Characters
with open("example.txt", "r") as file:
    content = file.read(5)  # Read first 5 characters
    print(content)