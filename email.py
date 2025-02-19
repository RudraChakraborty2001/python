import re  # Importing the regular expression module

# Sample text
text = "My email is example123@gmail.com and my friend's email is test.email@domain.org"

# Regular expression pattern to match email addresses
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

# Using re.findall() to extract all email addresses from the text
emails = re.findall(email_pattern, text)

# Printing the extracted email addresses
print("Extracted Emails:", emails)