import re  

text = "The price is 100 dollars and 20 cents."
pattern = r"\d+"  # Match one or more digits

# Extract all numbers
numbers = re.findall(pattern, text)
print("Numbers found:", numbers)
