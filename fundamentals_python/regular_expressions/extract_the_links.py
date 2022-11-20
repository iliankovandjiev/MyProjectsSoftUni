import re

text_input = input()
while text_input:
    pattern = r'www\.[A-Za-z0-9\-]+(\.[a-z]+)+'
    valid_urls = re.finditer(pattern, text_input)
    for url in valid_urls:
        print(url.group())
    text_input = input()