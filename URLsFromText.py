import re  

text = "Check out https://www.google.com and http://example.com for more info."
pattern = r"https?://[a-zA-Z0-9./-]+"  # Matches URLs starting with http or https

# Extract URLs
urls = re.findall(pattern, text)
print("Extracted URLs:", urls)
