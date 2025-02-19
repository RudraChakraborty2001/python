import re  

phone = "+1-123-456-7890"
pattern = r"^\+\d{1,2}-\d{3}-\d{3}-\d{4}$"

# Check if the phone number matches the pattern
if re.match(pattern, phone):
    print("Valid Phone Number")
else:
    print("Invalid Phone Number")
