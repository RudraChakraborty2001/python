import re  

text = "Hello World!"
pattern = r"^[A-Z]"  # Checks if the first character is an uppercase letter

if re.match(pattern, text):
    print("Starts with a capital letter")
else:
    print("Does not start with a capital letter")
