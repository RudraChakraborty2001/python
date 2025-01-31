import re  

text = "Today's date is 30/01/2025 and my birthday is on 15-08-1995."
pattern = r"\b\d{2}[-/]\d{2}[-/]\d{4}\b"

# Find all dates
dates = re.findall(pattern, text)
print("Extracted Dates:", dates)
