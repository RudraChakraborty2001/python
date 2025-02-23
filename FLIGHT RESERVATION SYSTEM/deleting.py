#Deleting a File
import os
if os.path.exists("riya.txt"):
    os.remove("riya.txt")
    print("File deleted.")
else:
    print("File does not exist.")